### restaurant-site-frontend
Restaurant-site-frontend is a web application for an italian restaurant with a menu and the ability to leave a review. You can visit the site http://italian-pizza-delivery.site/index.html
#### Install the PostgreSQL database (ubuntu)
1. Update System Packages:
   - Open a terminal on your Ubuntu system.
   - Run the following command to update the system packages:
     ```
     sudo apt update
     ```

2. Install PostgreSQL:
   - Use the following command to install PostgreSQL and its dependencies:
     ```
     sudo apt install postgresql
     ```

3. Verify PostgreSQL Installation:
   - After the installation is complete, PostgreSQL service will start automatically.
   - You can check the status of the service using the following command:
     ```
     sudo systemctl status postgresql
     ```

4. Access PostgreSQL:
   - By default, PostgreSQL creates a system user called "postgres" during installation.
   - Switch to the "postgres" user using the following command:
     ```
     sudo su - postgres
     ```

5. Access PostgreSQL Shell:
   - Once you are logged in as the "postgres" user, you can access the PostgreSQL shell by running the following command:
     ```
     psql
     ```

6. Create a New User and Database (Optional):
   - If you want to create a new user and database, you can use the following commands in the PostgreSQL shell:
     - Create a new user:
       ```
       CREATE USER your_username WITH PASSWORD 'your_password';
       ```
     - Create a new database:
       ```
       CREATE DATABASE your_database_name;
       ```
     - Grant privileges to the user on the database:
       ```
       GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
       ```

7. Exit PostgreSQL Shell and Switch Back to Regular User:
   - To exit the PostgreSQL shell, type `\q` and press Enter.
   - Switch back to your regular user account using the following command:
     ```
     exit
     ```
8. Start Using PostgreSQL:
   - Now you can start using PostgreSQL on your Ubuntu system.
   - You can also connect to the PostgreSQL database using a variety of tools such as pgAdmin.


#### Preparing the project for local deployment
   - You will need the nginx.conf file to configure nginx on the remote server, you will not need it locally
1. Update System Packages:
   - Run the following command to create a project directory:
   ```
   mkdir dir_name
   ```
   ```
   cd dir_name
   ```
2. Clone the project from the repository:
   - You can also clone the [frontend](https://github.com/itsapumpkinpie/restaurant-site-frontend):
   ```
   git clone https://github.com/itsapumpkinpie/restaurant-site-backend.git
   ```
3. Within the project directory, create a Python virtual environment by typing:
     ```
     python3 -m venv venv
     ```
4. You will need to activate the virtual environment and install your project’s Python requirements:
     ```
     source venv/bin/activate
     ```
     ```
     pip install -r requirements.txt
     ```
#### Completing Project Setup
1. migrate the initial database schema to our PostgreSQL database using the management script:
     ```
     manage.py makemigrations
     ```
     ```
     manage.py migrate
     ```
2. Create an administrative user for the project:
    - You will have to select a username, provide an email address, and choose and confirm a password.
     ```
     manage.py createsuperuser
     ```
3.  Finally, you can test out your project by starting up the Django development server with this command::
    - Don't forget to insert environment variables into settings.py
     ```
     python3 manage.py runserver
     ```
