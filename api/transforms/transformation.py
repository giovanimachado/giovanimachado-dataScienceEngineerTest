from sanic.response import json
from sanic import Blueprint
from sanic.log import logger
import os
import pandas as pd
import json as py_json
from .echo_opt import the_good_func
import numpy as np

trans = Blueprint("transformation")

@trans.route('/transformation', methods=['POST'])
async def to_transform(request):
    try:
        logger.info('Request sent to transfomation endpoint')
        logger.info(request.json)
        start_time = request.json[0]["from"]
        end_time = request.json[0]["to"]
        metrics = request.json[0]["metrics"]
        #print(os.getcwd())
        os.chdir("./data")
        df = pd.read_csv('data.csv', index_col=0)
        df_sliced = df.loc[start_time:end_time, metrics]
        # By default, a view is returned, so any modifications made will affect the original dataframe. edir
        arr = df_sliced.to_numpy()
        for i in np.arange(arr.shape[1]):
            #print(i)
            arr[:,i]=the_good_func(arr[:,i], tol=2)
        df_transformed = df_sliced
        result = py_json.loads(df_transformed.to_json(orient="columns"))
        #print(result)
        logger.info(result)
        logger.info('Request to /api/transformation endpoint fulfilled')
        os.chdir("..")
        return json(result, status=200)
    except Exception as error:
        logger.info("Error in transformation route")
        #logger.info(error)
        logger.error(str(error))
        return json({"Message":"Error in transformation route","Status":"500"}, status=500)
        #return text(result)
