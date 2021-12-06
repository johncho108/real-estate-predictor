from django import forms

class RequiredFeaturesForm(forms.Form):
    bedrooms = forms.IntegerField(label='Number of Bedrooms', widget=forms.NumberInput(attrs={'placeholder': '1 - 20', 'autocomplete':'off'}))
    sqft_living = forms.IntegerField(label='Living Space (Sqft)', widget=forms.NumberInput(attrs={'placeholder': '500 - 100000', 'autocomplete':'off'}))
    grade = forms.IntegerField(label='Quality of Construction', widget=forms.NumberInput(attrs={'placeholder': '1 - 13', 'autocomplete':'off'}))

class OptionalFeaturesForm(forms.Form):
    bathrooms = forms.FloatField(label='Number of Bathrooms', required=False, widget=forms.NumberInput(attrs={'placeholder': '1 - 10', 'autocomplete':'off'}))
    sqft_lot = forms.IntegerField(label='Lot Size (Sqft)', required=False, widget=forms.NumberInput(attrs={'placeholder': '500 - 100000', 'autocomplete':'off'}))
    floors = forms.IntegerField(label='Number of Floors', required=False, widget=forms.NumberInput(attrs={'placeholder': '1 - 10', 'autocomplete':'off'}))
    waterfront = forms.ChoiceField(label='Waterfront', choices=[('',''), ('yes', 'Yes'), ('no', 'No')], required=False)
    view = forms.IntegerField(label='View', required=False, widget=forms.NumberInput(attrs={'placeholder': '0 - 4', 'autocomplete':'off'}))
    condition = forms.IntegerField(label='Current Condition', required=False, widget=forms.NumberInput(attrs={'placeholder': '1 - 5', 'autocomplete':'off'}))
