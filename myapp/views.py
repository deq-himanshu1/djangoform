from django.shortcuts import render, redirect

# Create your views here.

from .forms import UserProfileForm



def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to the user_profile page
    else:
        form = UserProfileForm()
    return render(request, 'myapp/user.html', {'form': form})
def success_view(request):
    return render(request, 'myapp/success.html')