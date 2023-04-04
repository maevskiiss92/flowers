from django import forms

class SimpleForm(forms.Form):
    quantityField = forms.IntegerField(label="Количество")