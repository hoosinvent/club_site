from django.shortcuts import render
from .forms import *
import sendgrid
import os

def index(request):
	return render(request, "index.html")

def contact(request):
	if request.method == "GET":
		form = ContactForm()
	else:
		form = ContactForm(data=request.POST)
		if form.is_valid():
			contact_name = form.cleand_data['contact_name']
			contact_email = form.cleand_data['contact_email']
			content = form.cleaned_data['content']

			sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
			data = {
				"personalizations": [{
						"to": [{"email": "jes3cu@virginia.edu"}],
						"subject": "Hello World from the SendGrid Python Library!"
					}],
				"from": {"email": contact_email},
				"content": [{
						"type": "text/plain",
						"value": content
				}]
			}
			response = sg.client.mail.send.post(request_body=data)
	return render(request, "contact.html", {'form':form})
