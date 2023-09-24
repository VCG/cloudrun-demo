# cloudrun-demo
This tutorial demonstrates on how to deploy python/javascript-based apps using Google Cloud Run. 

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
```

Clone to tutorial repo

```
git clone https://github.com/VCG/cloudrun-demo.git
cd cloudrun-demo
```

## Deployment Tutorial

### Deploy python app to Cloud Run

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
// check http://127.0.0.1:4242/helloworld
```

Deploy to Cloud Run

```
gcloud run deploy <YOUR_NAME>-demo-server --source . --allow-unauthenticated
```
