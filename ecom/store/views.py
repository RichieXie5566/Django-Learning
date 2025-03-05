from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django import forms
import json
from django.db.models import Q
from cart.cart import Cart #cart資料夾裡的cart.py裡面的Cart

def home(request):
    products = Product.objects.all().order_by("id")
    return render(request, 'home.html', {'products':products })

def about(request):
    return render(request, 'about.html', {})

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def category(request, foo):
	# 用空格取代-
	foo = foo.replace('-', ' ')
	# 從URL抓類別
	try:
		# 抓類別
		category = Category.objects.get(name=foo)
		products = Product.objects.filter(category=category)
        
		return render(request, 'category.html', {'products':products, 'category':category})
	except:
		messages.error(request, ("此分類不存在..."))
		return redirect('home')
    

def login_user(request):
    if request.method == "POST": # 如果是表單提交(POST)
        username = request.POST['username']# 取得表單提交的帳號
        password = request.POST['password']# 取得表單提交的密碼
        user = authenticate(request, username = username, password = password) # 使用Django提供的authenticate方法驗證帳號密碼
        
        if user is not None: # 如果驗證成功
            login(request, user) # 執行登入

            current_user = Profile.objects.get(user__id = request.user.id) #取得目前的使用者
            save_cart = current_user.oldcart #從資料庫取得購物車裡面的資料
            if save_cart: #購物車裡面有東西
                converted_cart = json.loads(save_cart) #把django資料庫取出來的資料轉成JSon
                cart = Cart(request) #取得購物車裡的資料
                for key,value in converted_cart.items():
                    cart.db_add(product = key, quantity = value)

            messages.success(request, ('已登入')) # 顯示成功訊息
            return redirect('home') # 登入後導向首頁
        else: # 如果驗證失敗
            messages.error(request, ('登入時發生錯誤，請檢查帳號或密碼')) # 顯示錯誤訊息
            return redirect('login') # 導向登入頁面重新嘗試
    else: # 並未提交表單的帳號與密碼
        return render(request, 'login.html', {}) # 不進行驗證，回傳網頁給使用者

def logout_user(request):
    logout(request) # 清除session，登出當前使用者
    messages.success(request, ('已登出')) # 顯示成功登出訊息
    return redirect('home') # 登出後導向首頁

def register_user(request):
    form = SignUpForm() # 創建一個SignUpForm物件，供GET請求使用
    if request.method == "POST": # 如果是表單提交 (POST)
        form = SignUpForm(request.POST) # 將提交的資料填入表單
        if form.is_valid(): # 驗證表單是否符合規則
            form.save() # 將使用者資料儲存到資料庫

            # 從表單中取得用戶名與密碼 (password1 是 Django 預設的第一組密碼欄位)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(request, username = username, password = password) # authenticate認證新註冊的用戶
            
            # 如果認證成功，自動登入該用戶
            if user is not None:
                login(request, user)
                messages.success(request, '註冊完成並自動登入')  # 註冊成功訊息
                return redirect('home')  # 導向首頁
            else:
                messages.error(request, '註冊成功，但登入時發生問題，請手動登入')  # authenticate失敗的話(密碼雜湊問題、資料庫寫入延遲)
                return redirect('login') # 導向登入頁面，讓使用者自己重新登入
        
        else: # 表單驗證失敗
            messages.error(request, ('註冊時發生錯誤，請檢查帳號或密碼')) # 註冊錯誤訊息
            return redirect('register') # 導向註冊頁面
    else: # 並未提交表單
        return render(request, 'register.html', {'form':form}) # 不進行驗證，回傳網頁給使用者
    
def update_user(request):
    if request.user.is_authenticated: # 確認使用者有無登入
        current_user = User.objects.get(id = request.user.id) #取得目前的使用者
        
        # 如果是 POST 請求，則接收表單資料；如果不是，則使用當前用戶資料填充表單
        user_form = UpdateUserForm(request.POST or None, instance = current_user)

        if user_form.is_valid(): # 驗證表單是否通過
            user_form.save() # 儲存更新後的用戶資料

            login(request, current_user) # 重新登入用戶，確保變更立即生效
            messages.success(request,'成功修改帳號設定') 
            return redirect('home')
        
        # 如果表單驗證失敗，重新渲染表單並顯示錯誤訊息
        return render(request, 'update_user.html', {'user_form':user_form})
    else:
        messages.error(request,'請先登入') # 未登入，顯示錯誤訊息
        return redirect('home')

def update_info(request):
    if request.user.is_authenticated: # 確認使用者有無登入
        current_user = Profile.objects.get(user__id = request.user.id) # 取得目前的使用者
        shipping_user = ShippingAddress.objects.get(user__id = request.user.id) # 取得目前的使用者的宅配資訊
        
        # 如果是 POST 請求，則接收表單資料；如果不是，則使用當前用戶資料填充表單
        form = UserInfoForm(request.POST or None, instance = current_user)
        # 同上
        shipping_form = ShippingForm(request.POST or None, instance = shipping_user)

        if form.is_valid() or shipping_form.is_valid(): # 驗證表單是否通過
            form.save() # 儲存更新後的用戶資料
            shipping_form.save()
            messages.success(request,'成功修改結帳設定')
            return redirect('home')
        
        # 如果表單驗證失敗，重新渲染表單並顯示錯誤訊息
        return render(request, 'update_info.html', {'form':form,'shipping_form':shipping_form})
    else:
        messages.error(request,'請先登入') # 未登入，顯示錯誤訊息
    return render(request, 'login.html', {})

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST) # 將當前用戶與表單資料綁定
            if form.is_valid(): # 驗證表單輸入是否符合要求
                user = form.save() # 儲存新密碼
                update_session_auth_hash(request, user)  # 防止修改密碼後被強制登出
                messages.success(request,'成功修改密碼且自動登入')
                return redirect('home')
            else: # 如果表單驗證失敗
                for error in form.errors.values(): # 遍歷所有錯誤訊息
                    messages.error(request,'發生錯誤請遵守修改規則並重新輸入') 
                return redirect('update_password')

        else: # 如果不是 POST 請求（即 GET 請求，訪問修改密碼頁面）
            form = ChangePasswordForm(current_user) # 創建表單並填充當前用戶資料
            return render(request, 'update_password.html', {'form' : form}) # 渲染修改密碼頁面
        
    else:  # 如果用戶未登入
        messages.error(request,'先登入再修改密碼')
        return redirect('home')

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains = searched)|Q(description__icontains = searched))

        if not searched:
            messages.error(request,'查無商品')
            return render(request, 'search.html', {})
        else:

            return render(request, 'search.html', {'searched':searched})
    else:
        return render(request, 'search.html', {})
    
