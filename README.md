# Live website
This code base is for the website:

[https://heliopython.org](https://heliopython.org)

The website is based on Jekyll, which automatically builds changes on GitHub.
You don't have to run Jekyll yourself to make changes.

## Add software package

1. Fork [this repo](https://github.com/scivision/heliophysicsPy.github.io) on GitHub.
2. make your changes in [_data/projects.yml](_data/projects.yml)
3. Be sure to read the [taxonomy](_data/taxonomy.yml) to properly add keywords
3. make a Pull Request on GitHub.

## Add gallery example

To add a gallery example see the [gallery repository](https://github.com/heliophysicsPy/gallery).

## [optional] Jekyll

Jekyll can be setup on Linux / Windows Subsystem for Linux for optional previewing of the website on your computer by:

1. install 
  ```sh
  apt install ruby-dev libssl-dev
   
  gem update --system
  ```
2. be sure Gems are installed to home directory, NOT system (no sudo) by adding to ~/.bashrc:
   ```sh
   # Install Ruby Gems to ~/gems
   export GEM_HOME=$HOME/gems
   export PATH=$HOME/gems/bin:$PATH
   ```
3. install Gem bundler (without sudo):
   ```sh
   gem install jekyll bundler
   ```
4. from the top-level repo directory:
   ```sh
   bundle install   # one time

   bundle exec jekyll serve
   ```
   in several seconds the website is viewable at http://localhost:4000

### [Read the tutorial!](https://taniarascia.com/make-a-static-website-with-jekyll)

- Learn about static site generators
- Install Ruby and Jekyll
- Create a custom website running on Jekyll and Sass
- Deploy a Jekyll site to GitHub pages

### License

The code is open source and available under the [MIT License](LICENSE.md).
