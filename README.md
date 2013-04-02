# tweetnet

## Description

Tweetnet is a django application for capturing Twitter data and creating networks from it.

It can also serve as a base for other more specific twitter projects.  It contains Tweet and Tweet_User classes that you can extend to add co-keyed tables that can contain more information on each tweet.  You could also abstract these classes, or just copy and add stuff on to them if you need flat, single-table twitter data for ease of analysis (been there, done that).

Not a whole lot else to say here at the moment until I start integrating code to easily pull in tweets for a user, or based on a topic.

## Dependencies

None, so far.

## Installation

To install, pull the application from github, then place it in a working django site.  This will make the classes includable from other applications in the site.

From the django-enabled python shell (python manage.py shell), enter "import \<site\>.tweetnet" to pull in the tweetnet context.

If you want to create admins from it, you can also add it as a new application in settings.py.

## Also, Twitter API examples
For examples of how to authenticate and interact with twitter using a number of different python twitter and oauth libraries, see sample_code.py.