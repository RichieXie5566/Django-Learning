from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
import time
from .models import Order

@receiver(valid_ipn_received)
def paypal_payment_recevied(sender, **kwargs):
    
    # 幫我稱10秒讓PayPal送出IPN
    time.sleep(10)
    
    paypal_obj = sender
    my_Inovice = str(paypal_obj.invoice)
    
    # 確認訂單資料跟PayPal有對上
    my_Order = Order.objects.get(invoice=my_Inovice)
    # 確認付款了
    my_Order.paid = True
    # 儲存訂單
    my_Order.save()