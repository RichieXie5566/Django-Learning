from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from store.models import Product, Profile
from django.utils import timezone

# PayPal要用的
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid

def payment_success(request):
    return render(request, 'payment/payment_success.html', {})

def payment_failed(request):
    return render(request, 'payment/payment_failed.html', {})

def checkout(request):
    cart = Cart(request) # 從 session中獲取購物車
    cart_products = cart.get_prods # 取得購物車內的所有商品
    quantities = cart.get_quants # 取得購物車內各商品的數量
    totals = cart.cart_total()
    
    if request.user.is_authenticated: # 確認使用者有無登入
        shipping_user = ShippingAddress.objects.get(user__id = request.user.id) # 取得目前的使用者的宅配資訊
        shipping_form = ShippingForm(request.POST or None, instance = shipping_user)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form })
    else:
        messages.error(request,'請先登入') # 未登入，顯示錯誤訊息
        return redirect('home')
    
def billing_info(request):
    if request.POST:

        cart = Cart(request) # 從 session中獲取購物車
        cart_products = cart.get_prods # 取得購物車內的所有商品
        quantities = cart.get_quants # 取得購物車內各商品的數量
        totals = cart.cart_total()

        # 建立包含訂單的session
        my_shipping = request.POST 
        request.session['my_shipping'] = my_shipping

        # 獲取主機
        host = request.get_host()
        # 建立PayPal表單
        paypal_dict = {
            'business':settings.PAYPAL_RECEIVER_EMAIL,
            'amount_pay':totals,
            'item_name':'3C Product Order',
            'no_shipping':'2',
            'invoice':str(uuid.uuid4()),
            'currency_code':'TWD',
            'notify_url':'https://{}{}'.format(host, reverse("paypal-ipn")),
            'return_url':'https://{}{}'.format(host, reverse("payment_success")),
            'cancel_return':'https://{}{}'.format(host, reverse("payment_failed")),
        }

        paypal_form = PayPalPaymentsForm(initial=paypal_dict)
    
        if request.user.is_authenticated: # 確認使用者有無登入
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {"paypal_form":paypal_form, "cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form })
        else:
            messages.error(request,'請先登入') # 未登入，顯示錯誤訊息
            return redirect("login")  # 重導向到登入頁面
    else:
        return redirect("cart") # 讓沒有 POST 請求的使用者回到購物車
        
def process_order(request):
    if request.POST:
        cart = Cart(request) # 從 session中獲取購物車
        cart_products = cart.get_prods # 取得購物車內的所有商品
        quantities = cart.get_quants # 取得購物車內各商品的數量
        totals = cart.cart_total()
        payment_form = PaymentForm(request.POST or None)

        # 建立包含訂單的session
        my_shipping = request.session.get('my_shipping')
        
        # 收集訂單資訊
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        phone = my_shipping['shipping_phone']

        # 從 session_info 建立 Shippin_Address
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        amount_pay = totals

        # 建立訂單
        if request.user.is_authenticated:
            user = request.user
            create_order = Order(user=user, full_name=full_name, email=email, phone=phone, shipping_address=shipping_address, amount_pay=amount_pay)
            create_order.save()
            
            # 添加商品在訂單裡
            order_id = create_order.pk # 取得訂單id
            
            for product in cart_products(): # 取得商品id
                product_id = product.id 
                
                if product.is_sale: # 取得商品價錢
                    price = product.sale_price
                else:
                    price = product.price

                # 取得數量
                for key, value in quantities().items():
                    if int(key) == product.id:
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
                        create_order_item.save()
        else:
            messages.error(request,'請先登入') # 未登入，顯示錯誤訊息
            return redirect("login")  # 重導向到登入頁面

        # 結帳完清空購物車
        for key in list(request.session.keys()):
            if key == "session_key":
                del request.session[key]

        # 刪除資料庫裡的oldcart
        current_user = Profile.objects.filter(user__id=request.user.id)
        current_user.update(oldcart="")

        messages.success(request, '訂單已成立，謝謝光臨')
        return redirect("home")
    else:
        messages.error(request,'請先登入') # 未登入，顯示錯誤訊息
        return redirect("login")  # 重導向到登入頁面

def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=True)
        if request.POST:
            status = request.POST['shipping_status']
            num = request.POST['num']
            order = Order.objects.filter(id=num)
            order.update(shipped=False)
            
            messages.success(request, '訂單狀態已變更')
            return redirect('home')
        return render(request, "payment/shipped_dash.html", {"orders":orders})
    else:
        messages.error(request,'你沒有權限瀏覽此頁面')
        return redirect("home")

def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=False)
        if request.POST:
            status = request.POST['shipping_status']
            num = request.POST['num']
            order = Order.objects.filter(id=num)
            now = timezone.now()
            order.update(shipped=True, date_shipped=now)
            
            messages.success(request, '訂單狀態已變更')
            return redirect('home')
        return render(request, 'payment/not_shipped_dash.html', {"orders":orders})
    else:
        messages.error(request,'你沒有權限瀏覽此頁面')
        return redirect("home")

    
def orders(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        items = OrderItem.objects.filter(order=pk)

        if request.POST:
            status = request.POST['shipping_status']
            if status == "true":
                order = Order.objects.filter(id=pk)
                now = timezone.now()
                order.update(shipped=True, date_shipped=now)
            else:
                order = Order.objects.filter(id=pk)
                order.update(shipped=False)

            messages.success(request, '訂單狀態已變更')
            return redirect('home')
        return render(request, 'payment/orders.html', {"order":order,"items":items})
    else:
        messages.error(request,'你沒有權限瀏覽此頁面')
        return redirect("home")

# 引入PayPal
