import  requests
from datetime import datetime

USERNAME = "mansrathore"
TOKEN = "kalvbuykc6578afvdgad8b"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" :  TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes" ,
    "notMinor" :  "yes" ,
}

# response = requests.post(url=pixela_endpoint ,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id"   :   "graph2",
    "name"  :   "Coding Graph ",
    "unit" :  "hours",
    "type" :  "int",
    "color" : "shibafu",
}

headers = {
    "X-USER-TOKEN"  :  TOKEN
}

# response = requests.post(url=graph_endpoint ,json=graph_params,headers=headers)
# print(response.text)

post_endpoint =  f"{graph_endpoint}/{graph_params["id"]}"

today = datetime.now()


post_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "3" ,
}

# response = requests.post(url=post_endpoint ,json=post_params,headers=headers)
# print(response.text)

put_del_endpoint = f"{post_endpoint}/{post_params["date"]}"

put_params = {
    "quantity" :  "1" ,
}
# response = requests.put(url=put_del_endpoint ,json=put_params,headers=headers)
# print(response.text)


#del_request
response = requests.delete(url=put_del_endpoint ,headers=headers)
print(response.text)

