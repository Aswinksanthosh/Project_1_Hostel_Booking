from dataclasses import fields
from pyexpat import model
from django import forms
from .models import *

class user_reg_valid(forms.ModelForm):      #CREATED A FORM FROM MODEL
    class Meta:
        model=User_registration
        fields=('phno','name','gmail','pwd',)

class login12(forms.ModelForm):
    class Meta:
        model=User_registration           #signup have 5 fields, we need only 2
        fields=('gmail','pwd')              #for inputing only 2 fields

class hostel_add(forms.ModelForm):
    class Meta:
        model=hostels
        # fields=('name','price4','price6','price8','price10','share4','share6','share8','share10','address','phno','img','gmail','desc')
        fields='__all__'


class hostel_all_fields(forms.ModelForm):
    class Meta:
        model = hostels
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if instance is not None:
            self.fields['h_id'].initial = instance.h_id
            self.fields['price4'].initial = instance.price4
            self.fields['price6'].initial = instance.price6
            self.fields['price8'].initial = instance.price8
            self.fields['price10'].initial = instance.price10
            self.fields['name'].initial = instance.name
            self.fields['desc'].initial = instance.desc
            self.fields['rating'].initial = instance.rating
            self.fields['share4'].initial = instance.share4
            self.fields['share6'].initial = instance.share6
            self.fields['share8'].initial = instance.share8
            self.fields['share10'].initial = instance.share10
            self.fields['address'].initial = instance.address
            self.fields['phno'].initial = instance.phno
            self.fields['img'].initial = instance.img
            self.fields['gmail'].initial = instance.gmail
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.h_id = self.cleaned_data['h_id']
        if commit:
            instance.save()
        return instance

class EditForm(forms.ModelForm):
    class Meta:
        model = hostels
        fields = ['price4', 'price6', 'price8', 'price10', 'name', 'desc', 'rating', 'share4', 'share6', 'share8', 'share10', 'address', 'phno', 'img', 'gmail']
        widgets = {'img': forms.ClearableFileInput()}