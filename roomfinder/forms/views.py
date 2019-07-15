from django.shortcuts import render

from forms.models import RenterForm,LandlordForm
# Create your views here.
def renter_view(request):
	if request.method == "POST":
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		print(password)
		re_password = request.POST.get('re_password')
		print(re_password)
		gender = request.POST.get('gender')
		if ((first_name == '')|(last_name == '')|(email == '')|(password == '')|(re_password == '')|(gender == '')):
			print("null")
		elif password == re_password:
			RenterForm.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,gender=gender)
			print("succesfull")
	return render(request,'renterform/renterform.html')

def landlord_view(request):
	if request.method == "POST":
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		gender = request.POST.get('gender')
		if password == re_password:
			LandlordForm.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,gender=gender)
	return render(request,'landlordform/landlordform.html')