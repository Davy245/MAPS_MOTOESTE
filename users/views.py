from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from .forms import AuthForm, Moto_taxi_forms, Cliente_forms
from googleMaps.mixins import RedirectParams

# Create your views here.


class SignUpView(FormView):
	'''
	Generic FormView with our mixin for user sign-up with reCAPTURE security
	'''

	template_name = "users/sign_up.html"
	form_class = Cliente_forms
	success_url = "/"


	#over write the mixin logic to get, check and save reCAPTURE score
	def form_valid(self, form):
			
		obj = form.save()
		obj.save()
		up = obj.userprofile
		up.save()
		login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')
		#change result & message on success
		result = "Success"
		message = "Thank you for signing up"
		
		data = {'result': result, 'message': message}
		return JsonResponse(data)

		
class SignInView(FormView):
	'''
	Generic FormView with our mixin for user sign-in
	'''

	template_name = "users/sign_in.html"
	form_class = AuthForm
	success_url = "/"

	def form_valid(self, form):
		
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		#attempt to authenticate user
		user = authenticate(self.request, username=username, password=password)
		if user is not None:
			login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
			result = "Success"
			message = 'You are now logged in'
		

def sign_out(request):
	'''
	Basic view for user sign out
	'''
	logout(request)
	return redirect(reverse('users:sign-in'))
