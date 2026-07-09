from django.shortcuts import render
from django.contrib import messages
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return render(request, 'accounts/login.html')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
