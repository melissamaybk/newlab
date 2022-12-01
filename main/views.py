from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse
from .models import *
from django.db.models import Q

# Create your views here.
def homepage(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
  contacts = Contact.objects.all()
  form = ContactForm()
  return render(request, "home.html", {"form": form, "contacts":contacts})

def compareName(request):
  if request.method == "POST":
    Similar1 = request.POST.get('Similar1')
    Similar2 = request.POST.get('Similar2')

    contacts= Contact.objects.filter(name__contains=Similar1)
    contacts2= Contact.objects.filter(name__contains=Similar2)
    
    return render(request, "comparename.html", {'Similar1':Similar1, 'contacts':contacts, 'contacts2':contacts2, 'Similar2':Similar2})
  else:
    return render(request, "comparename.html", {})



def searchName(request):
  if request.method == "POST":
    searchname = request.POST.get('searchname')
    contacts= Contact.objects.filter(Q(name__contains=searchname) | Q(mobile__contains=searchname) | Q(telephone__contains=searchname))
    return render(request, "searchnamephone.html", {'searchname':searchname, 'contacts':contacts})
  else:
    return render(request, "searchnamephone.html")

def searchJob(request):
  if request.method == "POST":
    searchjob = request.POST.get('searchjob')
    contacts= Contact.objects.filter(job__contains=searchjob)
    return render(request, "searchjob.html", {'searchjob':searchjob, 'contacts':contacts})
  else:
    return render(request, "searchjob.html", {})


def updateContact(request,pk):

	contact= Contact.objects.get(id=pk)
	form= ContactForm(instance=contact)
	
	if request.method =="POST":
		#print("printing POST:", request.POST)
		form= ContactForm(request.POST, instance=contact)
		if form.is_valid():
			form.save()
			return redirect('/')
	context ={'form':form}
	return render(request, 'home.html',context)