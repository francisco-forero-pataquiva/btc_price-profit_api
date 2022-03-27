# Crypto prices backend 

## About <a name = "about"></a>

This is an API that works as the backend of <a href = "https://bitcoin-chart-project.web.app/">this project</a>. It was written using FastAPI and uses MongoDB. 


### Installing

Use the following commands to create a virtual environment on your Linux/Mac:

```
python3 -m venv venv
source venv/bin/activate
```

To install the dependencies of the project, use this command:

```
python3 -m pip install -r requirements.txt
```

To start the API, just run the main.py file.

### Docker

To facilitate the creation of the docker image use the docker-compose file with this command:

```
docker-compose up
```