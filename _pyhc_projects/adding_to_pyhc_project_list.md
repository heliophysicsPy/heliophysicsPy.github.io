# Adding a Project to the PyHC Project List

Described herein is the procedure for requesting to add a project to the PyHC Project List, and how the approval process works.

## Requesting to add a project

Before your project can be added to the PyHC Project List, you first need to do a self evaluation of the state of your
code base (based on the [project review guidelines](https://github.com/heliophysicsPy/heliophysicsPy.github.io/blob/master/_pyhc_projects/pyhc_project_grading_guidelines.md)). Once you've completed
your self evaluation, know what grades your project should be assigned for each of the six standards, and you 
are confident the results are ready to be input to the PyHC Project List, you'll need to fork the  
[PyHC website repository](https://github.com/heliophysicsPy/heliophysicsPy.github.io). You'll make all your changes in that
repository before creating a Pull Request (PR) to merge your repository's changes into the main PyHC website repository.

In your forked repository, navigate to _data/projects.yml. Think of projects.yml file as a database where you can enter in
information about your project that's called by other scripts in the repository to build the Projects page. 
In projects.yml, projects are listed in alphabetical order. Available inputs for your projects are as follows (where mandatory
inputs are starred, and variable names are shown in parentheses): 
* The project name (name) &ast;
* The project's website url (url),
* A description of the project's main function (description) &ast;,  
* The location of the project's logo (logo)
* The location of the project's documentation (docs)
* The location of the project's code base (code) &ast;
* Who to contact for questions about the project (contact) &ast;
* Keywords that are related to your project's functionality &ast;
* The grade for the community standard &ast;
* The grade for the documentation standard &ast;
* The grade for the testing standard &ast;
* The grade for the software maturity standard &ast;
* The grade for the Python 3 standard &ast;
* The grade for the license standard &ast;

The standards grades each require two values to be entered in, the img src url and the alt text of the given grade. The img
src url creates the colored boxes denoting standards grades, while the alt text is what shows up if the colored boxes can not
be rendered on a device. If you gave a "Requires Improvement" grade for a standard, you'd enter in
> ["https://img.shields.io/badge/Requires%20improvement-red.svg", "Requires improvement""].

Accordingly, if you gave a "Partially met" or a "Good" grade for a standard, you'd enter in
> ["https://img.shields.io/badge/Partially%20met-orange.svg", "Paritally met"]

or
  
> ["https://img.shields.io/badge/Good-brightgreen.svg", "Good"],

respectively.
 
Now, find the proper location for your project and enter in your project-specific information (You can do this in 
GitHub itself, or in an IDE if you prefer). Make sure to keep the same formatting as projects already listed in the 
yml file. An example project's inputs are shown below.

> name: "A Really Cool Project"  
  url: "http://www.mycoolproject.org"  
  description: "A project that does some awesome science!"  
  logo: "https://location/of/my/project/logo/logo.png"  
  docs: "http://docs.mycoolproject.org"  
  code: "https://github.com/mycoolproject/mycoolprojectcode"  
  contact: "Fearless Leader of the Really Cool Project"  
  keywords: ["solar","general"]  
  community: ["https://img.shields.io/badge/Good-brightgreen.svg", "Good"]  
  documentation: ["https://img.shields.io/badge/Good-brightgreen.svg", "Good"]   
  testing: ["https://img.shields.io/badge/Good-brightgreen.svg", "Good"]   
  software_maturity: ["https://img.shields.io/badge/Good-brightgreen.svg", "Good"]  
  python3: ["https://img.shields.io/badge/Good-brightgreen.svg", "Good"]   
  license: ["https://img.shields.io/badge/Good-brightgreen.svg", "Good"]   

Once you've added your project's information to projects.yml, commit and push your changes. Then, create a new PR 
on your forked repository's GitHub page. This will create a request to merge those changes into the main PyHC 
website repository. In this PR, write a short blurb about your project, including the name, a general description of the 
project, and what grades were assigned for the PyHC standards. If any of the standards fall below the "Good" classification,
make sure to provide some remarks about why that is, and what the project's plan is for improvement. As stated in the
reviewing guidelines, at present, no projects will be rejected from the PyHC Project list. However, at the 
PyHC Spring 2020 meeting we will set a date by which projects will be kicked off if they have any "Requires improvement" grades. 
Feel free to also post about your project and the PR in the [Riot.im chat group](https://riot.im/app/#/room/#heliopython:openastronomy.org). 
Within a week or so, a PyHC developer will review your PR request and approve it (for now, unconditionally, but after the 
PyHC Spring 2020 meeting approval is subject to the standards grades).
