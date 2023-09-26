# Hands on Cloud Run Tutorial

This tutorial will teach you how to deploy a simple client (Javascript/React) and server (Python/FastAPI) to Google Cloud Run.

### Prerequisites

* Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
* Install [Node.js](https://nodejs.org/en/download/)

Verify installs by testing the above tools in the command line
```
gcloud --version
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
// check http://127.0.0.1:4244/
```

Have a look at `server/Dockerfile`. This file defines the container environment that gcloud will use to host your Python application. Also familiarize yourself with the [serverless concept](https://en.wikipedia.org/wiki/Serverless_computing) of CloudRun. An app deployed in Cloud Run must fulfill [those requirements](https://cloud.google.com/run/docs/fit-for-run). Now deploy your code using this command from the cloud CLI:

```
gcloud run deploy <YOUR_NAME>-demo-server --source . --allow-unauthenticated
```

Once the command has finished successfully finished, visit the URL that is printed in the terminal. You should see the same output as when you ran the app locally. Also, inspect the options that are available for your deployment from the [Cloud Console](https://console.cloud.google.com/run?referrer=search&project=nsf-2124179-159391).

## Deploy React Client

Navigate to the client directory and install all local dependencies

```
cd ../client
npm install
```


Now, update the `client/.env.production` to the URL that has been generated by the Cloud Run deployment of the server. By using both the `client/.env` and `client/.env.production` React knows which URL to use depending on whether you are developing locally or you are using the deployed version. Next, have a look at `client/Dockerfile`. What is different from the `server/Dockerfile`?  

Deploy react client to Cloud Run
```
gcloud run deploy <YOUR_NAME>-demo-client --source . --allow-unauthenticated
```
This should give you a URL to your deployed React app if successful. The frontend website should display something like `Hello World! - This was loaded dynamically through an endpoint!` if everything worked out. 
