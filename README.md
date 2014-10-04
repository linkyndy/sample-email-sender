sample-email-sender
===================

A sample e-mail sender built with love on Flask, MongoDB, SendGrid and hosted on Heroku.

Deploy
----------

The app is already up and running at http://sample-email-sender.herokuapp.com/.

Install locally
---------------

If you'd like to install this app locally, just follow these simple steps:

1. Clone this repo

2. `pip install -r requirements.txt`

3. Set required env vars (hint: check config.py)

4. `python manage.py bootstrap`

5. `python manage.py runserver` and voila!

Note: For faster prototyping, this app uses Heroku's addons for MongoDB and SendGrid. If you don't want to use those addons, check the appropriate documentation for installing MongoDB and SendGrid on your local machine.
