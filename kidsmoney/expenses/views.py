from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Sum
from django import forms


from .forms import ExpenseForm
from .models import Expenses
from .models import Person
from django.contrib.auth.decorators import permission_required

@permission_required('expenses.view_person')
def home(request):
	page_title = 'Current Balance'
	expense = Person.objects.annotate((Sum('expenses__amount')))
	return render(request, 'home.html', {'expense': expense, 'page_title':page_title})

@permission_required('expenses.view_expenses')
def expense_detail(request, id):
	page_title = 'Expense Details'
	expense = Expenses.objects.filter(name_id=id)

	return render(request, 'expense_detail.html', {'expense': expense, 'page_title':page_title})

@permission_required('expenses.view_expenses')
def delete_expense(request, id):
	page_title = 'Delete Expense'
	expense = get_object_or_404(Expenses, id=id)
	key_id = expense.name_id
	print('I am here 1')
	if request.method == "POST":
		print('about to delete')

		expense.delete()
		return redirect('expense_detail', id=key_id)
	context = {
		"expense": expense
	}
	print('about to return')
	return render(request, "delete_expense.html", context)


@permission_required('expenses.view_expenses')
def add_expense(request, id):
	page_title = 'Add Expense'

	#init_name = { "name" : Expenses.objects.filter(Personname=id), "item" : "blalkkkllh"}
	form = ExpenseForm(request.POST or None, initial ={'name': id})
	if form.is_valid():
		expense = form
		form.save()
		form = ExpenseForm(request.POST or None)

	context = {
		'form': form,
		'page_title': page_title
	}
	return render(request, "add_expense.html", context)



