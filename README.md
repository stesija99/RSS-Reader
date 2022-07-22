# PROJECT TITLE:
Rss Reader with Python3 Django

# DESCRIPTION:
The project is used to download RSS links from the 24sata portal and display articles on the interface
Project is made with Python 3.7.5 and Django 3.2.14 versions

# HOW TO INSTALL PYTHON ENVIRONMENT:
install virtualenv  - sudo apt-get install virtualenv
install Python environment - virtualenv -p python3.7 pyenv (pyenv is personal choice of python environment name) 
'requirements.txt' file is added so its neccessary to install all packages and libraries from file to be able to start app - pip install -r requirements.txt

# HOW TO START APP:
It is necessary to be positioned within rssreader directory so you can se 'manage.py' file
1. python manage.py makemigrations rss
2. python manage.py migrate
3. python manage.py runserver
4. it is necessary to create a super user for the django admin interface:
-- python manage.py createsuperuser (for dev purposes, its OK to skip and use basic admin/admin credentials)

As the application does not currently use any cronjobs, it is necessary to manually launch a special command to retrieve data in all models:
python manage.py rss [option]  -->>>> option in ['actual','news','newest','sport','tech','lifestyle','viral','show']

Aplication is usually started on http://127.0.0.1:8000 on local machine and it redirects to /home/actual/ page
If you ran the special command correctly, the data should be displayed on the pages

# NOTE:
During work and running the server, I had problems with 'default_auto_field' option in /rss/apps.py, 
Commenting that part of code help me to start server, unfortunately, I didn't have enough time to investigate and solve problem till writing this document.
But I will in future.

# CREDITS
INSTALLATION:
• https://docs.djangoproject.com/en/4.0/intro/install/
Tutorial:
• https://docs.djangoproject.com/en/4.0/intro/tutorial01/
Management command: 
• https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/
Django admin: 
• https://docs.djangoproject.com/en/4.0/intro/tutorial02/#introducing-the-django-admin
Feed parser: 
• https://feedparser.readthedocs.io/en/latest/
AND OF COURSE, I KNOW HOW TO GOOGLE :)