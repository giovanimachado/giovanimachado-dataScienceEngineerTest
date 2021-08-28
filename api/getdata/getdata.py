from sanic.response import json
from sanic import Blueprint
from sanic.log import logger
import os
import pandas as pd
import json as py_json
import numpy as np

take = Blueprint("take")

@take.route('/data', methods=['POST'])
async def data_slicer(request):
    try:
        logger.info('Request sent to /api/data endpoint')
        logger.info(request.json)
        print(request.json)
        start_time = request.json[0]["from"]
        end_time = request.json[0]["to"]
        metrics = request.json[0]["metrics"]
        os.chdir("./data")
        df = pd.read_csv('data.csv', index_col=0)
        df = df.loc[start_time:end_time, metrics]
        result = py_json.loads(df.to_json(orient="columns"))
        print(result)
        os.chdir("..")
        logger.info(result)
        logger.info('Request to /api/data endpoint fulfilled')
        return json(result, status=200)
    except:
        logger.info("Error in data route")
        return json({"Message":"Error in data route","Status":"500"}, status=500)