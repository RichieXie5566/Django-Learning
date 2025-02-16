from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    cart = Cart(request) # 從 session中獲取購物車
    cart_products = cart.get_prods # 取得購物車內的所有商品
    quantities = cart.get_quants # 取得購物車內各商品的數量
    totals = cart.cart_total()
    
    # 將購物車內容傳遞給前端的 cart_summary.html
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals})

def cart_add(request):
    cart = Cart(request) # 從session中獲取購物車
    if request.POST.get('action') == 'post': # 檢查請求是否為 AJAX 的 POST 請求
        product_id = int(request.POST.get('product_id')) # 抓JQuery商品id
        product_qty = int(request.POST.get('product_qty')) # 抓JQuery商品數量
        product = get_object_or_404(Product, id=product_id) # 根據 ID 從資料庫獲取商品，若無則返回 404 錯誤
        
        cart.add(product = product, quantity = product_qty) # 將商品及數量加入購物車（Session 中）
        cart_quantity = cart.__len__() # 計算購物車內的總商品數量

        # 回傳 JSON 回應給前端，通知購物車內的總數量（AJAX 可用此數據更新畫面）
        reponse = JsonResponse({'qty':cart_quantity}) # 回傳response
        messages.success(request, '成功加入購物車')
        return reponse

    # 若不是 AJAX POST 請求，則渲染一個基本的 add.html
    return render(request, 'add.html', {})

def cart_delete(request):
    cart = Cart(request) # 創建Cart 物件，基於 request.session
    if request.POST.get('action') == 'post': 
        product_id = int(request.POST.get('product_id')) # 確保數據格式正確
        
        cart.delete(product = product_id) # 調用cart物件的delete方法來更新購物車

        response = JsonResponse({'product' : product_id}) # 回傳 JSON 響應，告知前端更新成功
        messages.success(request, '產品已刪除')
        return response

def cart_update(request):
    cart = Cart(request) # 創建Cart 物件，基於 request.session
    if request.POST.get('action') == 'post': 
        product_id = int(request.POST.get('product_id')) 
        product_qty = int(request.POST.get('product_qty')) # 確保數據格式正確

        cart.update(product = product_id, quantity = product_qty) # 調用 cart 物件的 update 方法來更新購物車數量

        response = JsonResponse({'qty' : product_qty}) # 回傳 JSON 響應，告知前端更新成功
        messages.success(request, '產品數量已更新')
        return response