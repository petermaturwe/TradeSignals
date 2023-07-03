from django.shortcuts import render, redirect
from .models import TradeSignal
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm

def index(request):
    # Get all trade signals
    trade_signals = TradeSignal.objects.all()

    # Separate the trade signals by category
    forex_signals = trade_signals.filter(category='forex')
    stock_signals = trade_signals.filter(category='stock')
    crypto_signals = trade_signals.filter(category='cryptocurrency')

    context = {
        'forex_signals': forex_signals,
        'stock_signals': stock_signals,
        'crypto_signals': crypto_signals,
    }
    return render(request, 'index.html', context)

def payment(request):
    return render(request, "payment.html")
def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'index' with the appropriate URL name for your home page
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})


def logoutview(request):
    logout(request)
    return redirect('login') 
def base(request):
    return redirect('base')
def stock_signals(request):
    stock_signals = TradeSignal.objects.filter(category='stock')
    return render(request, 'stock.html', {'stock_signals': stock_signals})

def forex_signals(request):
    forex_signals = TradeSignal.objects.filter(category='forex')
    return render(request, 'forex.html', {'forex_signals': forex_signals})
def crypto_signals(request):
    crypto_signals = TradeSignal.objects.filter(category='crypto')
    return render(request, 'crypto.html', {'crypto_signals': crypto_signals})

