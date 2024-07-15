# curly-enigma

Prototype implementeation for the API

## Running locally

Start the dev server like this:

`$gunicorn --chdir frontend --workers 1 --threads 4 --timeout 0 server:app`

Note: before starting the dev server, you should activate your python virtual environment (or create one if you don't
yet have one, and install the dependencies from the requirements.txt file.)

## Deploying the code to Google Cloud

In a terminal, run:

`gcloud run deploy curly-enigma-frontend --source . --region europe-central2`

After deployment, you can reach it at a cloud url, something like:

`https://curly-enigma-frontend-kbvtjqk7tq-lm.a.run.app/`

Note: before running `gcloud deploy` you need to authenticate yourself. To authenticate, run:

`$gcloud auth login`

```
You are now logged in as [hannakollo@google.com].
Your current project is [gic-sandbox-428315].  You can change this setting by running:
```
