from django import forms
from .models import RestaurantLocation
from .validators import validate_category

#for the function based view
class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if name == 'hello':
    #         raise forms.ValidationError('Not a valid name')
    #     return name    

#for the class based view
class RestaurantLocationCreateForm(forms.ModelForm):
    #email = forms.EmailField()
    # you can add the validators here or in the model
    # category = forms.CharField(required=False,validators=[validate_category])

    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category'
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'hello':
            raise forms.ValidationError('Not a valid name')
        return name

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if '.edu' in email:
    #         raise forms.ValidationError('we do not accept edu emails')
    #     return email