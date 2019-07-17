from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# now = timezone.now()
def home(request):
   return render(request, 'mytrip/home.html',
                 {'mytrip': home})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'mytrip/register_done.html', {'new_user': new_user})
    else:
      user_form = UserRegistrationForm()
      return render(request, 'mytrip/register.html', {'user_form': user_form})
