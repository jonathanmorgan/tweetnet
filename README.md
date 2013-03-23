Tweetnet is a django application for capturing Twitter data and creating networks from it.

It can also serve as a base for other more specific twitter projects.  It contains abstract Tweet and Tweet_User classes, and then concrete implementations of those classes, usable if you don't want any additional fields.

Not a whole lot else to say here at the moment until I start integrating code to easily pull in tweets for a user, or based on a topic.

To install, pull the application from github, then place it in a working django site and add it as a new application in settings.py.

From the django-enabled python shell (python manage.py shell), enter "import <site>.tweetnet" to pull in the tweetnet context.

For examples of how to authenticate and interact with twitter using a number of different python twitter and oauth libraries, see sample_code.py.