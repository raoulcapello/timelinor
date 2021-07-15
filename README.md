# Timelinor
Create your own timeline graphs as a webpage, with Timelinor.

# Tech stack

Built with:
* [Python 3](https://www.python.org/)
* [Django 3](https://www.djangoproject.com/)
* [Bootstrap 5](https://getbootstrap.com/)
* [Around Bootstrap Template](https://around.createx.studio/)

# Deployment

Required environment variables in any environment:
* SECRET_KEY
* DEBUG
* ALLOWED_HOSTS

Optional:
* DATABASES

See the various settings files in the settings folder for further details.
## Local/dev

* Create a virtual environment with virtualenvwrapper:

    `mkvirtualenv timelinor` 

* Set environment variables via `postactivate` file
* Install required packages with:

    `pip install -r requirements/local.txt`

## Staging and Production via Heroku

See the docs:
* [Heroku Docs - Django deployment](https://devcenter.heroku.com/articles/django-app-configuration)
* [Video explaining the basics](https://www.youtube.com/watch?v=1923eduj0Gg)
