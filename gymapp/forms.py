from django import forms
from .models import user_contact

class contact_model(forms.ModelForm):
    class Meta:
        model=user_contact
        fields='__all__'

