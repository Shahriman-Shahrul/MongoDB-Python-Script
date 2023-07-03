import smtplib
from email.message import EmailMessage


class Compiler:
    def __init__(self, mongodb_client, config):
        self.mongodb_client = mongodb_client
        self.config = config
        self.datasource_ids = []
        self.keyword_dict = {}

    def check_mongodb(self):
        # Step 1: Collect the keywords
        collection = self.mongodb_client.NFCC.problem_data  # Change to Problem_data
        result = list(collection.find({"status": 1}))

        keyword_dict = {}

        for d in result:
            datasource_id = d["_id"]["data_source_id"]
            keyword = d["_id"]["keyword"]

            if datasource_id not in keyword_dict:
                keyword_dict[datasource_id] = set()
            keyword_dict[datasource_id].add(keyword)

        # Step 2: Collect the Data_source_id
        self.datasource_ids = list(keyword_dict.keys())

        # Update the status of collected keywords to 2
        #collection.update_many({"status": 1}, {"$set": {"status": 2}})

        self.keyword_dict = keyword_dict
        print(keyword_dict)
        return self

    def send_email(self):
        # Step 3: Send the DataSource ID with keywords to the email addresses stored in the config

        email_subject = "Keyword List"
        email_sender = self.config["emailAddress"]["smtpUsername"]
        ######## In case of Missing email for datasource_id #############
        for datasource_id in self.keyword_dict:
            try:
                email_recipient = self.config["emailAddress"][datasource_id]
            except KeyError:
                print(
                    f"No email address found for DataSource ID: {datasource_id}")
                continue
        ############ Sending the email #########
        for datasource_id in self.keyword_dict:
            email_recipient = self.config["emailAddress"].get(datasource_id)
            if email_recipient:
                #keywords = list(keywords_set)
                keywords = self.keyword_dict[datasource_id]
                email_body = f"DataSource ID: {datasource_id}\nKeywords: {', '.join(keywords)}"
                msg = EmailMessage()
                msg.set_content(email_body)
                msg['Subject'] = email_subject
                msg['From'] = email_sender
                msg['To'] = email_recipient

                try:
                    with smtplib.SMTP_SSL(self.config["emailAddress"]["smtpServer"], self.config["emailAddress"]["smtpPort"]) as smtp:
                        smtp.login(self.config["emailAddress"]["smtpUsername"],
                                   self.config["emailAddress"]["smtpPassword"])
                        smtp.send_message(msg)
                        print("Email sent successfully.")

                except Exception as e:
                    print("Error occurred while sending the email:", str(e))
        return self
