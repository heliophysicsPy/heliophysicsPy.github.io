"""
Generate email content for PHEP 3 quarterly reminders.
Parses schedule.md and extracts the current quarter's information.
"""

import re
from datetime import datetime
from pathlib import Path


def get_current_quarter():
    """Return current year and quarter (1-4)."""
    now = datetime.now()
    quarter = (now.month - 1) // 3 + 1
    return now.year, quarter


def parse_schedule(schedule_path):
    """Parse schedule.md and return dict of quarters with their content."""
    content = Path(schedule_path).read_text()

    # Split by quarter headers (#### YYYY - Quarter N:)
    quarter_pattern = r'#### (\d{4}) - Quarter (\d):'
    sections = re.split(quarter_pattern, content)

    quarters = {}
    # sections[0] is empty/before first match, then year, quarter, content triplets
    for i in range(1, len(sections) - 2, 3):
        year = int(sections[i])
        quarter = int(sections[i + 1])
        quarter_content = sections[i + 2].strip()
        quarters[(year, quarter)] = quarter_content

    return quarters


def parse_table(table_text):
    """Parse a markdown table and return list of (package, version, info) tuples."""
    lines = table_text.strip().split('\n')
    rows = []
    for line in lines:
        # Skip header and separator rows
        if line.startswith('|') and '---' not in line:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if len(cells) >= 3 and cells[0]:  # Skip empty header rows
                rows.append((cells[0], cells[1], cells[2]))
    return rows


def extract_quarter_data(quarter_content):
    """Extract adopt and drop tables from quarter content."""
    adopt_match = re.search(
        r'###### Adopt support for:\s*\n((?:\|.*\n)+)',
        quarter_content
    )
    drop_match = re.search(
        r'###### Can drop support for:\s*\n((?:\|.*\n)+)',
        quarter_content
    )

    adopt_items = parse_table(adopt_match.group(1)) if adopt_match else []
    drop_items = parse_table(drop_match.group(1)) if drop_match else []

    return adopt_items, drop_items


def format_email(year, quarter, adopt_items, drop_items):
    """Generate email subject and body."""
    quarter_names = {1: "Q1", 2: "Q2", 3: "Q3", 4: "Q4"}
    q_name = quarter_names[quarter]

    subject = f"PHEP 3 Reminder: {q_name} {year} Support Schedule"

    body = f"""Hello PyHC Community,

This is a quarterly reminder about the PHEP 3 Python & Upstream Package Support Policy.

"""

    if adopt_items:
        body += f"## Adopt Support For (by end of {q_name} {year})\n\n"
        body += "The following package versions should be supported by PyHC packages:\n\n"
        for package, version, info in adopt_items:
            body += f"- **{package}** {version} ({info})\n"
        body += "\n"

    if drop_items:
        body += f"## Can Drop Support For (as of {q_name} {year})\n\n"
        body += "PyHC packages may now drop support for:\n\n"
        for package, version, info in drop_items:
            body += f"- **{package}** {version} ({info})\n"
        body += "\n"

    if not adopt_items and not drop_items:
        body += "No changes to the support schedule this quarter.\n\n"

    body += """---

For the full support schedule and Gantt chart, visit:
https://heliopython.org/docs/pheps/phep-3-support-schedule/

For the complete PHEP 3 specification:
https://github.com/heliophysicsPy/standards/blob/main/pheps/phep-0003.md

Questions? Reply to this email or discuss on PyHC Slack.

Best regards,
PyHC Tech Lead
"""

    return subject, body


def main():
    script_dir = Path(__file__).parent
    schedule_path = script_dir / "schedule.md"

    year, quarter = get_current_quarter()
    print(f"Current quarter: Q{quarter} {year}")

    quarters = parse_schedule(schedule_path)

    if (year, quarter) not in quarters:
        print(f"Warning: No data found for Q{quarter} {year}")
        # Try to find the nearest future quarter
        future_quarters = [(y, q) for y, q in quarters.keys() if (y, q) >= (year, quarter)]
        if future_quarters:
            year, quarter = min(future_quarters)
            print(f"Using next available quarter: Q{quarter} {year}")
        else:
            print("No future quarters found in schedule. Using empty content.")
            subject = f"PHEP 3 Reminder: Q{quarter} {year} Support Schedule"
            body = "No schedule data available for this quarter. Please check the PHEP 3 support schedule page."
            Path(script_dir / "email_subject.txt").write_text(subject)
            Path(script_dir / "email_body.txt").write_text(body)
            return

    quarter_content = quarters[(year, quarter)]
    adopt_items, drop_items = extract_quarter_data(quarter_content)

    print(f"Found {len(adopt_items)} adopt items, {len(drop_items)} drop items")

    subject, body = format_email(year, quarter, adopt_items, drop_items)

    # Write outputs for the GitHub Action to use
    Path(script_dir / "email_subject.txt").write_text(subject)
    Path(script_dir / "email_body.txt").write_text(body)

    print(f"\nSubject: {subject}")
    print(f"\nBody preview:\n{body[:500]}...")


if __name__ == "__main__":
    main()
