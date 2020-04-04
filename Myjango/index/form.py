from django import forms
from .models import *
class ProductForm(forms.Form):
      name=forms.CharField(max_length=20,label='名字')
      size=forms.CharField(max_length=20,label='尺寸')
      choice_list=[(i+1,v['type']) for i,v in enumerate(Product.objects.values('type'))]
      type=forms.ChoiceField(choices=choice_list,label="类型")