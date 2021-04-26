from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *




def index(request):
	if request.method == 'POST':
		data = request.POST
		if len(data) == 3 :
			user_auth = authenticate(username=data['username'],password=data['password'])
			if user_auth:
				login(request,user_auth)
				return redirect('home')
	return render(request, 'page/index.html')


def deconnection(request):
	logout(request)
	return redirect('index')


@login_required
def aide(request):
	transferts = Transfert.objects.all()
	return render(request, 'page/aide.html',{'transferts':transferts})

@login_required
def depense(request):
	formulaire	= 	DepenseForm()
	if request.method == 'POST':
		formulaire = DepenseForm(request.POST)
		form= request.POST
		if formulaire.is_valid():
			if form['partdeux'] == form['cpartdeux']:
				formulaire.save()
				messages.success(request,"Opération reuissie avec succé")
				return redirect('home')
			else:
				print("hello")
				messages.error(request, "Problème sur les montants")
	return render(request, 'page/depense.html',{'formulaire':formulaire})


@login_required
def transfert(request):
	formulaire = TransfertForm()
	if request.method == 'POST':
		formulaire = TransfertForm(request.POST)
		form= request.POST
		if formulaire.is_valid():
			if form['cbonguo'] == form['bonguo']:
				formulaire.save()
				messages.success(request,"Opération reuissie avec succé")
				return redirect('home')
			else:
				print("hello")
				messages.error(request, "Problème sur les montants")
	return render(request, 'page/transfert.html',{'formulaire':formulaire})
	

@login_required
def retrait(request):
	formulaire = RetraitForm()
	if request.method == 'POST':
		formulaire = RetraitForm(request.POST)
		form= request.POST
		if formulaire.is_valid():
			if form['cbonguo'] == form['bonguo']:
				formulaire.save()
				messages.success(request,"Opération reuissie avec succé")
				return redirect('home')
			else:
				print("hello")
				messages.error(request, "Problème sur les montants")
	return render(request, 'page/retrait.html',{'formulaire':formulaire})


@login_required
def depot(request):
	formulaire = DepotForm()
	if request.method == 'POST':
		formulaire = DepotForm(request.POST)
		form= request.POST
		if formulaire.is_valid():
			if form['cbonguo'] == form['bonguo']:
				formulaire.save()
				messages.success(request,"Opération reuissie avec succé")
				return redirect('home')
			else:
				print("hello")
				messages.error(request, "Problème sur les montants")
	return render(request, 'page/depot.html',{'formulaire':formulaire})

