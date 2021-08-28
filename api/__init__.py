from sanic.response import json
from sanic import Sanic
import sys, os
from sanic import Blueprint
#sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/hello/')
#from hello import hello
from .hello.hello import hello

#sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/transforms/')
#from transformation import trans
from .transforms.transformation import trans

# sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/getdata/')
# from getdata import take
from .getdata.getdata import take

api = Blueprint.group(trans, take, hello, url_prefix="/api")