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

def project(request):
	return render(request, "project.html")

def adroit(request):
	title = "ADROIT Assistive Device"
	picture = "Picture Here"
	abstract = "Lorem ipsum dolor sit amet, ad eam dicat simul eligendi, ei malorum probatus eam. Feugiat accusamus scripserit mel id. Et usu quidam maluisset. Cum persius feugait detracto in. Ius quaeque accusam appetere et, et mei quem habemus, quo ponderum vivendum ea. Ut mea facilis volutpat constituto, et sea lucilius consequuntur, essent facilisi dissentiet cum ex.  Sit dolor iriure no, vim choro praesent ex. No option saperet lucilius has. Omnes persius patrioque duo ut. Ad vel discere perfecto imperdiet, at est unum prima possit. At ius melius albucius insolens, ne utroque percipitur pro, nominavi ponderum eu ius. Eam id debet detracto principes, falli aeque constituto eam te, per te clita altera."
	team_members = {'John Doe':'jd9pp', 'Foo Bar':'fb2al'}
	readings = ['Wiki', 'Other']
	return render(request, "project.html", {'title':title, 'picture':picture, 'abstract':abstract, 'team_members':team_members, 'readings':readings})

def wheels(request):
	title = "Automated Training Wheels"
	picture = "Picture Here"
	abstract = "Lorem ipsum dolor sit amet, everti sensibus quo ut, an brute corrumpit usu. Ad augue ceteros usu, omnis tempor et eos. No has prima autem petentium, his dicant aeterno nominati in. Per ei molestie torquatos, vis suas timeam consulatu ei. Quo congue sententiae an, wisi debet liberavisse no vel.  Habeo suavitate dissentiet no sed. Vim minim epicurei partiendo ei, has ne sapientem consectetuer. At posse legimus sit, quo ei maluisset ullamcorper, velit nonumy eum in. Ius mutat doctus ea, his ex vidisse perpetua maiestatis, an nec albucius scaevola vivendum. Natum tation sensibus ea mel."
	team_members = {'Guy Fieri':'gf2el', 'Jackson Galaxy':'jg7ug'}
	readings = ['Wiki', 'More']
	return render(request, "project.html", {'title':title, 'picture':picture, 'abstract':abstract, 'team_members':team_members, 'readings':readings})

def laser(request):
	title = "Laser Line Shield"
	picture = "Picture Here"
	abstract = "Vocent phaedrum ei vis. Cum quaestio expetendis scribentur in, ipsum eloquentiam ut eam. Ea his oratio suavitate. Iudicabit accommodare ne sed, indoctum torquatos te cum, stet maiorum ex nam. In falli sadipscing nec, vis an tale sonet eloquentiam, numquam legimus vel te. Mutat inani interpretaris sea te, mei ut rebum populo tritani, tibique oportere reprimique ius ad.  Fuisset lucilius ex sed, cu animal nominati delicata vel. Qui suas nobis munere id, te vis enim case, te per dicit facilis. Reque assentior in eam, at porro definiebas usu. Duo id inani platonem posidonium, dolor mollis qualisque duo ex. Impetus eripuit suscipiantur ne sed, ad movet paulo deleniti ius. Ex diam quidam quo."
	team_members = {'This Guy':'tg3gt', 'That Girl':'gt4tg'}
	readings = ['Wiki', 'Reading']
	return render(request, "project.html", {'title':title, 'picture':picture, 'abstract':abstract, 'team_members':team_members, 'readings':readings})

def sound(request):
	title = "Sound Wave Module"
	picture = "Picture Here"
	abstract = "Lorem ipsum dolor sit amet, denique rationibus mei ad. Eam te melius latine atomorum. Harum oratio forensibus ad eam. Et his tamquam numquam, ei nihil populo altera usu.  Vim ne congue utroque, ipsum verear ne eum. Eu congue democritum cum, enim luptatum ex has. Veri minim nec in. Nonumy mandamus eu vis, quo in qualisque laboramus. Eleifend cotidieque vituperatoribus ut eos, ne eam dicant explicari."
	team_members = {'He Is':'hi7ae', 'She Is':'si8rt'}
	readings = ['Wiki', 'Him']
	return render(request, "project.html", {'title':title, 'picture':picture, 'abstract':abstract, 'team_members':team_members, 'readings':readings})
