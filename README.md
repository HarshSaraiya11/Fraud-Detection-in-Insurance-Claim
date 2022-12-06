# Fraud-Detection-in-Insurance-Claim

Install MySQL for windows from this link

https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.31.0.msi

keep MySQL service at default port while installing.

Mysql@localhost:3306

User: root

Password: root

Create a python virtual environment in a separate folder.

Install python modules from requirements.txt into the virtual env.

Run the following command -
```
pip instal -r requirements.txt
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
Open command prompt or powershell and go to your project directory.

Make sure you're in insurance directory containing manage.py file.

Run the following command - (Make sure you're using your virtual env python interpreter)
```
python manage.py runserver
```
