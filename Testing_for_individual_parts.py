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
    "integrationUrl": "http://localhost:3001"
}

reingest = Reingest(mongodb_client, config)
reingest.get_info_from_mongodb()
