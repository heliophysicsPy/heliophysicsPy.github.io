---
layout: page
title: Adding a Project to the PyHC Project List
permalink: /docs/adding_a_project/
exclude: true
---

Described herein is the procedure for requesting to add a project to the PyHC Project List, and how the approval process works.

## Requesting to add a project

Before your project can be added to the PyHC Project List (i.e., be added to the [PyHC Project page](https://heliopython.org/projects/)), you need to do a self evaluation of the state of your
code base (based on the [PyHC project review guidelines](https://github.com/heliophysicsPy/heliophysicsPy.github.io/blob/main/_pyhc_projects/pyhc_project_grading_guidelines.md)). Once you've completed
your self evaluation, know what grades your project should be assigned for each of the six standards, and you 
are confident the results are ready to be input to the PyHC Project List, you'll need to fork the  
[PyHC website repository](https://github.com/heliophysicsPy/heliophysicsPy.github.io). You'll make all your changes in that
forked repository before creating a Pull Request (PR) to merge your repository's changes into the main PyHC website repository.

In your forked repository, navigate to `_data/projects.yml` (or `_data/projects_core.yml`, _if you know your project already resides there_). Think of `projects.yml` file as a database where you can enter in
information about your project that's called by other scripts in the repository to build the Projects page. 
In `projects.yml`, projects are listed in alphabetical order. Available inputs for your projects are as follows (where mandatory inputs are starred*, and variable names are shown in parentheses): 

* The project name (name) *
* The project's website url (url),
* A description of the project's main function (description) *,  
* The location of the project's logo (logo)
* The location of the project's documentation (docs)
* The location of the project's code base (code) *
* Who to contact for questions about the project (contact) *
* Keywords that are related to your project's functionality *
* The grade for the community standard *
* The grade for the documentation standard *
* The grade for the testing standard *
* The grade for the software maturity standard *
* The grade for the Python 3 standard *
* The grade for the license standard *

The standards grades each require two values to be entered in, the img src url and the alt text of the given grade. The img
src url creates the colored boxes denoting standards grades, while the alt text is what shows up if the colored boxes can not
be rendered on a device. If you gave a `"Requires Improvement"` grade for a standard, you'd enter in

&nbsp;&nbsp;&nbsp;&nbsp; <code>["<a href="https://img.shields.io/badge/requires%20improvement-red.svg">https://img.shields.io/badge/requires%20improvement-red.svg</a>", "Requires improvement"]</code>

Accordingly, if you gave a `"Partially met"` or a `"Good"` grade for a standard, you'd enter in

&nbsp;&nbsp;&nbsp;&nbsp; <code>["<a href="https://img.shields.io/badge/Partially%20met-orange.svg">https://img.shields.io/badge/Partially%20met-orange.svg</a>", "Partially met"]</code>

or

&nbsp;&nbsp;&nbsp;&nbsp; <code>["<a href="https://img.shields.io/badge/Good-brightgreen.svg">https://img.shields.io/badge/Good-brightgreen.svg</a>", "Good"]</code>

respectively.
 
Now, find the proper location for your project and enter in your project-specific information (You can do this in 
GitHub itself, or in an IDE if you prefer). Make sure to keep the same formatting as projects already listed in the 
yml file. An example project's inputs are shown below.


&nbsp;&nbsp;&nbsp;&nbsp;  `name: "A Really Cool Project"`<br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>url: "<a href="http://www.mycoolproject.org">http://www.mycoolproject.org</a>"</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>description: "A project that does some awesome science!"</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>logo: "<a href="https://location/of/my/project/logo/logo.png">https://location/of/my/project/logo/logo.png</a>"</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>docs: "<a href="http://docs.mycoolproject.org">http://docs.mycoolproject.org</a>"</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>code: "<a href="https://github.com/mycoolproject/mycoolprojectcode">https://github.com/mycoolproject/mycoolprojectcode</a>"</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>contact: "Fearless Leader of the Really Cool Project"</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>keywords: ["solar","general"]</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>community: ["<a href="https://img.shields.io/badge/Good-brightgreen.svg">https://img.shields.io/badge/Good-brightgreen.svg</a>", "Good"]</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>documentation: ["<a href="https://img.shields.io/badge/Good-brightgreen.svg">https://img.shields.io/badge/Good-brightgreen.svg</a>", "Good"]</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>testing: ["<a href="https://img.shields.io/badge/Good-brightgreen.svg">https://img.shields.io/badge/Good-brightgreen.svg</a>", "Good"]</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>software_maturity: ["<a href="https://img.shields.io/badge/Good-brightgreen.svg">https://img.shields.io/badge/Good-brightgreen.svg</a>", "Good"]</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>python3: ["<a href="https://img.shields.io/badge/Good-brightgreen.svg">https://img.shields.io/badge/Good-brightgreen.svg</a>", "Good"]</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;  <code>license: ["<a href="https://img.shields.io/badge/Good-brightgreen.svg">https://img.shields.io/badge/Good-brightgreen.svg</a>", "Good"]</code><br>

Once you've added your project's information to projects.yml, commit and push your changes. Then, create a new PR 
on your forked repository's GitHub page. This will create a request to merge those changes into the main PyHC 
website repository. In this PR, write a short blurb about your project, including the name, a general description of the 
project, and what grades were assigned for the PyHC standards. If any of the standards fall below the "Good" classification,
make sure to provide some remarks about why that is, and what the project's plan is for improvement. As stated in the
reviewing guidelines, at present, no projects will be rejected from the PyHC Project list. However, at the 
PyHC Spring 2020 meeting we will set a date by which projects will be kicked off if they have any "Requires improvement" grades. 
Feel free to also post about your project and the PR in the [Element chat group](https://riot.im/app/#/room/#heliopython:openastronomy.org). 
Within a week or so, a PyHC developer will review your PR request and approve it (for now, unconditionally, but after the 
PyHC Spring 2020 meeting approval is subject to the standards grades).
