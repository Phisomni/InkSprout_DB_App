# Video Link: Put Youtube public link
# Put Appsmith Repo Link 

# Team&Project Name
* Team name: Ravneet Kaur, Yuna Lee, Elsa Cederlund, Aran Dharma, Winnie Chuma
* Project name: InkSprout
* Team member: FastButNotFurious

# As you work on the project, update the README.md in the main repo folder to include 
## an overview of your project (COPIED FROM THE PHASE 1)
InkSprout is an online original writing and blogging platform that allows writing content creators to connect with their reading audiences over the web. Anyone can create an account and post writing as well as access other social media-like features, which initially can be freely accessed by any interested reader with their own account. At a certain point, content creators with a large enough following will have the opportunity to monetize their content with ads and paywalls for certain posts. Users on the site can follow each other just like they would on many social media platforms, and InkSprout itself has the option to be linked to accounts on other platforms. The site will be moderated autonomously at the lowest levels, and will have human moderators to handle specific situations. Users can additionally pay to access writing assistants that can help them improve their content and provide insights on how to better reach their audience.

## information about how to start the docker containers (see other GitHub repos for models of how to write a good README)

## any information the user needs to build/start the containers (such as adding the secrets passwords files), etc. 


<<<< we need to move things below to appsmith repo README file
On the Appsmith Repo (make sure it is public). Update the README with a description of your UI, any information the user needs to know to access it, etc. 
# UI Screens
- Reader_Post_Searcher UI Screen: The user can go over the list of content creators and genres, choose a content creator to view that creator's posts and view the details for one post by selecting the row on the table. Then, they can click 'View/Write Comemnts' button to go to Reader_Comment_Post Screen 

- Reader_Comment_Post: When the user put the post id on input box, the comments for that post will be displayed on the table. The user can add or delete comment, and the table will be updated for any addition or deletion of comments.  


can delete things below 

# MySQL + Flask Project

This repo contains a setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 
