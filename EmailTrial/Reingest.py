import requests
import json
from datetime import datetime, timedelta

class Reingest:
    def __init__(self, mongodb_client,config):
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
        # Get the current datetime
        current_datetime = datetime.now()

        # Compare with the SLA datetime
        sla_datetime = current_datetime + timedelta(days=1)  

        if current_datetime > sla_datetime:
            # Call the API
            for _ in range(6):
                r = requests.post(self.config["integrationUrl"] + integration_endpoint,
                    data=json.dumps({
                        "jo_id": "JOP202200001",
                        "ip_id": "IPID",
                        "datasource_id": "632bfbcabc2aef398d6f7913",
                        "group_type": "nfcc",
                        "keyword": "",
                        "keyword_type": "CarPlatePipeline",
                        "request_from": "780313199993"
                    }),
                    headers={
                        "Content-type": "application/json",
                        "Accept": "application/json"
                    },
                    verify=False
                )

                if r.json()["status"] == 200:
                    break
        else:
            print("SLA datetime not reached. Skipping integration.")
        
        return self

