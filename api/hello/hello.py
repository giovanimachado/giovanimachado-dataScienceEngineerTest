from sanic import Sanic
from sanic.response import json
from sanic.response import json
from sanic import Blueprint
from sanic.log import logger

hello = Blueprint("hello")

@hello.route('/')
async def test(request):
    logger.info('Get Request to service hello')
    try:
        return json({'hello': 'IntelliSense', 
                    'accepting requests on':'[localhost:8000/api/data, localhost:8000/api/transformation]',
                    'request example':'https://gitlab.com/giovani.machado/testproject.dst.dataprovider/-/blob/master/README.md'}, status=200)
    except:
        logger.info("Error in redirection")
        return json({"Message":"Internal Error","Status":"500"}, status=500)