# timelinor-mockup
A first static mockup version of the Timelinow web app.

# Deployment

Required environment variables:
* SECRET_KEY
* DEBUG
* APP_ENV ('dev', 'staging', or 'production')
## Local/dev

* Create a virtual environment with virtualenvwrapper:

    `mkvirtualenv timelinor` 

* Set environment variables via `postactivate` file
* Install required packages with:

    `pip install -r requirements/local.txt`

## Staging via Heroku

Required files for Heroku:
* `Procfile`
* `requirements.txt` (the one in the project root folder)

Also note certain (clearly commented) settings in `settings.py`.

Deploy as follows:
* Create Heroku app
* Push repo to Heroku
* Set environment variables in Heroku app settings

Further reading:
* [Heroku Docs - Django deployment](https://devcenter.heroku.com/articles/django-app-configuration)
