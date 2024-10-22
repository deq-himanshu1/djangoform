from django import forms
from .models import UserProfile, Address

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address', 'is_default']
