import requests
import json
from datetime import datetime, timedelta


class Reingest2:
    def __init__(self, mongodb_client, config):
        self.mongodb_client = mongodb_client
        self.datasource_ids = []
        self.keyword_dict = {}
        self.configs = config

    def get_info_from_mongodb(self):
        collection = self.mongodb_client.nfis.problem_data
        result = list(collection.find({"status": 2}))

        keyword_dict = {}

        for d in result:
            datasource_id = d["_id"]["data_source_id"]
            keyword = d["_id"]["keyword"]

            if datasource_id not in keyword_dict:
                keyword_dict[datasource_id] = set()
            keyword_dict[datasource_id].add(keyword)

        self.datasource_ids = list(keyword_dict.keys())
        self.keyword_dict = keyword_dict

        return self

    def trigger_nfis_integration(self, integration_endpoint):
        # # Get the current datetime
        # current_datetime = datetime.now()

        # # Compare with the SLA datetime
        # sla_datetime = current_datetime + timedelta(days=1)

        # if current_datetime > sla_datetime:
        #     # Iterate through each datasource_id and keyword set
        # for datasource_id, keywords_set in self.keyword_dict.items():
        #     keywords = list(keywords_set)

            # Prepare the payload for the POST request
            payload = {
                "rfi_id": self.rfi_id,
                "jo_id": "JOP202200001",
                "ip_id": "IPID",
                "datasource_id": datasource_id,
                "group_type": "nfcc",
                "keyword": "",
                "keyword_type": "CarPlatePipeline",
                "request_from": "780313199993"
            }

            try:
                # Send the POST request
                response = requests.post(
                    self.config["integrationUrl"] + integration_endpoint,
                    data=json.dumps(payload),
                    headers={
                        "Content-type": "application/json",
                        "Accept": "application/json"
                    },
                    verify=False
                )

                # Check the response and print the result
                if response.status_code == 200:
                    print(
                        f"Integration successful for DataSource ID: {datasource_id}")
                else:
                    print(
                        f"Integration failed for DataSource ID: {datasource_id}, Status code: {response.status_code}, Response: {response.json()}")

            except Exception as e:
                print("Error occurred while sending the POST request:", str(e))
            return self

        # else:
        #     print("SLA datetime not reached. Skipping integration.")

        # return self
