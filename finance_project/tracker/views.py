from django.shortcuts import render
from .models import Transaction


# Create your views here.
def transaction_list(request):
    all_transactions = Transaction.objects.all()
    context = {
    'transactions': all_transactions,
    }
    return render(request, 'tracker/transaction_list.html', context)
