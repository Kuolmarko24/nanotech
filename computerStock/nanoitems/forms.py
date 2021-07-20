from django import forms
from .models import Product
# from .models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('item','type','quantity','price','specs')