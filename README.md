# Timelinor
Create your own timeline graphs 'as-a-webpage', with Timelinor!

You can find it [here](https://timelinor.herokuapp.com/)!

### Video demo: https://youtu.be/bM8lZVx4Lnk
### Description

I built this web application as part of [the final assignment of Harvard’s CS50 programming course](https://cs50.harvard.edu/x/2021/project/).

I had several aims with this project:

1. Become very comfortable with the Django and Bootstrap frameworks
2. Build a CI/CD pipeline using the Heroku platform
3. Create a web tool that might be useful for some people, in some scenario’s
4. Make the app look as professional and great as possible

#### Features:
* Tech stack:
    * [Python 3](https://www.python.org/)
    * [Django 3](https://www.djangoproject.com/)
    * [Bootstrap 5](https://getbootstrap.com/)
    * [Around Bootstrap Template](https://around.createx.studio/)
    * [Postgres](https://www.postgresql.org/)
* Fully-fledged user authentication system:
    * Login and registration
    * Customize profile
    * Password reset procedure via email
* Django features employed:
    * [Messages](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/)
    * [Signals](https://docs.djangoproject.com/en/3.2/topics/signals/)
    * [Custom User model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)
    * [Model Formsets](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#model-formsets)
* Third-party Django libraries:
    * [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    * [Django Extensions](https://django-extensions.readthedocs.io/en/latest/)
    * [Django Storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) (in combination with Amazon S3 buckets, for static file serving)
* CI/CD
    * Local development:
        * Using Django's development server
        * Docker Postgres container (`docker-compose.yml` and sample `.env` file included in `docker` folder in project root)
    * Staging and production:
        * After developing locally, code base can be pushed to [Heroku](https://www.heroku.com/)
        * Required Heroku config files (`Procfile`, `runtime.txt`, and `requirements.txt`) are part of this code base
    * Environment variables are used in every environement for sensitive data like database credentials, AWS, mail server, etc.
        * Separate Postgres databases can be configured using environement variables

# Deployment

Required environment variables in any environment, that should never be part of the codebase for security reasons:
* SECRET_KEY (Django uses this to secure the application, never share this key)
* DEBUG (Security warning: always set this to False in public environments)
* ALLOWED_HOSTS (This apps domainname - can add multiple separated by comma's)
* AWS_ACCESS_KEY_ID (Amazon S3 storage backend)
* AWS_SECRET_ACCESS_KEY (Amazon S3 storage backend)
* EMAIL_HOST (SMTP server)
* EMAIL_HOST_USER (SMTP username)
* EMAIL_HOST_PASSWORD (SMTP password)
* DEFAULT_FROM_EMAIL (Default from email)

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

# Important notes

Some notes for future development:
## Models

* Note that a [custom User model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) is used, make sure to [correctly reference](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#referencing-the-user-model) it in views and models
