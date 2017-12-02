import requests
import json
import time
import sendgrid
import os

from sendgrid.helpers.mail  import Email, Content, Mail

from celery                 import shared_task

from django.core.exceptions import ObjectDoesNotExist
 
from .models                import Rule, Alert


@shared_task
def Cryptobot(currencie_name):
    try:
        headers = {'CB-VERSION': time.strftime("%Y-%m-%d")}
        rule = Rule.objects.get(currencie=currencie_name)
        r = requests.get("https://api.coinbase.com/v2/prices/" + "BTC-" + currencie_name + "/spot", headers=headers)
        # We check if the currencie exist
        if r.status_code < 200 or r.status_code >= 300:
            print("coinbase don't know this currencie here the full message.")
            print(r.json())
        else:
            amount = float(r.json()['data']['amount'])
            print(amount)
            # If the value in under the minimum or upper the maximum we send a mail and create an alert
            if rule.value_min is not None and rule.value_min > amount or rule.value_max is not None and rule.value_max < amount:
                # Configure sendgrid to send mail
                sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
                from_email = Email("test@example.com")
                # !!!! Change email here for test !!!!
                to_email = Email("test@test.com")
                subject = "An Alert have been raise"
                content = Content("text/plain", "An Alert have been raise, the bitcoin is under/upper " + str(amount))
                mail = Mail(from_email, subject, to_email, content)
                response = sg.client.mail.send.post(request_body=mail.get())
                # We check if the mail have been send
                if response.status_code < 200 or response.status_code >= 300:
                    Alert.objects.create(message="Sending the mail have fail", currencie=currencie_name)
                else:
                    Alert.objects.create(message=content, currencie=currencie_name)
            # we launch the task after 5 second if everything work
            Cryptobot.apply_async((currencie_name,), countdown=5)
    except ObjectDoesNotExist:
        print("There is no rule for " + currencie_name + " go to http://127.0.0.1:8000/crypto/rules/ to create one, and name the currencie with one of the currencie you can see with python3 manage.py currencie_list")

@shared_task
def Currencie_List():
    reponse = requests.get("https://api.coinbase.com/v2/currencies")
    for currencies in reponse.json()['data']:
        print (currencies['id'])
