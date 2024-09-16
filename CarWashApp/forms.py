from django import forms
from .models import CarWash, Owner, Compliance, Location, Joining

class CarWashForm(forms.ModelForm):
    class Meta:
        model = CarWash
        fields = ['NM_Number', 'CarWashName', 'RegisteredBusinessName', 'RegistrationNo']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['OwnerNameSurname', 'OwnerIDNumber', 'ContactNumber', 'EmailAddress']

class ComplianceForm(forms.ModelForm):
    class Meta:
        model = Compliance
        fields = ['CIPC', 'BusinessBankAccount', 'SARS_PIN', 'Ownership']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['PhysicalAddress', 'GPSCoordinates', 'CityTownship', 'Province']

class JoiningForm(forms.ModelForm):
    class Meta:
        model = Joining
        fields = ['JoiningDate']

