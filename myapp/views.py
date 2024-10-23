from django.shortcuts import render, redirect
from .forms import UserProfileForm, AddressForm
from .models import UserProfile, Address

def user_profile_view(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST)
        address_form = AddressForm(request.POST)

        if user_form.is_valid() and address_form.is_valid():
            user_profile = user_form.save()  # Save the UserProfile
            address = address_form.save(commit=False)  # Don't save yet
            address.user = user_profile  # Associate the address with the user
            address.save()  # Now save the address

            if address.is_default:
                Address.objects.filter(user=user_profile).exclude(id=address.id).update(is_default=False)

            return redirect('success')  # Redirect to success page
    else:
        user_form = UserProfileForm()
        address_form = AddressForm()

    return render(request, 'frontend/user.html', {'user_form': user_form, 'address_form': address_form})

def success_view(request):
    return render(request, 'frontend/success.html')
