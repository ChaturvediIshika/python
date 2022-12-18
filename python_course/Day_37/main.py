import requests
from datetime import datetime

url_endpoint="https://pixe.la/v1/users"
post_parameters={
    "token":"asdfghjkl", 
    "username":"cishika104", 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}

# response=requests.post(url=url_endpoint,json=post_parameters)
# print(response.text)

graph_endpoint=f"{url_endpoint}/{post_parameters['username']}/graphs"

graph_config={
    "id":"graph12",
    "name":"my graph",
    "unit":"minute",
    "type":"int",
    "color":"kuro"
}

headers={
    "X-USER-TOKEN":"asdfghjkl"
}

# response=requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

post_endpoint=f"{url_endpoint}/{post_parameters['username']}/graphs/{graph_config['id']}"

today=datetime.now()

post_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":"35"
}

response=requests.post(url=post_endpoint,json=post_config, headers=headers)
print(response.text)