# Team sauce katsudon's project for IE04
Team members:  
s1280179 Tomohito Ide  
s1282003 Angelita Gozaly

Type of software: Web application  
  
Language and frameworks:  
Backend: Python (Django)  
Frontend: HTML, CSS, JavaScript  
  
Plan for this week:   
- Work on working hours input
- Review diagrams and backlogs
  
## External Links  
UI Mockups:  
Student's login-> https://ta-report-system-ce3b81.webflow.io/  
Student's main-> https://ta-report-system-ce3b81.webflow.io/main-student/  
Student's report-> https://ta-report-system-ce3b81.webflow.io/report-student/  
Lecturer's login-> https://ta-report-system-ce3b81.webflow.io/login-lecturer/  
Lecturer's main-> https://ta-report-system-ce3b81.webflow.io/main-lecturer/  
Lecturer's report-> https://ta-report-system-ce3b81.webflow.io/report-lecturer/  

This is the initial structure for your project.
You may customize the structure to your liking, but there are a few rules that you **must** follow.

## Setting up development environment
Installing Python: [reference](https://cloudbytes.dev/snippets/upgrade-python-to-latest-version-on-ubuntu-linux)

Installing MySQL: [reference](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

Installing MySQL development libraries for Python
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

Creating database: 
* Start the local MySQL server with `sudo systemctl start mysql.service`
* Login to your root account with `mysql -u root -p`
* From the MySQL console, create a database with `CREATE DATABASE {{DB_NAME}}`
* Create a dedicated MySQL user and grant necessary privileges **optional*
```
CREATE USER '{{USERNAME}}'@'{{HOST}}' IDENTIFIED BY {{PASSWORD}};
GRANT PRIVILEGE ON {{DB_NAME}} TO '{{USERNAME}}'@'{{HOST}}';
```

Installing Pip **if necessary*
```
sudo apt-get install python3-pip
```

## Installing dependencies
Run the following command from the root directory of this repository
```
pip3 install -r requirements.txt
```

## Setting up Django
Django should already be installed after the [above section](#installing-dependencies). To confirm that it has been installed properly, run the following command
```
python3 -m django --version
```

To manage your local database credentials, create a file named `.env` in the root directory of this project and store all related variables. Refer to the format below
```
DB-NAME={{LOCAL_DB_NAME}}
DB-USER={{LOCAL_DB_USERNAME}}
DB-PASSWORD={{LOCAL_DB_PASSWORD}}
```

After setting up your database credentials, migrate all Django models into your local database by running the following command from the `src/ta_report_system` directory
```
python3 manage.py makemigrations
```

Finally, you can launch your local server with
```
python3 manage.py runserver
```

For more details, refer to [Django official documentation](https://docs.djangoproject.com/ja/4.1/intro/)

## Project structure rule
**Do not delete** the following directories.
Each should contain the corresponding documents.
* *doc* : Project documents (UML diagrams, requirements, etc.) created by the team should be kept here.
* *report* : Use the templates for the reports.
  * *weekly* : Put your weekly report slides (pptx format) here.
  * *final* : Put your final report slides (pptx format) here.
* *RFP* :sparkles:
  * *ie04_project2021_RFP_<date>.pdf* : Request for proposal for the project.
* *src* : All source code (and settings, resources) of your product should be kept here.

