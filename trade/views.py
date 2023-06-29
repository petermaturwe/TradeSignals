from django.shortcuts import render, redirect
from .models import TradeSignal
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm

def index(request):
    trade_signals = TradeSignal.objects.all()
    return render(request, 'index.html', {'trade_signals': trade_signals})
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

