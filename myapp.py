
import requests

import json

URL = "http://127.0.0.1:8000/studentapi/"

# fetch the data 
# def get_data(id = None):
#     data={}
#     if id is not None:
#         data = {'id':id}
#     json_data = json.dumps(data)
#     r= requests.get(url=URL, data=json_data)
#     data = r.json()
#     print(data)

# get_data()


# Post or store the data 
# def post_data():
#     data = {
#         'name': 'kabin',
#         'roll': '5',
#         'city': 'tokha'}
#     json_data = json.dumps(data)
#     r= requests.post(url=URL, data = json_data)
#     data = r.json()
#     print(data)

# post_data()

# complete or partially update the data
# def update_data():
#     data = {
#         'id':'4',
#         'name': 'kabin',
#         'city': 'gausala'}
#     json_data = json.dumps(data)
#     r= requests.put(url=URL, data = json_data)
#     data = r.json()
#     print(data)

# update_data()

#delete the data
def delete_data():
    data ={'id':1}
    json_data = json.dumps(data)
    r= requests.delete(url=URL, data = json_data)
    data = r.json()
    print(data)

delete_data()