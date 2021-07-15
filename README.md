# timelinor-mockup
A first static mockup version of the Timelinow web app.

# Deployment

Set the following environment variables:
* SECRET_KEY
* DEBUG
* APP_ENV ('dev', 'staging', or 'production')
## Local/dev

* Create a virtual environment with virtualenvwrapper:

    `mkvirtualenv timelinor` 

* Set environment variables via `postactivate` file

## Staging via Heroku

* Create Heroku app
* Push repo to Heroku
* Set environment variables in Heroku app settings

Further reading:
* [Heroku Docs - Django deployment](https://devcenter.heroku.com/articles/django-app-configuration)
