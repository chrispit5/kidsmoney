from django.contrib import admin

from expenses.models import Expenses, Person


@admin.register(Expenses)
class Expenese(admin.ModelAdmin):
	pass

@admin.register(Person)
class Expenese(admin.ModelAdmin):
	pass