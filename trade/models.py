from django.db import models
from django.utils import timezone
# Create your models here.

def default_created_at():
    return timezone.now()
    
class TradeSignal(models.Model):
    currency = models.CharField(max_length=50)
    buy = models.BooleanField(default=False)
    sell = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    close_button_visible = models.BooleanField(default=False)
    entry_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, default=None)
    entry_price_visible = models.BooleanField(default=False)
    take_profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    stop_loss_visible = models.BooleanField(default=False)
    take_profit_visible = models.BooleanField(default=False)
    trade_now_visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=default_created_at)

    def get_current_time(self):
        return timezone.localtime(timezone.now())
    


    def __str__(self):
        return self.currency

    class Meta:
        app_label ='trade'
