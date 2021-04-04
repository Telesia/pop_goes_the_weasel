# Pop Goes The Weasel
## Code Institute Milestone Project 3: Python and Data Centric Development

Welcome Telesia,
=======
Pop Goes The Weasel is a dictionary style website for users who want to learn more about cockney words, phrases and the art of rhyming slang.

A link to the website can be found [here]()

### UX

#### Strategy
Pop Goes The Weasel is a fun and informative online dictionary. It is for users who may want to understand more about the language of cockney rhyming slang and/or
contribute to the vernacular of terms. It is an interactive application where users can register then subsequently login to their account in order to add any further cockney words and phrases. The application is aimed at a wide range of users (10 - 100!) and because of that I am keeping the overall look contempory yet professional. The users will want to access information regarding cockney words and phrases as well as contribute to the dictionary easily. 

As a first time user I want to:

* be able to read cockney words and rhyming slang phrases 
* be able to register for an account
* be able to add a word or phrase to the dictionary
* be able to edit a word or phrases in the dictionary that I have added
* be able to delete a word or phrase in the dictionary that I have added
* be able to instinctively navigate the website to find the information required efficiently.
* enjoy the experience of entering a website that is informative and understand the main aims of the site
* be able to contact the website for any further information about cockney rhyming slang or incase my account is malfunctioning.

As a registered user I want to:

* be able to log in and log out of my account
* be able to read cockney words and rhyming slang phrases 
* be able to add a word or phrase to the dictionary
* be able to edit a word or phrases in the dictionary that I have added
* be able to delete a word or phrase in the dictionary that I have added
* be able to instinctively navigate the website to find the information required efficiently.
* be able to contact the website for any further information about cockney rhyming slang or incase my account is malfunctioning.

As a site owner I want to:

* make the purpose of the site clear
* create an informative and interesting experience for users, whether registered or not
* present some cockney words/phrases in the dictionary but allow scope for more to be added
* allow registered users to create, read, edit and delete the dictionary
* allow users to read the dictionary

#### Scope
After analysis of the user stories, I have decided that I cannot implement all user's needs at this time so I have decided on the below features to be my initial minimum scope:

* Register account form
* Log in form
* Log out capability
* Add words to dictionary
* Edit words in dictionary 
* Delete words from dictionary
* Responsive design
* Contact form 

#### Structure

The application will be structured with traditional multiple pages from a navbar. 
Site structure will include the following pages.

For a new user:
* Home
* Register
* Sign In
* Contact 

For a registered user:
* Home 
* Profile
* Add To dictionary
* Sign Out

The project will also use a database served by the cloud platform MongoDB.

I set up the database using the following steps from CI tutorials:

* Created an account with MongoDB and selected the create a shared cluster option.
* Selected AWS as my cloud provider and my closest region.
* Then I selected The M0 cluster tier, named the cluster and created.
* Once the cluster was created I clicked on database access and added in the database user details.
* Then I set the database user privileges to read and write to the database.
* In security menu, network access, add IP address and access from anywhere.
* Clicked on the connect button then the connect your application button.
* Added the details into my environmental variable within env.py file to connect.
* Then within my cluster, I clicked collections, create database and named it 'Pop Goes The Weasel'.
* Within the database I created my 2 collections for the project - users and cockney_dictionary

##### Database schema 

My db consists of two collections: 

1. cockney_dictionary

    * Here is an example of a record from the collection:

            _id:6061e9439c533093c991e8ae

            word:"barnet"

            meaning:"hair"

            added_by:"ricky"

2. users 

    * Here is an example of a record from the collection:

            _id: 605c9a6865d28b2c50090bc2

            username: "andrew"
            
            password: "pbkdf2:sha256:150000$MaQNn5Lf$6bba13503c555e28773bcf1f25ac5d568c5080d3..."





#### Skeleton
I designed wireframes for mobile, tablet and desktop using Balsamiq.
They are viewable in PDF using the following link:

[Wireframes](static/wireframes) 

#### Surface
##### Colours

I wanted the colours to reflect the UK flag, but in a more subtle and modern palette. This choice is to represent the cockneys of London, UK and their dialect.

0E3746 - Navy Blue

EAE8DC - Oatmeal

F4F2EC - Off White

BE2623 - Warm Red

![colour palette](static/images/colour_palette_PGTW.jpeg "Colour Palette")

##### Typography

I have used two Google Fonts: Roboto, Roboto Slab for headings and sans-serif as a back up font.

### Features

* Responsive on all devices with a mobile-first design using the Materialize framework

* An easy to use navigation bar located at the top of every page with a collapsible side navigation menu on mobile devices

* A home page with an about section that explains the purpose of the site

* A dictionary page with a materialize collapsible component, search functionality and a sort button

* Add, Edit and Delete functionality

* Register, Sign In and Sign Out functionality

* A profile page that displays words the user has added to the dictionary

* A contact page with an easy to use form connected to EmailJS to allow anyone to contact the site owner

* A footer located on every page 

#### Features Left to Implement:
* A search bar feature to look up words in the dictionary

### Technologies Used

* HTML5

* CSS3 

* Javascript

* Python

* Materialize

A modern framework used to implement css and layout features.

* MongoDB Atlas 

The cloud based service used as the database for the project.

* Flask

Uses Flask as a microframework to create the application.

* Heroku

A cloud platform used to deploy the project. 

* GitHub

The project uses GitHub to store its code.

* Gitpod

The project uses Gitpod as the IDE.

* Git

Used within Gitpod as the version control system.

* Google Developer Tools

Used within Google Chrome to inspect pages to help solve any bugs and view responsive design features.

* Balsamiq

The project uses Balsamiq to create wireframes.

* EmailJS

Used to integrate the functionality of the contact form to connect to an appropriate email address.



### Testing

Please refer to seperate document found [here](TESTING.md)

* Noticed bug with mobile view that navbar <a></a> link for brand-logo didn't display fully so adjusted design to use an icon which mixed up the media and worked better visually 
for responsiveness.

  if request == "POST":
        word = {
            "word": request.form.get("word"),
            "meaning": request.form.get("meaning"),
            "added_by": session["user"]
            }
        mongo.db.cockney_dictionary.insert_one(word)


* bug in display of dictionary showing first line the wrong way round for word and meaning. The html h5 tag I had added had made it display incorrectly.



### Deployment

The repository for the project is held on GitHub and was created by Sarah Telesia. 

#### Steps to create project using Gitpod and GitHub:

* Navigate to Code Institute main template on github (https://github.com/Code-Institute-Org/gitpod-full-template)
* Click on 'Use this template' and create personalised Repository Name
* Click 'Create repository from template'
* Click on 'Gitpod' button in new respository, to open in IDE

#### Steps on how to clone the repository from GitHub

I have learned and taken the information for the below clone steps from https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

There are two options:

Clone using GitHub Desktop

Open GitHub website and navigate to Quartet-Militaire repository on Sarah Telesia's GitHub at https://github.com/Telesia/Lockdown-Cocktail-V2
Above the list of files, click on Code button
Scroll down to read 'Open with GitHub Desktop' and then click
This will open GitHub Desktop (If this is your first time using GitHub Desktop follow the software download procedure)
A pop up will ask you where you wish to clone the repository to on your local computer and then press clone
You can now access the repository files in your chosen IDE

Clone using Git

Open GitHub website and navigate to Quartet-Militaire repository on Sarah Telesia's GitHub at https://github.com/Telesia/Lockdown-Cocktail-V2
Above the list of files, click on Code button
Click on the web URL viewable and copy
Open the terminal
Change the current working directory to the location where you want the cloned directory
Type git clone, and then paste the URL you copied earlier
Press Enter to create your local clone.6.
You can now access the repository files in your chosen IDE

#### Deploy the Project to Heroku

The steps are show in the CI tutorial 'Putting the Basics In Place' which I followed.
Here is a summary of steps:



### Credits

Colour palette from www.digitalsynopsis.com 

Credit to CI (Code Institute) lessons on EmailJS integration for the contact.js function.

Credit to CI (Code Institute) lessons on the Task Manager Application, which I have based my project around.

Credit to: Ed B_lead for code logic and how to wire up data-targets/Ids taken from Code Institute Slack channel.

Thank to my mentor Spencer Barriball















# Testing 

* Noticed bug with mobile view that navbar <a></a> link for brand-logo didn't display fully so adjusted design to use an icon which mixed up the media and worked better visually 
for responsiveness.

  if request == "POST":
        word = {
            "word": request.form.get("word"),
            "meaning": request.form.get("meaning"),
            "added_by": session["user"]
            }
        mongo.db.cockney_dictionary.insert_one(word)


* bug in display of dictionary showing first line the wrong way round for word and meaning. The html h5 tag I had added had made it display incorrectly.

