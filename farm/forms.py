from django import forms
from .models import login,farmer,research_agro,drone_operator,kvk,warehouse,registration

class loginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = "__all__"

class farmerForm(forms.ModelForm):
    class Meta:
        model = farmer
        fields = "__all__"

class research_agroForm(forms.ModelForm):
    class Meta:
        model = research_agro
        fields = "__all__"

class drone_operatorForm(forms.ModelForm):
    class Meta:
        model = drone_operator
        fields = "__all__"

class kvkForm(forms.ModelForm):
    class Meta:
        model = kvk
        fields = "__all__"

class warehouseForm(forms.ModelForm):
    class Meta:
        model = warehouse
        fields = "__all__"

class registrationForm(forms.ModelForm):
    class Meta:
        model = registration
        fields = "__all__"