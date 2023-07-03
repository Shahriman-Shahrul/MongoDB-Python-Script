import requests
import json

integrationUrl = "http://localhost:3001"
integration_endpoint = "/api/v1/integration/agency"


r = requests.post(
    integrationUrl + integration_endpoint, data=json.dumps(
        {
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
    ),
    headers={
        "Content-type": "application/json",
        "Accept": "application/json"
    },
    verify=False
)

print(r.json()["status"])
print(r.json()["message"])
