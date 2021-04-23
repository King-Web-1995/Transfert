from django.db import models
from django.shortcuts import render, redirect

ligne     	= [('D1','D1'),('D2','D2'),('D3','D3'),('D4','D4'),('D5','D5'),
				('D6','D6'),('D7','D7'),('D8','D8'),('D9','D9'),('D10','D10'),
				('D11','D11'),('D12','D12'),('D13','D13'),('D14','D14'),('D15','D15'),
				('D16','D16'),('D17','D17'),('D18','D18'),('D19','D19'),('D20','D20'),
				('D21','D21'),('D22','D22'),('D23','D23'),('D24','D24'),('D25','D25'),
				('D26','D26'),('D27','D27'),('D28','D28'),('D29','D29'),('D30','D30'),
				('D31','D31'),('D32','D32'),('D33','D33'),('D34','D34'),('D35','D35'),
				('D36','D36'),('D37','D37'),('D38','D38'),('D39','D39'),('D40','D40'),
				('D41','D41'),('D42','D42'),('D43','D43'),('D44','D44'),('D45','D45'),
				('D46','D46'),('D47','D47'),('D48','D48'),('D49','D49'),('D50','D50'),
				('D51','D51'),('D52','D52'),('D53','D53'),('D54','D54'),('D55','D55')]

class Transfert(models.Model):

    numer   	=	models.CharField(max_length=25, unique=True,verbose_name="Numéro de Transfert")
    lumbu		=	models.DateTimeField(auto_now_add=True, verbose_name="Date et Heure de Transfert")
    bonguo		=	models.DecimalField(max_digits=19, decimal_places=5, verbose_name="Montant à Transférer")
    cbonguo		=	models.DecimalField(max_digits=19, decimal_places=5, verbose_name="Confirmation Montant")
    def __str__(self):
    	return self.numer

    def numero(self):

    		total = Transfert.objects.all().last()
    		if total:
    			self.numer 	= "TSRF "+str(total.id + 1)
    		else:
    			self.numer 	= "TSRF "+str(1)

    	

    def save(self,*args, **kwargs):

    	if not self.id:

	    	self.numero()

	    	if self.bonguo != self.cbonguo:

	    		return None

	    	else:

	    		self.bonguo		= self.bonguo
	    		self.cbonguo	= self.cbonguo

	    		super().save(*args, **kwargs)
	    		return True

	

class Retrait(models.Model):
	
	numer   	=	models.CharField(max_length=25, unique=True,verbose_name="Numéro de Retrait")
	lumbu		=	models.DateTimeField(auto_now_add=True, verbose_name="Date et Heure de Retrait")
	bonguo		=	models.DecimalField(max_digits=19, decimal_places=5, verbose_name="Montant à Retirer")
	cbonguo		=	models.DecimalField(max_digits=19, decimal_places=5, verbose_name="Confirmation Montant")
	def __str__(self):
		return self.numer

	def numero(self):

		total = Retrait.objects.all().last()
		if total:
			self.numer 	= "RETA "+str(total.id + 1)
		else:
			self.numer 	= "RETA "+str(1)

		

	def save(self,*args, **kwargs):
		
		self.numero()
		if self.bonguo == self.cbonguo:
			self.bonguo		= self.bonguo
			self.cbonguo	= self.cbonguo

			super().save(*args, **kwargs)
			return True

		else:
			return None


class Depot(models.Model):
	
	numer   	=	models.CharField(max_length=25, unique=True,verbose_name="Numéro de Dépôt")
	lumbu		=	models.DateTimeField(auto_now_add=True, verbose_name="Date et Heure de Dépôt")
	bonguo		=	models.DecimalField(max_digits=19, decimal_places=5, verbose_name="Montant à Dépôt")
	cbonguo		=	models.DecimalField(max_digits=19, decimal_places=5, verbose_name="Confirmation Montant")
	def __str__(self):
		return self.numer

	def numero(self):

		total = Depot.objects.all().last()
		if total:
			self.numer 	= "DEPT "+str(total.id + 1)
		else:
			self.numer 	= "DEPT "+str(1)

		

	def save(self,*args, **kwargs):
		
		self.numero()
		if self.bonguo == self.cbonguo:
			self.bonguo		= self.bonguo
			self.cbonguo	= self.cbonguo

			super().save(*args, **kwargs)
			return True

		else:
			return None

		

class Depense(models.Model):

	numer   	=	models.CharField(max_length=25, unique=True,verbose_name="Numéro de Dépense")
	lumbu		=	models.DateTimeField(auto_now_add=True, verbose_name="Date et Heure de Dépense")
	benun		=	models.CharField(max_length=25, verbose_name="Benificiaire")
	lettre		=	models.CharField(max_length=55, verbose_name="Montant en lettre")
	partdeux	=	models.DecimalField(max_digits=19, decimal_places=5, verbose_name="Montant de Dépense")
	likambom	=	models.CharField(max_length=255, verbose_name="Motif de Dépense")
	cpartdeux	=	models.DecimalField(max_digits=19, decimal_places=5, verbose_name="Confirmation Montant")
	lignebuget	=	models.CharField(max_length=4,choices=ligne,default='S1', verbose_name="Ligne Budgétaire")
	
	def __str__(self):
		return self.numer



	def numero(self):

		total = Depense.objects.all().last()
		if total:
			self.numer 	= "DPSE "+str(total.id + 1)
		else:
			self.numer 	= "DPSE "+str(1)


	def save(self,*args, **kwargs):
		
		self.numero()
		if self.partdeux == self.cpartdeux:
			self.partdeux	= 	self.partdeux
			self.cpartdeux	= 	self.cpartdeux

			super().save(*args, **kwargs)
			return True

		else:
			return None
