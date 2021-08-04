# Timelinor
Spice up your resume or online portfolio with a **good looking timeline** of your heroic feats!

Create your own timeline graphs 'as-a-webpage', with Timelinor!

You can find it [here](https://timelinor.herokuapp.com/) (registration is free)!

![Screenshot](/frontend/static/img/showcase-1.png)

### Description

I built this web application as part of [the final assignment of Harvard’s CS50 programming course](https://cs50.harvard.edu/x/2021/project/).

I had several aims with this project:

1. Apply my knowledge of the Django and Bootstrap frameworks
2. Build a CI/CD pipeline using the Heroku platform
3. Create a web tool that may actually be useful for some people
4. Make the app look as professional and great as possible

### Video demo: https://youtu.be/bM8lZVx4Lnk (3 minutes)
# Technical Features

* Tech stack:
    * [Python 3](https://www.python.org/)
    * [Django 3](https://www.djangoproject.com/)
    * [Bootstrap 5](https://getbootstrap.com/)
    * [Around Bootstrap Template](https://around.createx.studio/)
    * [Postgres](https://www.postgresql.org/)
    * [Docker](https://www.docker.com/)
* Fully-fledged user authentication system:
    * Login and registration
    * Customize profile
    * Password reset procedure via email
* Notable Django features employed:
    * [Messages](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/)
    * [Signals](https://docs.djangoproject.com/en/3.2/topics/signals/)
    * [Custom User model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)
    * [Model Formsets](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#model-formsets)
* Notable Third-party Django libraries used:
    * [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    * [Django Environ](https://django-environ.readthedocs.io/en/latest/)
    * [Django Extensions](https://django-extensions.readthedocs.io/en/latest/)
    * [Django Storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) (in combination with Amazon S3 buckets, for static file serving)
* Notable Python library used:
    * [Black](https://github.com/psf/black), the uncompromising code formatter
* CI/CD
    * Local development:
        * Django's development server
        * Docker Postgres container (`docker-compose.yml` and sample `.env` file included in `docker` folder in project root)
    * Staging and production:
        * After developing locally, code base can easily be pushed to a [Heroku](https://www.heroku.com/) pipeline, consisting of both a staging and a production environment
        * Required Heroku config files (`Procfile`, `runtime.txt`, and `requirements.txt`) are part of this code base
    * [Environment variables](#set-environment-variables) are used in every environment for sensitive data like database credentials, AWS, mail server, etc.
        * Separate Postgres databases can be configured using said environment variables

# Deployment

## Set environment variables

### Any environment (local/dev, staging, and production)
Required environment variables in any environment (local/dev, staging, and production), that should never be part of the codebase for security reasons:
* SECRET_KEY (Django uses this to secure the application, never share this key!)
* DEBUG (Security warning: always set this to False in public environments)
* ALLOWED_HOSTS (This apps domain name - you can add multiple host names separated by comma's)
* AWS_ACCESS_KEY_ID (Amazon S3 storage backend)
* AWS_SECRET_ACCESS_KEY (Amazon S3 storage backend)
* EMAIL_HOST (SMTP server)
* EMAIL_HOST_USER (SMTP username)
* EMAIL_HOST_PASSWORD (SMTP password)
* DEFAULT_FROM_EMAIL (Default 'from' email)

### Local

Additional required environment variables for the Postgres Docker container in your local/dev environment:
* PG_NAME (Postgres database name)
* PG_USER (Postgres username, has to be the same as PG_NAME otherwise Docker container won't be accessible)
* PG_PASSWORD (Postgres database password)

### Staging and production
Additional required environment variables for staging and production:
* `DJANGO_SETTINGS_MODULE` (points to correct settings file, either `timelinor.settings.staging` or `timelinor.settings.production`)

See the various settings files in the `settings` folder for further details.

## Installation

### Local

* Create a virtual environment, for instance with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html):

    `mkvirtualenv timelinor` 

* Consider [setting environment variables](#set-environment-variables) via virtualenvwrapper's `postactivate` file
* Install required packages with:

    `pip install -r requirements/local.txt`
* Note there are multiple settings files (in the `settings` folder), and that the `DJANGO_SETTINGS_MODULE` variable in both `manage.py` and `wsgi.py` are set to `timelinor.settings.local` by default

### Staging and Production via Heroku

See the docs:
* [Heroku Docs - Django deployment](https://devcenter.heroku.com/articles/django-app-configuration)
* [Video explaining the basics](https://www.youtube.com/watch?v=1923eduj0Gg)

* Install required packages with:

    `pip install -r requirements/local.txt`

# Important notes

Important notes:
## Models

* Note that a [custom User model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) is used, make sure to [correctly reference](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#referencing-the-user-model) it in views and models
