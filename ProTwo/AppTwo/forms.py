from django import forms
from AppTwo.models import Users

class NewuserForm(forms.ModelForm):

    class Meta():
        model = Users
        fields = '__all__'