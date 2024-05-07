from django.shortcuts import render
 

def home(request):
    return render(request, 'home.html')

def contact_success(request):
    return render(request, 'contact_success.html')
# views.py

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
