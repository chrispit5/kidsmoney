from django import forms

from .models import Expenses


class DateInputCJP(forms.DateInput):
	input_type = 'date'


class ExpenseForm(forms.ModelForm):
	item = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'item'
		}))
	amount = forms.IntegerField(widget=forms.NumberInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'amount'
		}))
	exdate = forms.DateField(widget=DateInputCJP)
	class Meta:
		model = Expenses
		fields = [
			'name',
			'item',
			'amount',
			'exdate'
			]
	
