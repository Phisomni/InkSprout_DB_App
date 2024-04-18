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

# Reader_Post_Searcher (satisfy user story 1.1)
- List of content creator: by showing a list of content creators and genre information related with genreID, the user can easily figure out which content creator's posts they want to explore.
- Find post by content creator: by submitting userID of a content creator, the user can view the list of posts that the content creator created.
- Chosen post: The title, content, number of views, and other information related to specific content by clicking a certain row of a table which is generated on 'Find post by content creator' section.
- View / Write Comments: when click this button, the page will transition to Reader_Comment_Post Screen

# Reader_Comment_Post (satisfy user story 1.3)
- Input Post ID: when the user input the post id, the comments on that post will be displayed on the table below.
- Add Comment: when put comment and post informaiton on form and click submit, the new comment will be added to the comment table above.
- Delete Comment: when put the comment ID to delete and clikc submit, the comment will be deleted and disappear from the comment table above. 

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
