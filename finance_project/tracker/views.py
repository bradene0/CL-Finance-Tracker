from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.models import User
import time 

# Create your views here.
def transaction_list(request):
    current_user = get_or_create_guest_user(request)
    all_transactions = Transaction.objects.filter(user=current_user)

    context = {
    'transactions': all_transactions,
    }
    return render(request, 'tracker/transaction_list.html', context)

#--------------------------------------------------------
def add_transaction(request):
    current_user = get_or_create_guest_user(request)
    if request.method == 'POST':
       form = TransactionForm(request.POST)
       if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = current_user
            transaction.save() 
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'tracker/add_transaction.html', {'form': form})

#---------------------------------------------------------
def single_transact(request, id):
    one_transaction = get_object_or_404(Transaction, id=id, user=current_user)
    context = {
        'transaction': one_transaction,
    }

    return render(request, 'tracker/single_transact.html', context)

#---------------------------------------------------------
def edit_transaction(request, id):
    current_user = get_or_create_guest_user(request)
    transaction_to_edit = get_object_or_404(Transaction, id=id, user=current_user)

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
    current_user = get_or_create_guest_user(request)
    user_dashboard = Transaction.objects.filter(user=current_user)


    total_income = 0
    total_expenses = 0
    for transaction in user_dashboard:
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
def get_or_create_guest_user(request):
    if request.user.is_authenticated:
        return request.user

    guest_user_id = request.session.get('guest_user_id')

    if guest_user_id:
        try:
            return User.objects.get(id=guest_user_id)
        except User.DoesNotExist:
            pass

    guest_username = f"guest_{int(time.time())}"
    new_guest = User.objects.create(username=guest_username)
    request.session['guest_user_id'] = new_guest.id 

    return new_guest
#-----------------------------------------------------------












