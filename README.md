# SWT2 2016/17 - Introductory Exercise

We prepared an application skeleton for you that has a failing test case.

To pass the exercise, follow these steps:

## 1) Fork this repository.

* You need to be logged-in with your Github account.
* Click the "Fork" button in the upper right. 

![fork](https://cloud.githubusercontent.com/assets/1652117/19190800/ce8e6a42-8c9f-11e6-8047-60a238fcd200.png)
* In your [repository's settings](/../../settings), enable issue tracking.

![issues](https://cloud.githubusercontent.com/assets/1652117/19190926/65ee376e-8ca0-11e6-8755-5e67eaf37cab.png)

## 2) Set-up Travis CI for your fork

* Log-in to [Travis CI](http://travis-ci.org) and
* Enable automatic builds for your exercise repository.

## 3) Setup development environment

* Clone the repository to your local machine

### Option 1: Setup locally
* Change into the newly created directoy
* Inside the directory, check the used Ruby version using `ruby --version`. It should be `2.2.2`. Other Ruby versions might work, but this is the one that was tested.
* If the correct Ruby version is not used, install a ruby version manager, for example [rbenv](https://github.com/rbenv/rbenv) using the instructions for [rbenv installation](https://github.com/rbenv/rbenv#basic-github-checkout) and [ruby-build installation](https://github.com/rbenv/ruby-build#installing-as-an-rbenv-plugin-recommended).
  * WARNING: If you already have the Ruby version manager [RVM](https://rvm.io/) installed, please use that or uninstall it prior to rbenv installation, as the two version managers are incompatible.
* Install Ruby version 2.2.2 with `rbenv install 2.2.2`
* The `.ruby_version` file in the repository instructs the ruby version manager to use the correct version.

### Option 2: Use a VM
* Install [Virtualbox](https://www.virtualbox.org/manual/ch02.html) (the VM provider) and [Vagrant](https://www.vagrantup.com/docs/installation/) (to manage VMs) for your platform.
* Download the prepared VM image and install the dependencies:

```
vagrant up # download the image and start the VM
vagrant ssh # connect via ssh
cd hpi-swt2
bundle install # install dependencies
exit # restarting the session for changes to take effect
```
* In order to start the development server:

```
vagrant ssh #connect with VM
cd hpi-swt2
rails s -b 0 #starting rails server, the -b part is necessary since the app is running in a VM and would otherwise drop the requests coming from the host OS
```

* Edits to files in the local folder will be mirrored into the VM's `hpi-swt2` folder as the folders are synced.

## 4) Dive into the code

* Run `bundle install` to install the dependencies of the project (they are stored in the `Gemfile`)
* Run `rspec` to run the tests ([RSpec](http://rspec.info/) is a test framework for Ruby)
* Try to get the failing test green.

## 5) Commit and push

* When you are done, push your changes.
* Travis CI will now try to build your project.

## 6) Check your inbox

* You will be notified of problems via Github issues.
* While you wait, see if your code can use some refactorings, continue reading the tutorial, or plan the next steps.

## 7) For each ticket

* Write a test that documents the missing or failing behavior.
  * Unit tests are preferred.
* Commit the failing test and reference the issue.
  * The commit message could be `Failing test for #<ISSUE NUMBER>`.
  * There is no need to push the failing commit.
* Fix the issue and commit all changes.
  * The commit message could be `<CHANGED THE THING>. Closes #<ISSUE NUMBER>`.

## 8) Repeat steps 5 to 7 until the exercise is complete.

Tips:

* This exercise is designed to be solved while reading the official [Rails tutorial](http://guides.rubyonrails.org/getting_started.html)
* run `rspec spec/<path_to_spec>.rb` to only run one set of specs
* have a look at `/spec/factories` to get 'inspiration' for your data model
* Besides simple scaffolds, [associations](http://guides.rubyonrails.org/association_basics.html) and [validations](http://guides.rubyonrails.org/active_record_validations.html) are needed ...
* occasionally start up the server (`rails s`) and have a look at the app in your browser (`http://localhost:3000`)
* Look at the Mockup: https://gomockingbird.com/mockingbird/index.html?project=v890g6l#v890g6l/OQMURm
* Make sure that all local changes are committed (`git status`) and pushed to the upstream repository (i.e., the one on GitHub) before the deadline

