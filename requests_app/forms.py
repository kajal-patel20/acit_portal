from django import forms
from .models import AssetRequest

class AssetRequestForm(forms.ModelForm):

    required_by_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
        label="Required By Date"
    )

    class Meta:
        model = AssetRequest
        fields = ['product', 'asset_price', 'tentative_vendor', 'required_by_date', 'quantity', 'description']
        
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Laptop, Projector, etc.'}),
            'asset_price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Asset Price'}),
            'tentative_vendor': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Tentative Vendor'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Quantity', 'min': 1}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Description (optional)', 'rows': 3}),
        }
