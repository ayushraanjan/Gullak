from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Wallet
from .forms import TaskForm
from .models import Approval
from .forms import AddMoneyForm
from django.core.exceptions  import ValidationError
from django.core.validators import MaxValueValidator
from child.models import ChildwalletBalance
from decimal import Decimal


def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        parent = request.user  
        reward = request.POST['reward']
        task = Task.objects.create(parent=parent, title=title, description=description, reward=reward)
        wallet = Wallet.objects.get(user=parent)
        wallet.balance = wallet.balance - Decimal(reward)
        wallet.save()
        return redirect('parent:dashboard')  
    return redirect('parent:dashboard')

@login_required
def dashboard(request):
    parent = request.user
    task_list = Task.objects.filter(parent=parent)
    approval = Approval.objects.filter(parent=parent)
    
    wallet, created = Wallet.objects.get_or_create(user=request.user)

    form = TaskForm()
    
    
    add_money_form = AddMoneyForm()
    
   
    return render(request, 'dashboard.html', {
        'task_list' : task_list,
        'NewTaskForm' : form,
        'approvals' : approval,
        'balance' : wallet.balance,
        'add_money' : add_money_form,

    
    })

def approved(request, task_id):
    if request.method == 'POST':
        task = Approval.objects.get(id=task_id)
        task_title = task.title
        task_to_delete = Task.objects.get(title=task_title)
        task_reward = task_to_delete.reward
        ChildwalletBalance += task_reward
        Wallet -= task_reward


        task_to_delete.delete()
        task.delete()

        return redirect('dashboard')



def add_money(request):
    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            wallet, created = Wallet.objects.get_or_create(user=request.user)
            wallet.balance += amount
            wallet.save()
            return redirect('parent:dashboard')
    else:
        form = AddMoneyForm()
    return render(request, 'add_money.html', {'form': form})