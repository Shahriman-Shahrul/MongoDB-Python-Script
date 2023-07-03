# import requests
# import json

# integrationUrl = "http://localhost:3001"
# integration_endpoint = "/api/v1/integration/agency"


# r = requests.post(
#     integrationUrl + integration_endpoint, data=json.dumps(
#         {
#             "datasource_id": "64759832a192c9757f232b06",
#             "case_id": "RFI202200002",
#             "rfi_id": "RFI202200002",
#             "jo_id": "RFI202200002",
#             "ip_id": "IPID",
#             "group_type": "nfcc",
#             "keyword": "960101109999a",
#             "keyword_type": "CarPlatePipeline",
#             "request_from": "561220105657"
#         }
#     ),
#     headers={
#         "Content-type": "application/json",
#         "Accept": "application/json"
#     },
#     verify=False
# )

# print(r.status_code)
# print(r.text)


# import requests

# # Set the URL and endpoint of your Mockoon server
# integrationUrl = "http://127.0.0.1:3001"
# integration_endpoint = "/api/v1/integration/agency"

# # Set the parameters for the GET request
# params = {
#     "datasource_id": "64759832a192c9757f232b06",
#     "case_id": "RFI202200002",
#     "rfi_id": "RFI202200002",
#     "jo_id": "RFI202200002",
#     "ip_id": "IP-ID",
#     "group_type": "nfcc",
#     "keyword": "960101109999a",
#     "keyword_type": "CarPlatePipeline",
#     "request_from": "561220105657"
# }

# # Send the GET request to the Mockoon API
# response = requests.get(integrationUrl + integration_endpoint, params=params)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Print the response content (JSON data in this case)
#     print(response.json())
# else:
#     # Print an error message if the request was not successful
#     print(f"Request failed with status code {response.status_code}")


import requests
import json

# Set the URL and endpoint of your Mockoon server
# integrationUrl = "http://127.0.0.1:3001"
# integration_endpoint = "/api/v1/integration/agency"

# Set the data for the POST request
data = {
    "datasource_id": "64759832a192c9757f232b06",
    "case_id": "RFI202200002",
    "rfi_id": "RFI202200002",
    "jo_id": "RFI202200002",
    "ip_id": "IP-ID",
    "group_type": "nfcc",
    "keyword": "960101109999a",
    "keyword_type": "CarPlatePipeline",
    "request_from": "561220105657"
}

# Send the POST request to the Mockoon API
r = requests.post(
    "http://127.0.0.1:3001/api/v1/integration/agency",
    data=json.dumps(data),
    headers={"Content-type": "application/json", "Accept": "application/json"}, verify=False
)

print(r.status_code)
print(r.text)
