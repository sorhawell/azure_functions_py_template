# add local packages to path
import sys
sys.path.append(".python_packages/lib/site-packages")

import azure.functions as func
import datetime
import json
import logging


app = func.FunctionApp()

import os
import my_stuff;


def list_files(startpath):
    result = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        result += '{}{}/\n'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            result += '{}{}\n'.format(subindent, f)
    return result



@app.route(route="HttpExample", auth_level=func.AuthLevel.ANONYMOUS)
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:

    logging.info(sys.path)
    
    logging.info('Python HTTP trigger function processed a request.')

  
    #POC use local package which again uses sqlalchemy
    logging.info(str(my_stuff.sa))

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             #"This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             list_files("."),
             status_code=200
        )