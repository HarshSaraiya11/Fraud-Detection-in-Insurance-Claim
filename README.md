# Fraud-Detection-in-Insurance-Claim

Install MySQL for windows from this link

https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.31.0.msi

keep MySQL service at default port while installing.

Mysql@localhost:3306

User: root

Password: root

Create a python virtual environment in a separate folder.
```
python -m venv virtualenv
```

This will create a virtual enviornment named virtualenv in your project folder.

To activate this virtual enviornment, go into virtualenv folder and then Scripts folder,
```
cd virtualenv/Scripts
```

And Run,
```
.\activate
```
This will activate the virtualenv.


Install python modules from requirements.txt into the virtualenv.

Run the following command ( go back to the project directory where requirements.txt file is there )-
```
pip install -r requirements.txt
```

Ensure that the Django settings.py file has correct database configuration. i.e.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ananta_insurance',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
```

Create a schema (database) named ananta_insurane inside the root user of MySql.
You can create this schema using MySql Workbench or by using MySQL Command Line Client.

Type the following in MySQL CLI and close the CLI after query execution,

```
create database ananta_insurance;
```
Open command prompt or powershell and go to your project directory.

Make sure you're in insurance directory containing manage.py file.

Run the following command,
```
python manage.py makemigrations
```
```
python manage.py migrate
```

Then create a Django superuser by entering following command.
```
python manage.py createsuperuser
```
Enter your username password and press y. This username and password will be your admin username and password.

Then,
Run the following commands to load the data into database,
```
python manage.py loaddata auth_data.json
```
```
python manage.py loaddata data.json
```

Run the following command - (Make sure you're using your virtualenv python interpreter)
```
python manage.py runserver
```

To view the admin panel,

go to http://127.0.0.1:8000/admin

And enter the username and password entered while creating superuser.
