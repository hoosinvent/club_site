from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mass_mail
from django.db.models import Q

def index(request):
	return render(request, "index.html")