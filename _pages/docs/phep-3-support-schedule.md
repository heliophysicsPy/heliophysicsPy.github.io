---
layout: page
title: PHEP 3 Support Schedule
permalink: /docs/pheps/phep-3-support-schedule/
exclude: true
---

This page provides a visual timeline and schedule for [PHEP 3](https://github.com/heliophysicsPy/standards/blob/main/pheps/phep-0003.md), PyHC's Python and Upstream Package Support Policy (based on [SPEC 0](https://scientific-python.org/specs/spec-0000/)).

<br>

## Support Policy Summary

All PyHC packages should:
1. **Support Python versions** for at least **36 months** (3 years) after their initial release
2. **Support upstream core Scientific Python packages** for at least **24 months** (2 years) after their initial release
3. **Adopt support for new versions** within **6 months** of their release

The upstream [core Scientific Python packages](https://scientific-python.org/specs/core-projects/) are:
- `numpy`, `scipy`, `matplotlib`, `pandas`, `scikit-image`, `networkx`, `scikit-learn`, `xarray`, `ipython`, `zarr`

<br>

## Support Window Timeline

{% include mermaid_chart.html file="phep-3/chart.md" %}

## Drop and Adoption Schedule

Below is an auto-generated schedule with recommended dates for dropping support and adopting new versions. We suggest that the next release in a given quarter is considered as the one removing support for a given item.

You may want to delay the removal of support of an older Python version until your package fully works on the newly released Python, thus keeping the number of supported minor versions of Python the same for your package.

<br>

<div class="schedule-table" markdown="1">
{% include_relative phep-3/schedule.md %}
</div>

---

<br>

## Additional Information

- **Full PHEP 3 specification:** [PHEP 3 on GitHub](https://github.com/heliophysicsPy/standards/blob/main/pheps/phep-0003.md)
- **DOI:** [10.5281/zenodo.17794207](https://doi.org/10.5281/zenodo.17794207)
- **Email reminders:** Automated email reminders are sent via the PyHC mailing list quarterly and near important drop/support dates
- **Questions?** [Contact](/contact) the PyHC Tech Lead or discuss on the [PyHC's mailing list or Slack](/contact)

<br>

## For Package Maintainers

PyHC packages should:
- Clearly document their dependency version policy (see examples: [PlasmaPy](https://docs.plasmapy.org/en/stable/contributing/coding_guide.html#dependencies-and-requirements), [SpacePy](https://spacepy.github.io/dep_versions.html))
- Test against the minimum and maximum supported versions
- Avoid maximum or exact requirements (e.g., `numpy<2` or `matplotlib==3.5.3`) unless absolutely necessary
- Not require versions of any dependency older than 24 months

---

*This page is maintained by the PyHC Tech Lead. The schedule is generated using code from PHEP 3 and is updated periodically.*
