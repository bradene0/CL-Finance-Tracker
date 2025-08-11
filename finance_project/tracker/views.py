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















