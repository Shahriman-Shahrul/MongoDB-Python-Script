
from NFIS_email_trial.collect_keyword_send_email import Compiler
from NFIS_email_trial.reingest import Reingest
import pymongo


# Connect to MongoDB
# mongodb_client = pymongo.MongoClient("mongodb://localhost:27017")

# Define the connection parameters
host = 'pndc-dahlia1.nfcc.gov.my'
port = 27017
username = 'nfisMongo'
password = 'Nfis@dev2022'
auth_source = 'admin'  # If you need to specify an authentication database

# Create the MongoClient
mongodb_client = pymongo.MongoClient(host=host, port=port,
                                     username=username, password=password,
                                     authSource=auth_source)
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

compiler = Compiler(mongodb_client, config)
compiler.check_mongodb().send_email()

# Step 2 : Reingest

reingest = Reingest(mongodb_client, config)
reingest.get_info_from_mongodb()
reingest.trigger_nfis_integration2("api/v1/integration/agency")
