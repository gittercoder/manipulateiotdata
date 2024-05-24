# iot/forms.py
from django import forms

class DynamicDataForm(forms.Form):
    pass  # No fixed fields, will be handled dynamically in the template