from django.shortcuts import render
from .forms import *
import sendgrid
import os

def index(request):
	return render(request, "index.html")

def contact(request):
	response = None
	if request.method == "GET":
		form = ContactForm()
	else:
		form = ContactForm(data=request.POST)
		if form.is_valid():
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			email_subject = form.cleaned_data['email_subject']
			content = form.cleaned_data['content']

			sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
			data = {
				"personalizations": [{
						"to": [{"email": "jes3cu@virginia.edu"}],
						"subject": email_subject
					}],
				"from": {"email": contact_email},
				"content": [{
						"type": "text/plain",
						"value": content
				}]
			}
			response = sg.client.mail.send.post(request_body=data)
			form = ContactForm()
	return render(request, "contact.html", {'form':form, 'email_sent':response})
