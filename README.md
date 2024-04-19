# Video Link: https://drive.google.com/file/d/1WpzRNhuSYzA0zEglyKszyaLrBLwGYYAo/view

# Put Appsmith Repo Link: https://github.com/Ravneet2005/appsmith.git

# Team & Project Name
* Team members: Ravneet Kaur, Yuna Lee, Elsa Cederlund, Aran Dharma, Winnie Chuma
* Project name: InkSprout
* Team name: FastButNotFurious

# As you work on the project, update the README.md in the main repo folder to include (delete)
## Project overview (COPIED FROM THE PHASE 1)
InkSprout is an online original writing and blogging platform that allows writing content creators to connect with their reading audiences over the web. Anyone can create an account and post writing as well as access other social media-like features, which initially can be freely accessed by any interested reader with their own account. At a certain point, content creators with a large enough following will have the opportunity to monetize their content with ads and paywalls for certain posts. Users on the site can follow each other just like they would on many social media platforms, and InkSprout itself has the option to be linked to accounts on other platforms. The site will be moderated autonomously at the lowest levels, and will have human moderators to handle specific situations. Users can additionally view their followings list and be aware of their writers of interest

# WHY and HOW?
We wanted to create this type of application because we thought it would be interesting to work on something close to social media, especially instagram. We used AppSmith for the front end parts, creating the UIs for the different screens, and DataGrip to create the database. Additionally, we utilized VS Code to create the python code for our API requests used to connect AppSmith and our data to make our App possible. For the building, testing, and deployment of InkSprout, we also used docker to make sure that our database, AppSmith, and web were all running and connected.  

<<<<<<< HEAD
# How to start the docker containers (explained)
**Important** - you need Docker Desktop installed
To start the docker containers, you can either do this in the terminal or the VS Code terminal. Make sure to be in the 23f-project-boilerplate file and run the command "docker compose up -d"
Will end like this: ...... 23f-project-boilerplate % docker compose up -d  
Navigate to the README.md in under the secrets folder and follow the instructions there so that you can use the root password in the AppSmith. 
How to add password in AppSmith: Data --> + --> Database name: inkSprout --> MySQL username: root --> MySQL password: db_root_password(yours)  --> Test Configuration
=======
## any information the user needs to build/start the containers (such as adding the secrets passwords files), etc. 


<<<< we need to move things below to appsmith repo README file
On the Appsmith Repo (make sure it is public). Update the README with a description of your UI, any information the user needs to know to access it, etc. 
# UI Screens
- Reader_Post_Searcher UI Screen: The user can go over the list of content creators and genres, choose a content creator to view that creator's posts and view the details for one post by selecting the row on the table. Then, they can click 'View/Write Comemnts' button to go to Reader_Comment_Post Screen 

- Reader_Comment_Post: When the user put the post id on input box, the comments for that post will be displayed on the table. The user can add or delete comment, and the table will be updated for any addition or deletion of comments.  


can delete things below 
>>>>>>> 7972f0cec7b8af3334f57bfb6fdbabc209a5c102

# MySQL + Flask Project

This repo contains a setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
2. A Python Flask container to implement a REST API
3. A Local AppSmith Server

## How to setup and start the containers (steps)
**Important** - you need Docker Desktop installed

1. Clone this repository.  
2. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
3. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
4. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
5. Build the images with `docker compose build`
6. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 



