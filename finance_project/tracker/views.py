from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

# Create your views here.
def transaction_list(request):
    all_transactions = Transaction.objects.all()
    context = {
    'transactions': all_transactions,
    }
    return render(request, 'tracker/transaction_list.html', context)

#--------------------------------------------------------
def add_transaction(request):
    if request.method == 'POST':
       form = TransactionForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'tracker/add_transaction.html', {'form': form})

#---------------------------------------------------------
def single_transact(request, id):
    one_transaction = Transaction.objects.get(id=id)
    context = {
        'transaction': one_transaction,
    }

    return render(request, 'tracker/single_transact.html', context)

#---------------------------------------------------------
def edit_transaction(request, id):
    transaction_to_edit = Transaction.objects.get(id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            transaction_to_edit.delete()
            return redirect('transaction_list')
        else:
            form = TransactionForm(request.POST, instance=transaction_to_edit)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction_to_edit)
    
    context = {
        'form': form
    }
    return render(request, 'tracker/edit_transaction.html', context)
#----------------------------------------------------------
def home(request):
    dashboard = Transaction.objects.all()
    total_income = 0
    total_expenses = 0
    for transaction in dashboard:
        if transaction.amount > 0:
            total_income += transaction.amount
        else:
            total_expenses += transaction.amount

    print(f"DEBUG: Total income calculated is {total_income}")
    print(f"DEBUG: Total Expenses calculated is {total_expenses}")

    
    total_expenses = abs(total_expenses)

    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
    }
    return render(request, 'tracker/home.html', context)
#----------------------------------------------------------












