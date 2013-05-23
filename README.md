# tweetnet

## Description

Tweetnet is a django application for capturing Twitter data and creating networks from it.

It can also serve as a base for other more specific twitter projects.  It contains Tweet and Tweet_User classes that you can extend to add co-keyed tables that can contain more information on each tweet.  You could also abstract these classes, or just copy and add stuff on to them if you need flat, single-table twitter data for ease of analysis (been there, done that).

Not a whole lot else to say here at the moment until I start integrating code to easily pull in tweets for a user, or based on a topic.

## Dependencies

None, so far.

## Installation

## Installation

- install pip

        (sudo) easy_install pip

- install django

        (sudo) pip install django

- install South (data migration tool), if it isn't already installed.

        (sudo) pip install South

- install the twitter python library

        (sudo) pip install twitter

- in your work directory, create a django site.

        django-admin.py startproject <site_directory>
    
- cd into the site\_directory

        cd <site_directory>
    
- pull in Jon's python\_utilities

        git clone https://github.com/jonathanmorgan/python_utilities.git

- pull in tweetnet python code

        git clone https://github.com/jonathanmorgan/tweetnet.git
    
### Configure

- from the site\_directory, cd into the site configuration directory, where settings.py is located (it is named the same as site\_directory, but nested inside site\_directory, alongside all the other django code you pulled in from git - <site\_directory>/<same\_name\_as\_site\_directory>).

        cd <same_name_as_site_directory>

- in settings.py, set USE_TZ to false to turn off time zone support:

        USE_TZ = False

- configure the database in settings.py

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


- in settings.py, add 'south' to the INSTALLED\_APPS list.  Example:
    
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
            'south',
        )

- Once database is configured in settings.py, in your site directory, run "python manage.py syncdb" to create database tables.

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
            'south',
            'tweetnet',
        )

- run `python manage.py migrate tweetnet`.

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
