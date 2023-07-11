
from datetime import datetime, timedelta
import requests
import json


class YourClass:
    def __init__(self):
        self.config = {"integrationUrl": "http://localhost:3001/"}
        self.result_2 = [{'_id': {'keyword': 'PQR555', 'rfi_id': '8579', 'data_source_id': '64759832a192c9757f232b06'},
                          'keyword_type': 'CarPlatePipeline', 'request_from': '780313199993', 'status': 2, 'retry_count': 3, 'sla_datetime': datetime.datetime(2023, 1, 17, 18, 33, 45), '_class': 'org.nfcc.nfis.integration.model.ProblemDataModel'},
                         {'_id': {'keyword': 'MAD4227', 'rfi_id': '8579', 'data_source_id': '841bffgt345398d6f7330'},
                          'keyword_type': 'CarPlatePipeline', 'request_from': '780313199993', 'status': 2, 'retry_count': 3, 'sla_datetime': datetime.datetime(2023, 1, 17, 18, 33, 45), '_class': 'org.nfcc.nfis.integration.model.ProblemDataModel'},
                         {'_id': {'keyword': 'ABC123', 'rfi_id': '8579', 'jo_id': 'JO202300001', 'ïp_id': 'IPID', 'data_source_id': '632bfc5dbc2aef398d6f7914'},
                          'keyword_type': 'CarPlatePipeline', 'request_from': '780313199993', 'status': 2, 'retry_count': 3, 'sla_datetime': datetime.datetime(2023, 1, 17, 18, 33, 45), '_class': 'org.nfcc.nfis.integration.model.ProblemDataModel'},
                         {'_id': {'keyword': 'MYD892', 'rfi_id': '8579', 'data_source_id': '64759832a192c9757f232b06'},
                          'keyword_type': 'CarPlatePipeline', 'request_from': '780313199993', 'status': 2, 'retry_count': 3, 'sla_datetime': datetime.datetime(2023, 1, 17, 18, 33, 45), '_class': 'org.nfcc.nfis.integration.model.ProblemDataModel'},
                         {'_id': {'keyword': 'YTK3452', 'rfi_id': '8579', 'data_source_id': '64759832a192c9757f232b06'},
                          'keyword_type': 'CarPoopPipeline', 'request_from': '780313199993', 'status': 2, 'retry_count': 3, 'sla_datetime': datetime.datetime(2023, 1, 17, 18, 33, 45), '_class': 'org.nfcc.nfis.integration.model.ProblemDataModel'}]

    def trigger_nfis_integration2(self, integration_endpoint):
        rfi_id = self.result_2["_id"]["rfi_id"]
        datasource_id = self.result_2["_id"]["data_source_id"]
        keyword = self.result_2["_id"]["keyword"]
        keyword_type = self.result_2["keyword_type"]
        request_from = self.result_2["request_from"]

        sla_datetime = self.result_2["sla_datetime"]

        jo_id = self.result_2["_id"].get("jo_id")
        ip_id = self.result_2["_id"].get("ip_id")

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

        current_datetime = sla_datetime - timedelta(days=2)

        if current_datetime < sla_datetime:
            for _ in range(6):
                try:
                    response = requests.post(
                        self.config["integrationUrl"] + integration_endpoint,
                        data=json.dumps(payload),
                        headers={
                            "Content-type": "application/json",
                            "Accept": "application/json"
                        },
                        verify=False
                    )

                    if response.status_code == 200:
                        break
                    else:
                        print(
                            f"Integration failed for DataSource ID: {datasource_id}, Status code: {response.status_code}, Response: {response.text}")

                except Exception as e:
                    print("Error occurred while sending the POST request:", str(e))
        else:
            print("SLA datetime not reached. Skipping integration.")

        return self


# Example usage
your_instance = YourClass()
your_instance.trigger_nfis_integration2("api/v1/integration/agency")
