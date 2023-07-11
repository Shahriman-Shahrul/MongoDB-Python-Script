
from unittest.mock import patch, MagicMock
import unittest
from EmailTrial.collect_keyword_send_email import Compiler
from EmailTrial.Reingest import Reingest
import pymongo


# Connect to MongoDB
mongodb_client = pymongo.MongoClient("mongodb://localhost:27017")

# Define the configuration
config = {
    "emailAddress": {
        "64759832a192c9757f232b06": "spectacular32shah@gmail.com",
        "841bffgt345398d6f7330": "spectacular32shah@gmail.com",
        "smtpServer": "smtp.gmail.com",
        "smtpPort": 465,
        "smtpUsername": "shahriman.shahrul@kewmann.com",
        "smtpPassword": "hvugnvvwwsppuzsh",
    },
    "mongodb": {
        "mongodbHost": "pnpc-dahlia1.nfcc.gov.my",
        "mongodbHost2": "pnpc-dahlia2.nfcc.gov.my",
        "mongodbPort": "27012",
        "dbName": "nfis",
        "mongodbUsername": "nfisMongo",
        "mongodbPassword": "Nfis@prod222",
        "ssl": "True",
        "caFile": "/home/rootadmin/spark_projects/certs/ca.pem",
        "certFile": "/home/rootadmin/spark_projects/certs/nfcc.gov.my.pem"
    },
    "integrationUrl": "http://localhost:3001/"
}

# Step 1 : Compiler

# compiler = Compiler(mongodb_client, config)
# compiler.check_mongodb().send_email()

# Step 2 : Reingest

reingest = Reingest(mongodb_client, config)
reingest.get_info_from_mongodb()
reingest.trigger_nfis_integration("api/v1/integration/agency")


################################

# # Sample data to use for testing
# sample_data = [
#     {'_id': {'keyword': 'PQR555', 'rfi_id': '8579', 'data_source_id': '64759832a192c9757f232b06'},
#         'keyword_type': 'CarPlatePipeline', 'request_from': '780313199993', 'status': 2,
#         'retry_count': 3, 'sla_datetime': '2023-01-17T18:33:45.000+00:00',
#         '_class': 'org.nfcc.nfis.integration.model.ProblemDataModel'},
#     {'_id': {'keyword': 'MAD4227', 'rfi_id': '8579', 'data_source_id': '841bffgt345398d6f7330'},
#         'keyword_type': 'CarPlatePipeline', 'request_from': '780313199993', 'status': 2,
#         'retry_count': 3, 'sla_datetime': '2023-01-17T18:33:45.000+00:00',
#         '_class': 'org.nfcc.nfis.integration.model.ProblemDataModel'},
#     {'_id': {'keyword': 'ABC123', 'rfi_id': '8579', 'data_source_id': '841bffgt345398d6f7330'},
#         'keyword_type': 'CarPlatePipeline', 'request_from': '780313199993', 'status': 2,
#         'retry_count': 3, 'sla_datetime': '2023-01-17T18:33:45.000+00:00',
#         '_class': 'org.nfcc.nfis.integration.model.ProblemDataModel'},
#     {'_id': {'keyword': 'MYD892', 'rfi_id': '8579', 'data_source_id': '64759832a192c9757f232b06'},
#         'keyword_type': 'CarPlatePipeline', 'request_from': '780313199993', 'status': 2,
#         'retry_count': 3, 'sla_datetime': '2023-01-17T18:33:45.000+00:00',
#         '_class': 'org.nfcc.nfis.integration.model.ProblemDataModel'}
# ]


# class TestReingest2(unittest.TestCase):

#     def test_get_info_from_mongodb(self):
# Create a mock MongoDB client
# mock_mongodb_client = MagicMock()

# Create a mock collection
# mock_collection = MagicMock()

# Set the return value of collection.find to our sample data
#mock_collection.find.return_value = sample_data

# Set the "nfis.problem_data" attribute of the mock MongoDB client to our mock collection
#mock_mongodb_client.nfis.problem_data = mock_collection

# Create an instance of the Reingest2 class with the mock MongoDB client
# reingest = Reingest2(mock_mongodb_client, {})

#         # Call the get_info_from_mongodb method
#         result = reingest.get_info_from_mongodb()

#         # Check if the method returns the correct instance of the Reingest2 class
#         self.assertIs(result, reingest)

#         # Check if the datasource_ids and keyword_dict attributes are set correctly
#         self.assertEqual(reingest.datasource_ids, [
#                          '64759832a192c9757f232b06', '841bffgt345398d6f7330'])
#         self.assertEqual(reingest.keyword_dict, {
#             '64759832a192c9757f232b06': {'PQR555', 'MYD892'},
#             '841bffgt345398d6f7330': {'MAD4227', 'ABC123'}
#         })


# if __name__ == '__main__':
#     unittest.main()


# TestReingest2()

################################################################################################
