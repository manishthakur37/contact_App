from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


# Create your views here.

def IndexPage(request):
	ContactList = Contact.objects.all()
	contact=Contact.objects.filter(full_name__contains='search-area')
	context = {
		'ContactList':ContactList,
	}
	return render(request,'core/index.html',context)


def AddPage(request):
	if request.method == 'POST':
		full_name = request.POST['fullname']
		relationship = request.POST['relationship']
		email = request.POST['e-mail']
		phone_number = request.POST['phone-number']
		address = request.POST['address']
		ContactAdd=Contact(full_name=full_name,relationship=relationship,email=email,phone_number=phone_number,address=address)
		ContactAdd.save()
		return redirect('/')
	return render(request,'core/add.html')


def ContactProfile(request, pk):
	contact = Contact.objects.get(id=pk)
	return render(request,'core/contact-profile.html',{'contact':contact})


def EditPage(request, pk):
	contact = Contact.objects.get(id=pk)
	if request.method == 'POST':
		full_name = request.POST.get('fullname')
		relationship = request.POST.get('relationship')
		email = request.POST.get('e-mail')
		phone_number = request.POST.get('phone-number')
		address = request.POST.get('address')
		contact.full_name=full_name
		contact.relationship=relationship
		contact.email=email
		contact.phone_number=phone_number
		contact.address=address
		contact.save()
		return redirect('/')	
	return render(request,'core/edit.html',{'contact':contact})

def DeletePage(request, pk):
	contact = Contact.objects.get(id=pk)
	if request.method == 'POST':
		contact.delete()
		return redirect('/')
	return render(request,'core/delete.html',{'contact':contact})
