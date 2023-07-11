import requests
import json
from datetime import datetime, timedelta


class Reingest:
    def __init__(self, mongodb_client, config):
        self.mongodb_client = mongodb_client
        self.config = config
        self.result = None

    def get_info_from_mongodb(self):
        collection = self.mongodb_client.NFCC.problem_data2
        result = list(collection.find({"status": 2}))

        unique_entries = set()
        filtered_result = []

        for d in result:
            data_source_id = d["_id"]["data_source_id"]
            keyword = d["_id"]["keyword"]

            # Create a unique identifier for each entry based on data_source_id and keyword
            entry_id = f"{data_source_id}_{keyword}"

            # Check if this identifier is not already present in the set
            if entry_id not in unique_entries:
                unique_entries.add(entry_id)
                filtered_result.append(d)

        self.result = filtered_result
        print(self.result)
        return self.result

    def trigger_nfis_integration(self, integration_endpoint):

        for data_item in self.result:
            # Extract information from each item in the "result" list
            rfi_id = data_item['_id']['rfi_id']
            datasource_id = data_item['_id']['data_source_id']
            keyword = data_item['_id']['keyword']
            keyword_type = data_item['keyword_type']
            request_from = data_item['request_from']

            jo_id = data_item['_id'].get('jo_id')
            ip_id = data_item['_id'].get('ip_id')

            sla_datetime_str = self.result["sla_datetime"]["$date"]
            sla_datetime = datetime.strptime(
                sla_datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            sla_datetime = current_datetime + timedelta(days=2)
            # Prepare the payload for the POST request
            payload = {
                "rfi_id": rfi_id,
                "jo_id": jo_id,
                "ip_id": ip_id,
                "datasource_id": datasource_id,
                "group_type": "nfcc",
                "keyword": keyword,
                "keyword_type": keyword_type,
                "request_from": request_from
            }

            # change this to datetime.now()
        current_datetime = sla_datetime - timedelta(days=2)

        if current_datetime < sla_datetime:
            for _ in range(6):
                try:
                    # Send the POST request
                    response = requests.post(
                        self.config["integrationUrl"] +
                        integration_endpoint,
                        data=json.dumps(payload),
                        headers={
                            "Content-type": "application/json",
                            "Accept": "application/json"
                        },
                        verify=False
                    )

                    # Check the response and print the result
                    if response.status_code == 200:
                        break
                    else:
                        raise Exception(
                            f"Integration failed for DataSource ID: {datasource_id}, Status code: {response.status_code}, Response: {response.text}")

                except Exception:
                    print(
                        "Error occurred while sending the POST request:", response.text)
        else:
            raise Exception(
                f"Integration failed for DataSource ID: {datasource_id}, Status code: {response.status_code}, Response: {response.text}")

        return self

    def trigger_nfis_integration2(self, integration_endpoint):
        for data_item in self.result:
            # Extract information from each item in the "result" list
            rfi_id = data_item['_id']['rfi_id']
            datasource_id = data_item['_id']['data_source_id']
            keyword = data_item['_id']['keyword']
            keyword_type = data_item['keyword_type']
            request_from = data_item['request_from']

            jo_id = data_item['_id'].get('jo_id')
            ip_id = data_item['_id'].get('ip_id')

            # Prepare the payload for the POST request
        payload = {
            "rfi_id": rfi_id,
            "jo_id": jo_id,
            "ip_id": ip_id,
            "datasource_id": datasource_id,
            "group_type": "nfcc",
            "keyword": keyword,
            "keyword_type": keyword_type,
            "request_from": request_from
        }
        for _ in range(6):
            try:
                # Send the POST request
                response = requests.post(
                    self.config["integrationUrl"] +
                    integration_endpoint,
                    data=json.dumps(payload),
                    headers={
                        "Content-type": "application/json",
                        "Accept": "application/json"
                    },
                    verify=False
                )
                # Check the response and print the result
                if response.status_code == 200:
                    print(response.text)
            except Exception:
                print(
                    f"Integration failed for DataSource ID: {datasource_id}, Status code: {response.status_code}, Response: {response.text}")
        return self
