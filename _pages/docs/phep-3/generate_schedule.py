import requests
import collections
from datetime import datetime, timedelta

import pandas as pd
from packaging.version import Version


py_releases = {
    "3.9": "Oct 5, 2020",
    "3.10": "Oct 4, 2021",
    "3.11": "Oct 24, 2022",
    "3.12": "Oct 2, 2023",
    "3.13": "Oct 7, 2024",
    "3.14": "Oct 7, 2025"
}
core_packages = [
    "numpy",
    "scipy",
    "matplotlib",
    "pandas",
    "scikit-image",
    "networkx",
    "scikit-learn",
    "xarray",
    "ipython",
    "zarr"
]
plus36 = timedelta(days=int(365 * 3))
plus24 = timedelta(days=int(365 * 2))
plus6 = timedelta(days=int(365 * 0.5))

# Release data

# put cutoff 3 quarters ago – we do not use "just" -9 month,
# to avoid the content of the quarter to change depending on when we generate this
# file during the current quarter.

current_date = pd.Timestamp.now()
current_quarter_start = pd.Timestamp(
    current_date.year, (current_date.quarter - 1) * 3 + 1, 1
)
cutoff = current_quarter_start - pd.DateOffset(months=9)


def get_release_dates(package, support_time=plus24):
    releases = {}

    print(f"Querying pypi.org for {package} versions...", end="", flush=True)
    response = requests.get(
        f"https://pypi.org/simple/{package}",
        headers={"Accept": "application/vnd.pypi.simple.v1+json"},
    ).json()
    print("OK")

    file_date = collections.defaultdict(list)
    for f in response["files"]:
        ver = f["filename"].split("-")[1]
        try:
            version = Version(ver)
        except:
            continue

        if version.is_prerelease or version.micro != 0:
            continue

        release_date = None
        for format in ["%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ"]:
            try:
                release_date = datetime.strptime(f["upload-time"], format)
            except:
                pass

        if not release_date:
            continue

        file_date[version].append(release_date)

    release_date = {v: min(file_date[v]) for v in file_date}

    for ver, release_date in sorted(release_date.items()):
        drop_date = release_date + support_time
        if drop_date >= cutoff:
            releases[ver] = {
                "release_date": release_date,
                "drop_date": drop_date,
                "support_by_date": release_date + plus6
            }

    return releases


package_releases = {
    "python": {
        version: {
            "release_date": datetime.strptime(release_date, "%b %d, %Y"),
            "drop_date": datetime.strptime(release_date, "%b %d, %Y") + plus36,
            "support_by_date": datetime.strptime(release_date, "%b %d, %Y") + plus6
        }
        for version, release_date in py_releases.items()
    }
}

package_releases |= {package: get_release_dates(package) for package in core_packages}

# filter all items whose drop_date are in the past
package_releases = {
    package: {
        version: dates
        for version, dates in releases.items()
        if dates["drop_date"] > cutoff
    }
    for package, releases in package_releases.items()
}


# Save Gantt chart
# You can paste the contents into https://mermaid.live/ to generate the chart image.

print("Saving Mermaid chart to chart.md (render at https://mermaid.live/)")
with open("chart.md", "w") as fh:
    fh.write(
        """gantt
dateFormat YYYY-MM-DD
axisFormat %m / %Y
title Support Window"""
    )

    for name, releases in package_releases.items():
        fh.write(f"\n\nsection {name}")
        for version, dates in releases.items():
            fh.write(
                f"\n{version} : {dates['release_date'].strftime('%Y-%m-%d')},{dates['drop_date'].strftime('%Y-%m-%d')}"
            )
    fh.write("\n")

# Print drop schedule

data = []
for k, versions in package_releases.items():
    for v, dates in versions.items():
        data.append(
            (
                k,
                v,
                pd.to_datetime(dates["release_date"]),
                pd.to_datetime(dates["drop_date"]),
                pd.to_datetime(dates["support_by_date"]),
            )
        )

df = pd.DataFrame(data, columns=["package", "version", "release", "drop", "support_by"])

df["quarter_drop"] = df["drop"].dt.to_period("Q")
df["quarter_support_by"] = df["support_by"].dt.to_period("Q")

dq_drop = df.set_index(["quarter_drop", "package"]).sort_index()
dq_support_by = df.set_index(["quarter_support_by", "package"]).sort_index()


print("Saving support schedule to schedule.md")


def pad_table(table):
    rows = [[el.strip() for el in row.split("|")] for row in table]
    col_widths = [max(map(len, column)) for column in zip(*rows)]
    rows[1] = [
        el if el != "----" else "-" * col_widths[i] for i, el in enumerate(rows[1])
    ]
    padded_table = []
    for row in rows:
        line = ""
        for entry, width in zip(row, col_widths):
            if not width:
                continue
            line += f"| {str.ljust(entry, width)} "
        line += f"|"
        padded_table.append(line)

    return padded_table


def make_table(sub):
    table = []
    table.append("|    |    |    |")
    table.append("|----|----|----|")
    for package in sorted(set(sub.index.get_level_values(0))):
        vers = sub.loc[[package]]["version"]
        minv, maxv = min(vers), max(vers)
        rels = sub.loc[[package]]["release"]
        rel_min, rel_max = min(rels), max(rels)
        version_range = str(minv) if minv == maxv else f"{minv} to {maxv}"
        rel_range = (
            str(rel_min.strftime("%b %Y"))
            if rel_min == rel_max
            else f"{rel_min.strftime('%b %Y')} and {rel_max.strftime('%b %Y')}"
        )
        table.append(f"|{package:<15}|{version_range:<19}|released {rel_range}|")

    return pad_table(table)


def make_adopt_table(sub):
    table = []
    table.append("|    |    |    |")
    table.append("|----|----|----|")
    for package in sorted(set(sub.index.get_level_values(0))):
        vers = sub.loc[[package]]["version"]
        minv, maxv = min(vers), max(vers)
        support_bys = sub.loc[[package]]["support_by"]
        support_by_min, support_by_max = min(support_bys), max(support_bys)
        version_range = str(minv) if minv == maxv else f"{minv} to {maxv}"
        support_by_range = (
            str(support_by_min.strftime("%b %Y"))
            if support_by_min == support_by_max
            else f"{support_by_min.strftime('%b %Y')} and {support_by_max.strftime('%b %Y')}"
        )
        table.append(f"|{package:<15}|{version_range:<19}|support by {support_by_range}|")

    return pad_table(table)


def make_quarter(quarter, dq_drop, dq_support_by):
    table = ["#### " + str(quarter).replace("Q", " - Quarter ") + ":\n"]

    # Add new versions adoption schedule if not empty
    if quarter in dq_support_by.index.get_level_values(0):
        table.append("###### Adopt support for:\n")
        adopt_sub = dq_support_by.loc[quarter]
        adopt_table = make_adopt_table(adopt_sub)
        table.extend(adopt_table)

    table.append("\n###### Can drop support for:\n")
    sub = dq_drop.loc[quarter]
    table.extend(make_table(sub))

    return "\n".join(table)


with open("schedule.md", "w") as fh:
    # we collect package 6 month in the past, and drop the first quarter
    # as we might have filtered some of the packages out depending on
    # when we ran the script.
    tb = []
    for quarter in list(sorted(set(dq_drop.index.get_level_values(0))))[1:]:
        tb.append(make_quarter(quarter, dq_drop, dq_support_by))

    fh.write("\n\n".join(tb))
    fh.write("\n")
