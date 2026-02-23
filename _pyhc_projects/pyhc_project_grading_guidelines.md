# PyHC Project Review Guidelines

This document outlines the criteria upon which projects are reviewed for submission to the PyHC Project
list (i.e., submission to the [PyHC Project page](https://heliopython.org/projects/)). Its intended audience is the project owner, or the main project developer who is submitting a project review/adding a project to the PyHC Project list.
For now, PyHC intends to stick with this "self review" process. In the future, a PyHC developer may also review a
project if needed.

The reviewer's job is to give a grade of "Requires improvement" (red), "Partially met" (yellow), or "Good" (green)
with respect to how well their project stacks up to each of the review standards listed in the table below.
If a project's grade for a standard falls below the "Good" classification, the reviewer should provide some remarks about
why that is, and what the project's plan is for improvement.

At present, no projects will be rejected from the PyHC Project list. However, at the PyHC Spring 2020 meeting we will
set a date by which projects will be kicked off if they have any "Requires improvement" grades.
We will also set up a timeline for which projects are 1) informed they are in danger of being kicked off and 2) given
time to fix the problematic categories.

A more detailed description of a review's grading colors is shown below.

<table>
<tr>
<td><img src="https://img.shields.io/badge/Requires%20improvement-red.svg" alt="Requires improvement"></td>
<td>At present, we won't reject any projects that have a standard with this grade, however, projects are strongly encouraged to improve. Note that this is going to change in the latter part of 2020.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Partially%20met-orange.svg" alt="Partially met"></td>
<td>This indicates that a project only partially meets a standard. It is not cause for a project to be removed from the PyHC Project list, however, projects are still encouraged to continue improving until they reach a "Good" rating for that standard.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Good-brightgreen.svg" alt="Good"></td>
<td>This indicates that a project meets all the requirements of a standard.</td>
</tr>
</table>

The six standards against which we assess a project are the following:

* Community
* Documentation
* Testing
* Software Maturity
* PHEP 3 (Python & Upstream Package Support)
* License

An explanation of each standard (and sub-standards therein) are defined in the [PyHC Community Standards](https://github.com/heliophysicsPy/standards/blob/main/standards.md)

### Community

In order to conform to the PyHC Community standard, packages need to successfully meet these sub-standards:
* Open Development
* Duplication
* Collaboration
* Code of Conduct

See the [PyHC Community Standards, points 2, 12, 13, and 15](https://github.com/heliophysicsPy/standards/blob/main/standards.md)

<table>
<tr>
<td width=200><img src="https://img.shields.io/badge/Requires%20improvement-red.svg" alt="Requires improvement"></td>
<td>Project doesn't employ any of the Community sub-standards.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Partially%20met-orange.svg" alt="Partially met"></td>
<td>Project partially meets the Community sub-standards.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Good-brightgreen.svg" alt="Good"></td>
<td>Every sub-standard mentioned above is implemented, without any major weaknesses.</td>
</tr>
</table>

### Documentation

Basically, make sure that the project has documentation, and if so, take note of the state of said documentation.
See the [PyHC Standards, point 8](https://github.com/heliophysicsPy/standards/blob/main/standards.md) for the specifics on what should be included in documentation.

<table>
<tr>
<td width=200><img src="https://img.shields.io/badge/Requires%20improvement-red.svg" alt="Requires improvement"></td>
<td>Essentially, the project contains little to no documentation. If documentation does exist, it is incomplete, or incorrect in many places.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Partially%20met-orange.svg" alt="Partially met"></td>
<td>Documentation exists, and is in decent shape (covers most of what is mentioned in the PyHC Standards). Documentation may need updating in places.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Good-brightgreen.svg" alt="Good"></td>
<td>The project's documentation covers every point mentioned in the PyHC Standards.</td>
</tr>
</table>

### Testing

Code must have unit tests to ensure its functionality. Unit tests should cover all individual components of code, as well as interaction between different components in the code. Automated testing, and system and acceptance testing is encouraged. See [PyHC Standards, point 9](https://github.com/heliophysicsPy/standards/blob/main/standards.md) for more specifics on testing expectations.

<table>
<tr>
<td width=200><img src="https://img.shields.io/badge/Requires%20improvement-red.svg" alt="Requires improvement"></td>
<td>No unit tests present, or few tests present, which are very basic in nature and don't cover a majority of the project's code base. Little to no test coverage, or no measure of test coverage at all. Other suggested testing is not implemented.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Partially%20met-orange.svg" alt="Partially met"></td>
<td>A good amount of unit tests exist, but they don't cover all of the project's code base. Test coverage is close to the desired limit, but might be a little under. Automatic testing, and system/acceptance testing might be implemented. </td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Good-brightgreen.svg" alt="Good"></td>
<td>All points in the PyHC standards document for testing are covered, with very little to improve.</td>
</tr>
</table>

### Software Maturity

The Software Maturity standard contains seven sub-standards:
* Packaging (e.g. pip, conda)
* Releases
* OS Support
* Version Control
* Coding Style
* Dependencies
* Binaries

See the [PyHC Community Standards, points 1, 3, 4, 6, 7, 10, and 14](https://github.com/heliophysicsPy/standards/blob/main/standards.md)

<table>
<tr>
<td width=200><img src="https://img.shields.io/badge/Requires%20improvement-red.svg" alt="Requires improvement"></td>
<td>Few, or none, of the software maturity standards are implemented.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Partially%20met-orange.svg" alt="Partially Met"></td>
<td>Most of the software maturity standards are implemented, but a couple still require inclusion.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Good-brightgreen.svg" alt="Green"></td>
<td>All of the software maturity standards are implemented, with little to no improvements to be made.</td>
</tr>
</table>

### PHEP 3 (Python & Upstream Package Support)

This deals with a project's support for Python versions and upstream Scientific Python packages per [PHEP 3](https://doi.org/10.5281/zenodo.17794207). See the [PyHC Community Standards, point 11](https://github.com/heliophysicsPy/standards/blob/main/standards.md). To make compliance easy to check, PyHC provides a [PHEP 3 Compliance Checker GitHub Action](https://github.com/heliophysicsPy/pyhc-actions).

<table>
<tr>
<td><img src="https://img.shields.io/badge/Requires%20improvement-red.svg" alt="Requires improvement"></td>
<td>Package does not support Python versions or upstream packages within the required timeframes, with no plan to update.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Partially%20met-orange.svg" alt="Partially met"></td>
<td>Package supports most required Python versions and upstream packages, but may be missing support for some recent releases or still depends on versions older than allowed.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Green-brightgreen.svg" alt="Green"></td>
<td>Package supports all Python versions released within the last 36 months, upstream packages released within the last 24 months, and adopts new versions within 6 months of release.</td>
</tr>
</table>

### License

Projects need to have permissive licenses for open source scientific software (see specific recommendations in the [PyHC standards, point 5](https://github.com/heliophysicsPy/standards/blob/main/standards.md).

<table>
<tr>
<td width=200><img src="https://img.shields.io/badge/Requires%20improvement-red.svg" alt="Requires improvement"></td>
<td>Project does not have a license.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Partially%20met-orange.svg" alt="Partially met"></td>
<td>Project has a license, but it does not conform with open source scientific software.</td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Good-brightgreen.svg" alt="Green"></td>
<td>Project has a permissive license for open source scientific software.</td>
</tr>
</table>
