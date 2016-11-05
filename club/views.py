from django.shortcuts import render

import sendgrid
import os

def index(request):
	return render(request, "index.html")

def contact(request):
	sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
	data = {
		"personalizations": [{
				"to": [{"email": "jes3cu@virginia.edu"}],
				"subject": "Hello World from the SendGrid Python Library!"
			}],
		"from": {"email": "jes3cu@virginia.edu"},
		"content": [{
				"type": "text/plain",
				"value": "Hello, Email!"
		}]
	}
	response = sg.client.mail.send.post(request_body=data)
	print(response.status_code)
	print(response.body)
	print(response.headers)
	return render(request, "contact.html")
