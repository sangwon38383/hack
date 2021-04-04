from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone 
from .models import Bond, BondOther  
from .forms import BondForm, SellForm
from .text_analysis import *

def bond_list(request):
   bonds = Bond.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'bonds/bond_list.html', {'bonds':bonds})

def bondother_list(request):
   bonds = BondOther.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'bonds/bond_buy.html', {'bonds':bonds})


def post_new(request):
    if request.method == "POST":
        form = BondForm(request.POST)
        if form.is_valid():
            bond = form.save(commit=False)
            bond.author = request.user 
            bond.published_date = timezone.now()
            bond.estimated_rate = do_anal(bond.company)
            bond.save()
            return redirect('bond_detail', pk = bond.pk) 
    else:
        form = BondForm()
    return render(request, 'bonds/bond_edit.html', {'form': form})


def bond_detail(request, pk):
    bond = get_object_or_404(Bond, pk=pk)
    if request.method == "POST":
        form = SellForm(request.POST)
        if form.is_valid():
            bond = form.save(commit=False)
            bond.author = request.user
            bond.published_date = timezone.now()
            bond.save()
            return redirect('contract_sell', pk = bond.pk)
    else:
        form = SellForm()
    return render(request, 'bonds/bond_detail.html', {'bond': bond, 'form' : form})

def bondother_detail(request, pk):
    bond = get_object_or_404(BondOther, pk=pk)
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bond = form.save(commit=False)
            bond.author = request.user
            bond.published_date = timezone.now()
            bond.save()
            return redirect('contract_buy', pk = bond.pk)
    else:
        form = BidForm()
    return render(request, 'bonds/bond_detail.html', {'bond': bond, 'form' : form})

def contract_sell(request, pk):
    bonds = Bond.objects.filter(minprice__contains = 'Sell').order_by('published_date')
    return render(request, 'bonds/sell_bond_list.html', {'bonds':bonds})

def contract_buy(request, pk):
    bonds = Bond.objects.filter(minprice__contains = 'Bid').order_by('published_date')
    return render(request, 'bonds/buy_bond_list.html', {'bonds':bonds})

def bond_sell(request, pk):
    bond = get_object_or_404(Bond, pk=pk)
    if request.method == "POST":
        bond_sell_form = SellForm(request.POST)
        if bond_sell_form.is_valid():   
            sell = bond_sell_form.save(commit=False)
            bond.price = sell.price
            bond.save()
            return redirect('bond_detail', pk = bond.pk)
    else:
        bond_sell_form = SellForm()    
        
    return render(request, 'bonds/bond_sell.html', {'bond_sell_form': bond_sell_form})
