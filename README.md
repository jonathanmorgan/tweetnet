# tweetnet

## Description

Tweetnet is a django application for capturing Twitter data and creating networks from it.

It can also serve as a base for other more specific twitter projects.  It contains Tweet and Tweet_User classes that you can extend to add co-keyed tables that can contain more information on each tweet.  You could also abstract these classes, or just copy and add stuff on to them if you need flat, single-table twitter data for ease of analysis (been there, done that).

Not a whole lot else to say here at the moment until I start integrating code to easily pull in tweets for a user, or based on a topic.

## Dependencies

Depends no "twitter" tweet collection package, and on my python_utilities github repository [https://github.com/jonathanmorgan/python_utilities](https://github.com/jonathanmorgan/python_utilities).

Also depends on Django 1.7 or greater.  Old South-based migrations are in the `/south_migrations folder`, but they are not going to be updated going forward.

## Installation

### Django setup

- in your work directory, create a django site.

        django-admin.py startproject <site_directory>
    
- cd into the site\_directory

        cd <site_directory>
    
- pull in Jon's python\_utilities

        git clone https://github.com/jonathanmorgan/python_utilities.git

- pull in tweetnet python code

        git clone https://github.com/jonathanmorgan/tweetnet.git
    
### Install python packages

- install pip

        (sudo) easy_install pip

- use pip to install required packages:

    - tweetnet/requirements.txt contains a list of required packages.  To install requirements using requirements.txt and pip:

            (sudo) pip install -r sourcenet/requirements.txt

    - or, install each individually:

    - install ipython

            (sudo) pip install ipython

    - install six

            (sudo) pip install six

    - install pytz

            (sudo) pip install pytz

    - install django

            (sudo) pip install django

    - install the twitter python library

            (sudo) pip install twitter

    - if using postgresql, install postgresql database driver (psycopg2)

            (sudo) pip install psycopg2
        
    - if using mysql, install mysql database driver (MySQL-python)

            (sudo) pip install MySQL-python
        
        or you can install it using your OS's package manager (sometimes easier to get it to compile).

### Django Configuration

- from the site\_directory, cd into the site configuration directory, where settings.py is located (it is named the same as site\_directory, but nested inside site\_directory, alongside all the other django code you pulled in from git - <site\_directory>/<same\_name\_as\_site\_directory>).

        cd <same_name_as_site_directory>

- if you want to use logging, in settings.py, configure logging near the top of the file:

        import logging
        
        logging.basicConfig(
            level = logging.DEBUG,
            #level = logging.INFO,
            format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
            filename = '<log_file_path>',
            filemode = 'w'
        )

- configure the database in settings.py

    - For postgresql (recommended becuase of unicode support):

        - create postgresql database.
        - create user to interact with postgresql database.  Set permissions so user has all permissions to your database.
        - In settings.py, in the DATABASES structure:
            - set the ENGINE to "django.db.backends.postgresql_psycopg2"
            - set the database NAME, USER, and PASSWORD.
            - If the database is not on localhost, enter a HOST.
            - If the database is listening on a non-standard port, enter a PORT.
        - Example:

                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': 'tweetnet',                      # Or path to database file if using sqlite3.
                        # The following settings are not used with sqlite3:
                        'USER': 'django_user',
                        'PASSWORD': '<pgsql_password>',
                        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                        'PORT': '',                      # Set to empty string for default (5432).
                    }
                }

    - For sqlite3:

        - figure out what file you want to hold the database.  For the initial implementation, we used reddit.sqlite in same directory as code (/home/socs/socs_reddit/reddit_collect/reddit.sqlite).
        - In settings.py, in the DATABASES structure:
            - set the ENGINE to "django.db.backends.sqlite3"
            - set the database NAME (path to file), USER and PASSWORD if you set one on the database.
            - If the database is not on localhost, enter a HOST.
            - If the database is listening on a non-standard port, enter a PORT.
        - Example:

                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': '/home/socs/socs_reddit/reddit_collect/reddit.sqlite',                      # Or path to database file if using sqlite3.
                        # The following settings are not used with sqlite3:
                        'USER': '',
                        'PASSWORD': '',
                        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                        'PORT': '',                      # Set to empty string for default.
                    }
                }


    - For mysql:

        - create mysql database.
            - at the least, make your database use character set utf8 and collation utf8_unicode_ci
            - To support emoji and crazy characters, in mysql >= 5.5.2, you can try setting encoding to utf8mb4 and collation to utf8mb4\_unicode\_ci instead of utf8 and utf8\_unicode\_ci.  It didn't work for me, but I converted the database instead of starting with it like that from scratch, so your mileage may vary.  If you need to do this to an existing database:

                    ALTER DATABASE <database_name> CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

        - create user to interact with mysql database.  Set permissions so user has all permissions to your database.
        - In settings.py, in the DATABASES structure:
            - set the ENGINE to "django.db.backends.mysql"
            - set the database NAME, USER, and PASSWORD.
            - If the database is not on localhost, enter a HOST.
            - If the database is listening on a non-standard port, enter a PORT.
        - Example:

                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': 'socs_reddit',                      # Or path to database file if using sqlite3.
                        # The following settings are not used with sqlite3:
                        'USER': 'socs_reddit',
                        'PASSWORD': '<mysql_password>',
                        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                        'PORT': '',                      # Set to empty string for default.
                    }
                }

- in settings.py, add 'tweetnet' to the INSTALLED\_APPS list.  Example:
    
        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            # Uncomment the next line to enable the admin:
            # 'django.contrib.admin',
            # Uncomment the next line to enable admin documentation:
            # 'django.contrib.admindocs',
            'tweetnet',
        )

- Once database is configured in settings.py, in your site directory, run "python manage.py migrate" to create database tables.

## Usage

There are examples of usage in tweetnet/examples:

- sample_twitter_collector.py - example that opens a StreamCollector, uses django model class to store a subset of their information in a database.
- sample_tweet_consumer.py - (IN PROGRESS) example that loops over tweets in database, gets user information, gets each user's tweets, then adds those tweets to the database.
- sample_libraries_oauth.py - examples of how to authenticate and interact with twitter using a number of different python twitter and oauth libraries.

From the django-enabled python shell (python manage.py shell), enter "import tweetnet" to pull in the tweetnet context.

### Getting imports in your shell

The easiest way to run code from a shell is to go to your django sites folder and use manage.py to open a shell:

    python manage.py shell
    
If you choose, you can also just open the base python interpreter:

    python
    
Or you can install something fancier like ipython, and then run ipython:

    ipython
    
If you don't use manage.py to open a shell (or if you are making a shell script that will be run on its own), you'll have to do a little additional setup to pull in and configure django:

    # make sure the site directory is in the sys path.
    import sys
    site_path = '<site_folder_full_path>'
    if site_path not in sys.path:
        
        sys.path.append( site_path )
        
    #-- END check to see if site path is in sys.path. --#
    
    # if not running in django shell (python manage.py shell), make sure django
    #    classes have access to settings.py
    # set DJANGO_SETTINGS_MODULE environment variable = "<site_folder_name>.settings".
    import os
    os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "<site_folder_name>.settings"

# TODO

- Add tables for hashtags, URLS.