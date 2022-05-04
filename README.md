# BTC Price & Profit API 

## About

This is an API that works as the backend of <a href = "https://bitcoin-chart-project.web.app/">this project</a>. It was written using FastAPI and uses MongoDB. 


## Installing

Use the following commands to create a virtual environment on your Linux/Mac:

```
python3 -m venv venv
source venv/bin/activate
```

To install the dependencies of the project, use this command:

```
python3 -m pip install -r requirements.txt
```

To run the API locally, just run the main.py file.

## Deployment

### Docker

In the main branch, to facilitate the creation of the docker image use the docker-compose file with this command:

```
docker-compose up
```
### AWS Lambda

In the "lambda" branch, the deployment is done directly through a CI/CD Pipeline that deploys the API to AWS.
