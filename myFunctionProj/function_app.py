import azure.functions as func
import datetime
import json
import logging
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()

    return func.HttpResponse(
        body=json.dumps(data),
        mimetype="application/json",
        status_code=200
    )
            