from django import forms 
from .models import Bond, BondOther 

class BidForm(forms.ModelForm):
    class Meta:
        model = BondOther
        fields = ('bid',)
        widgets = {
            'bid' : forms.TextInput(
attrs={'class': 'form-control', 'style': 'width: 70%; top:130px; left: 200px;', 'placeholder': 'INPUT YOUR BID'}
),}



class BondForm(forms.ModelForm):

    class Meta:
        model = Bond
        fields = ('company', 'price', 'roe', 'roa', 'debt_eq', 'long_debt_eq')
        widgets = {
            'company': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:130px; left: 200px;', 'placeholder': 'INPUT COMPANY NAME'}
            ),
            'price': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:230px; left: 200px;', 'placeholder': 'INPUT PAR VALUE'}
            ),
            'roe': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:330px; left: 200px;', 'placeholder': 'INPUT COMPANY ROE'}
            ),
            'roa': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:430px; left: 200px;', 'placeholder': 'INPUT COMPANY ROA'}
            ),
            'debt_eq': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:530px; left: 200px;', 'placeholder': 'INPUT COMPANY DEBT/EQ'}
            ),
            'long_debt_eq': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:630px; left: 200px;', 'placeholder': 'INPUT COMPANY LONG TERM DEBT/EQ'}
            ),
        }


class SellForm(forms.ModelForm):

    class Meta:
        model = Bond 
        fields = ('minprice',)
        widgets = {
            'price': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:130px; left: 200px;', 'placeholder': 'INPUT MIN PRICE'}
            ),}
