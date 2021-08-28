# Company X Test Project

This repository contains instructions and data for a test project for the
role of Data Science Engineer in Company X Data Science team.

## Overview

The goal of the project is to devise and implement a prototype for a
microservice that acts as a dataprovider.

## Background

Company X offers data-driven models for real-time prediction, simulation
and optimization to our customers in the Z sector. These models are hosted
on cloud servers in microservices that provide a HTTP API for requesting specific
predictions. One central component of the clusters are dataprovider services that,
upon request, return the data required for the calculations that are carried out
in the models.


## Environment

Usually, the data comes from databases such as Mongo DB, but, for this test, the data source for the test project will be a CSV file that can
be hosted together with the dataprovider service.

The service should have two endpoints:

1. Endpoint called `data` for requesting data of specific metrics over a given period of time
2. Endpoint called `transformed` for requesting data as in case 1., but with an additional
   transformation function applied to the data

The response should be a JSON-encoded string containing all the (minutely) data
for the chosen metrics and time period.

The service should be written using the Sanic package for microservices in Python
available at https://github.com/huge-success/sanic

For endpoint #2, the provided transformation function in `transforms/echo.py`
should be optimized computationally and implemented inside the service.


## Example Requests

#### Endpoint 1.
`curl -XPOST localhost:8080/data -d '{"from": "2016-01-10T00:00:00", "to": "2016-01-10T01:00:00", "metrics": ["Bearing Pressure A (kPa)", "Bearing Pressure B (kPa)"]}'`

#### Endpoint 2.
`curl -XPOST localhost:8080/transformed -d '{"from": "2016-01-10T00:00:00", "to": "2016-01-10T01:00:00", "metrics": ["Bearing Pressure A (kPa)", "Bearing Pressure B (kPa)"]}'`


## Activities to be performed

- Become familiar with the Sanic microservice framework
- Implement the microservice
- Set up the first endpoint for raw data requests using time stamps for start
  and end dates and a list of metrics to be returned as JSON
- Optimize and implement the transformation function to be applied
  to the data for the second endpoint
- Add helpful logging to the service
- Write a README.md for users of the service


## Provided Resources

- data.csv containing multivariate time-series data from a SAG mill
- Sanic microservice package
- Selection of transform functions


## Project Output

- Dataprovider prototype code with README.md


<br>

# Service implementation

<div align="center">



Working and learning!

![Working](https://media2.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif?cid=ecf05e47zt9dh640cf0m15fepxiu2znu27i3x99z2qud90cd&rid=giphy.gif&ct=g)

</div>

## tasks

- ~~Become familiar with the Sanic microservice framework~~ 
- ~~Implement the microservice~~
- ~~Set up the first endpoint for raw data requests using time stamps for start and end dates and a list of metrics to be returned as JSON~~
- ~~Optimize and implement the transformation function to be applied to the data for the second endpoint~~
- ~~Add helpful logging to the service~~
- ~~Write a README.md for users of the service~~
- **~~Refactor the code~~**

## Directory layout

    .
    ├── api
    ├    ├── getdata            # Directory containing code to respond to data requests
    ├    ├── hello              # Directory containing a simple script to be used on root
    ├    ├── transforms         # Directory containing optimized transformation function and api/transformation 
    ├── data                    # Directory containing data used on routes api/data and api/transformation
    ├── server.py               # main file 
    └── README.md

## How to run the project?

Choose a folder in you computer, open gitbash and run

`$ git clone https://gitlab.com/giovani.machado/testproject.dst.dataprovider`

Install necessary packages (it is recommended to run in a dedicated Environment)

`pip install sanic numpy pandas`

Change to directory _testproject.dst.dataprovider/

`$ cd testproject.dst.dataprovider`

Run the server

`Sanic server.app`

With the server running it is possible to send http requests to endpoints #1 and #2 (there is a postman collection available here)


## Endpoint 1 

### Using the command line:
`$ curl -XPOST localhost:8000/api/data -d '[{"from": "2016-01-10T00:00:00", "to": "2016-01-10T01:00:00", "metrics": ["Bearing Pressure A (kPa)", "Bearing Pressure B (kPa)"]}]'
`

### Using postman
POST request to `localhost:8000/data`:

Body

```json
[
    {
        "from":"2016-01-10T00:00:00", 
        "to": "2016-01-10T01:00:00", 
        "metrics": ["Bearing Pressure A (kPa)", "Bearing Pressure B (kPa)"]
    }
]
```

### Response:

```json
{
    "Bearing Pressure A (kPa)": {
        "2016-01-10T00:00:00": 4995.8025290157,
        "2016-01-10T00:01:00": 4987.5011554459,
        "2016-01-10T00:02:00": 4958.5134380638,
        ...
        "2016-01-10T00:58:00": 4996.6875023567,
        "2016-01-10T00:59:00": 4954.1331844548,
        "2016-01-10T01:00:00": 4991.156250382
    },
    "Bearing Pressure B (kPa)": {
        "2016-01-10T00:00:00": 5104.0679771276,
        "2016-01-10T00:01:00": 5073.2560418776,
        "2016-01-10T00:02:00": 5101.3238254586,
        ...
        "2016-01-10T00:58:00": 5060.374646875,
        "2016-01-10T00:59:00": 5056.4358806473,
        "2016-01-10T01:00:00": 5096.2730164364
    }
}
```

## Endpoint 2 

### Request Using the command line:
`$ curl -XPOST localhost:8000/api/transformation -d '[{"from": "2016-01-10T00:00:00", "to": "2016-01-10T01:00:00", "metrics": ["Bearing Pressure A (kPa)", "Bearing Pressure B (kPa)"]}]'
`

### Request Using postman
POST request to `localhost:8000/transformed`

Body

```json
[
    {
        "from":"2016-01-10T00:00:00", 
        "to": "2016-01-10T01:00:00", 
        "metrics": ["Bearing Pressure A (kPa)", "Bearing Pressure B (kPa)"]
    }
]
```

### Response (considering tol = 2):

```json
{
    "Bearing Pressure A (kPa)": {
        "2016-01-10T00:00:00": 4995.8025290157,
        "2016-01-10T00:01:00": 4991.6518422308,
        "2016-01-10T00:02:00": 4980.6057075085,
        "2016-01-10T00:03:00": 4979.7169325957,
        ...
        "2016-01-10T00:57:00": 4985.0153486332,
        "2016-01-10T00:58:00": 0.0,
        "2016-01-10T00:59:00": 0.0,
        "2016-01-10T01:00:00": 0.0
    },
    "Bearing Pressure B (kPa)": {
        "2016-01-10T00:00:00": 5104.0679771276,
        "2016-01-10T00:01:00": 5088.6620095026,
        "2016-01-10T00:02:00": 5092.8826148212,
        "2016-01-10T00:03:00": 5100.7996004468,
        ...
        "2016-01-10T00:57:00": 5055.8827407401,
        "2016-01-10T00:58:00": 0.0,
        "2016-01-10T00:59:00": 0.0,
        "2016-01-10T01:00:00": 0.0
    }
}
```
