from django import forms 
from .models import Bond 

class BondForm(forms.ModelForm):

    class Meta:
        model = Bond
        fields = ('company', 'price', 'roe', 'roa', 'debt_eq', 'long_debt_eq')
        widgets = {
            'company': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:130px; left: 200px;', 'placeholder': '기업명을 입력하세요.'}
            ),
            'price': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:230px; left: 200px;', 'placeholder': '채권가액을 입력하세요.'}
            ),
            'roe': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:330px; left: 200px;', 'placeholder': 'roe를 입력하세요.'}
            ),
            'roa': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:430px; left: 200px;', 'placeholder': 'roa를 입력하세요.'}
            ),
            'debt_eq': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:530px; left: 200px;', 'placeholder': '자산채무비율을 입력하세요.'}
            ),
            'long_debt_eq': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:630px; left: 200px;', 'placeholder': '장기자산채무비율을 입력하세요.'}
            ),
        }


class SellForm(forms.ModelForm):

    class Meta:
        model = Bond 
        fields = ('price',)
        widgets = {
            'price': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 70%; top:130px; left: 200px;', 'placeholder': '최소가격을 입력하세요'}
            ),}
