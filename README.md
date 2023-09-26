# cloudrun-demo

This tutorial will teach you how to deploy a simple client (javascript/react) and server (python/fastapi) to Google Cloud Run.

### Prerequisites

* Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
* Install [Docker](https://docs.docker.com/get-docker/)
* Install [Node.js](https://nodejs.org/en/download/)

Verify installs by testing the above tools in the command line
```
gcloud --version
docker --version
npm --version
```

### Setup

Login to gcloud project

```
gcloud auth login // prompts for login
gcloud config set project nsf-2124179-159391
gcloud config get-value project // verify project id
```

Clone to tutorial repo

```
git clone https://github.com/VCG/cloudrun-demo.git
cd cloudrun-demo
```

## Deploy Python Server

Install local dependencies and test locally

```
cd server
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the app locally

```
python main.py
// check http://127.0.0.1:4242/
```

Have a look at the Dockerfile in your server directory. This file defines the container environment, that gcloud will use to host your python application. ALso familiarize yourself with the [serverless concept](https://en.wikipedia.org/wiki/Serverless_computing) of CloudRun. An app deployed in Cloud Run must fulfill [those requirements](https://cloud.google.com/run/docs/fit-for-run). Now deploy your code using this command from the cloud CLI:

```
gcloud run deploy <YOUR_NAME>-demo-server --source . --allow-unauthenticated
```

Once the command has finished successfully finished, visit the URL that is printed in the terminal. You should see the same output as when you ran the app locally. Also, inspect the options that are available for your deployment from the [Cloud Console](https://console.cloud.google.com/run?referrer=search&project=nsf-2124179-159391).

## Deploy React Client

Navigate to the client directory and install all local dependencies

```
cd ../client

```
