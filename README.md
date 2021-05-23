<p align="center">

  <h1 align="center">ClinifyForest</h1>

  <p align="center">
    Clinify Exclusive Forest App!
    <br />
    <a href="https://github.com/tiluckdave/ClinifyForest"><strong>Explore the code »</strong></a>
    <br />
    <br />
    &nbsp;&nbsp;<a href="https://clinifyforest.herokuapp.com/">Visit the site</a>&nbsp;&nbsp;
    ·
    &nbsp;&nbsp;<a href="https://github.com/tiluckdave/ClinifyForest/issues">Report Bug</a>&nbsp;&nbsp;
    ·
    &nbsp;&nbsp;<a href="https://github.com/tiluckdave/ClinifyForest/issues">Request Feature</a>&nbsp;&nbsp;
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Clinify Forest is a pomodoro app made for Clinify Squad Discord Server.

### Built With

Major Frameworks used in the development and Production of this web app is as follows
* [Bootstrap](https://getbootstrap.com)
* [Django](https://www.djangoproject.com/)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)


<!-- GETTING STARTED -->
## Getting Started

Setting up the project locally maybe headache for the first time but believe me it is very easy.

### Prerequisites

Prequisites
* Python
  ```sh
  Python version 3.9.2 is used in this project
  ```
* Django installed globally
  ```sh
  pip install django -g
  ```
* Postgres
  ```
  Download and Install postgres from the link below
  ```
  [PostGres](https://www.postgresql.org/download/windows/)
* Virtualenv
  ```sh
  pip install virtualenv
  ```
* You should compulsorily become a member of Clinify Squad Discord Server link ->
  [Clinify Squad](https://clinify.in)
 
### Installation

1. Create a Virtual enviornment
   ```sh
   python -m venv csenv
   ```
   ```sh
   source ./csenv/Scripts/activate
   ```
3. Clone the repo
   ```sh
   git clone https://github.com/tiluckdave/ClinifyForest.git
   ```
3. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Setup the database
   1. Search and open psql from windows search
   2. create and connect to localhost:5432
   3. setup new password for postgres
   4. run below command
   ```
   CREATE DATABASE clinifyforest;
   ```
5. Creating a Discord Application
   * visit [Discord Developers Portal](https://discord.com/developers/applications)
   * Login if you are not
   * click on New application
   * Name your application whatever you want
   * headover to `OAuth2` section and click on `Add Ridirect`
   * Add this url `http://127.0.0.1:8000/login/redirect`
   * Click on `Save Changes`
   * Now under `OAuth2 URL Generator`
   * Select redirect Url as `http://127.0.0.1:8000/login/redirect`
   * Under scopes select `identify` and `guilds`
   * A new url will be generated at the bottom Copy it!
   
6. Enviornment Variables
   * In the root folder where `manage.py` file lies create a new `.env` file
   * Paste the below text to `.env` file
   ```
   SECRET_KEY=secretkey
   DBENGINE=django.db.backends.postgresql
   DBNAME=clinifyforest
   DBUSER=postgres
   DBPASSWORD=<yourpassword>
   DBHOST=localhost
   DBPORT=5432
   OAUTHURL=<your-oauth-url>
   REDIRECT_URI=http://127.0.0.1:8000/login/redirect
   CLINIFY_SERVER_ID=740589508365385839
   MY_DISCORD_CLIENT_ID=<your-discord-client-id>
   MY_DISCORD_CLIENT_SECRET=<your-discord-client-secret>
   ```
   * replace `<yourpassword>` with your postgres password which you just set in step 4
   * replace `<your-oauth-url>` with the oauthurl you copied at last in the step 5
   * replace `<your-discord-client-id>` with your discord developers client id
   * replace `<your-discord-client-secret>` with your discord developers client secret
7. Create local settings
   * Open the folder in any of the code editor
   * Head over to `ClinifyForest` Folder
   * Create a new file called `local_settings.py`
   * paste this code in the file
   ```
   import os
   from .settings import BASE_DIR
   
   DEBUG = True
   TEMPLATE_DEBUG = True
   ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']
   
   TZC = 0
   ```
   * save `local_settings.py`
9. Make migrations
   ```sh
   python manage.py makemigrations
   ```
   ```sh
   python manage.py sqlmigrate login 0001
   python manage.py sqlmigrate main 0001
   python manage.py sqlmigrate search 0001
   ```
   ```sh
   python manage.py migrate
   ```
10. Run the server
    ```sh
    python manage.py runserver
    ```
    And You are good to go
    Now visit [localhost:8000](http://127.0.0.1:8000)
    
11. Create Super User
    ```sh
    python manage.py createsuperuser
    ```
   


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact

Your Name - [@tiluckdave](https://twitter.com/tiluckdave) - davetilak003@gmail.com

Discord Tag - @tiluckdave#4120

Project Link: [https://github.com/tiluckdave/ClinifyForest](https://github.com/tiluckdave/ClinifyForest)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Clinify](https://clinify.in)
