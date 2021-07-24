# Timelinor
Create your own timeline graphs as a webpage, with Timelinor.

# Tech stack

Built with:
* [Python 3](https://www.python.org/)
* [Django 3](https://www.djangoproject.com/)
* [Bootstrap 5](https://getbootstrap.com/)
* [Around Bootstrap Template](https://around.createx.studio/)

# Deployment

Required environment variables in any environment, that should never be part of the codebase for security reasons:
* SECRET_KEY (Django uses this to secure the application, never share this key)
* DEBUG (Security warning: always set this to False in public environments)
* ALLOWED_HOSTS (This apps domainname)
* AWS_ACCESS_KEY_ID (Amazon S3 storage backend)
* AWS_SECRET_ACCESS_KEY (Amazon S3 storage backend)

Required environment variables for local development Postgres Docker container
* PG_NAME (Postgres database name)
* PG_USER (Postgres username, has to be the same as PG_NAME otherwise Docker container won't be accessible)
* PG_PASSWORD (Postgres database password)

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
