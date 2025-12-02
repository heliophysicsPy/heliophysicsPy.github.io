---
layout: post
title: "Announcing PHEP 3"
author: sapols
---

<img src="/../img/page_images/phep3-gantt.jpg" alt="PHEP 3 Support Window" style="display: block; margin-left: auto; margin-right: auto; width: 60%">

PyHC has formally adopted **[PHEP 3: PyHC Python & Upstream Package Support Policy](https://github.com/heliophysicsPy/standards/blob/main/pheps/phep-0003.md)**! This new PHEP establishes a unified, time-based approach to dependency support across the PyHC ecosystem, bringing our community into alignment with the broader Scientific Python ecosystem.

PHEP 3 recommends that all PyHC packages adopt the following support policy, based on [SPEC 0](https://scientific-python.org/specs/spec-0000/):

- **Support Python versions for 36 months** (3 years) after their initial release
- **Support core Scientific Python packages for 24 months** (2 years) after their initial release
- **Adopt new versions within 6 months** of their release

This policy applies to Python itself and to the upstream [core Scientific Python packages](https://scientific-python.org/specs/core-projects/): NumPy, SciPy, Matplotlib, pandas, scikit-image, NetworkX, scikit-learn, xarray, IPython, and Zarr.

PHEP 3 replaces the previous PyHC standard #11, which simply mandated Python 3 support. This new standard provides clear, predictable timelines for both adopting new dependency versions and dropping support for older ones—giving package maintainers and users alike a reliable roadmap for dependency management.

To learn more, read **[the full PHEP 3 document](https://github.com/heliophysicsPy/standards/blob/main/pheps/phep-0003.md)**. We will also maintain a [PHEP 3 Support Schedule page](/docs/pheps/phep-3-support-schedule/) with a graphical timeline and quarterly reminders to help package maintainers stay on track. Questions or feedback? Join the discussion on [PyHC's mailing list or Slack](/contact)!
