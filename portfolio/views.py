def achievements(request):
	return render(request, 'portfolio/achievements.html')


from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
	return render(request, 'portfolio/home.html')

def skills(request):
	return render(request, 'portfolio/skills.html')

def projects(request):
	return render(request, 'portfolio/projects.html')

def feedback(request):
	sent = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			subject = f"Portfolio Contact from {name} ({email})"
			body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
			send_mail(
				subject,
				body,
				email,  # from email
				['rangurahul98@gmail.com'],  # to email
			)
			sent = True
	else:
		form = ContactForm()
	return render(request, 'portfolio/feedback.html', {'form': form, 'sent': sent})
