import json as py_json
import importlib
import sys, os.path
from sanic import Sanic
from sanic.log import logger
from sanic.response import HTTPResponse, json
from sanic.response import text
from sanic import response
import pandas as pd
import os
import json as json_python
import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/api/')
#print(sys.path)
from api import api
#from .api import api

# #to import the echo function 
#sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/transforms/')
#from echo_opt import the_good_func

app = Sanic("dataProvider")
app.blueprint(api)
   
@app.get('/')
async def root(request):
    print(request.args)
    logger.info('Request sent to root, redirected to /api;')
    return response.redirect('/api/')
    
if __name__ == '__main__':
    app.run(access_log=True)
