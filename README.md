# My Django-Ecom-App retry

Website link:https://django-ecom-app-production-d8d0.up.railway.app/

I am working towards becoming a back-end engineer, so I started learning Python and using the Django framework to build an E-commerce website for study purpose.

I've attempted to building this website multiple times, but some versions didn't turn out well, so I deleted their commits. This website is not intended for commercial use, all products are dummy data and still I don't have rights to operate or own them.

The PayPal payment function is working, sandbox account testing only.

Credit Cards payments are not yet functional. 
Click the button will create order on Railway or local PostgreSQL instance.

## 1.Element and tree
### Using Python3.12 Django PostgreSQL Railway
```
Ecom-retry
├─ ecom                                      
│  ├─ cart
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ cart.py
│  │  ├─ context_processors.py
│  │  │  
│  │  ├─ models.py
│  │  ├─ templates
│  │  │  └─ cart_summary.html
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  
│  │   
│  ├─ ecom
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │
│  │  
│  ├─ manage.py
│  ├─ media
│  │  └─ uploads
│  │     └─ product
│  │        ├─ T700_4TB.webp
│  │        ├─ Ultra_7_265K.webp
│  │        ├─ 9800x3d.webp
│  │        ├─ ASUS_ROG_Phone_9_Pro_Edition.webp
│  │        ├─ FURY_Beast_DDR5_5600_64GB.webp
│  │        ├─ iPhone_14.webp
│  │        ├─ MSI_5090.webp
│  │        ├─ MSI_MAG_X670E.webp
│  │          
│  │        
│  ├─ payment
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ hooks.py
│  │  ├─ models.py
│  │  ├─ templates
│  │  │  └─ payment
│  │  │     ├─ billing_info.html
│  │  │     ├─ checkout.html
│  │  │     ├─ not_shipped_dash.html
│  │  │     ├─ orders.html
│  │  │     ├─ payment
│  │  │     ├─ payment_failed.html
│  │  │     ├─ payment_success.html
│  │  │     ├─ process_order.html
│  │  │     └─ shipped_dash.html
│  │  ├─ urls.py
│  │  ├─ views.py
│  │
│  ├─ procfile
│  ├─ railway.json
│  ├─ requirements.txt
│  ├─ runtime.txt
│  ├─ static
│  │  ├─ css
│  │  │  └─ styles.css
│  │  ├─ favicon.ico
│  │  ├─ gs large.jpeg
│  │  ├─ gs mid.png
│  │  ├─ gs.jpeg
│  │  ├─ js
│  │  │  └─ scripts.js
│  │  ├─ search.png
│  │  └─ wayne75525-bd.gif
│  ├─ staticfiles
│  │
│  │
│  └─ store
│     ├─ admin.py
│     ├─ apps.py
│     ├─ forms.py
│     │
│     ├─ models.py
│     ├─ templates
│     │  ├─ about.html                              
│     │  ├─ base.html
│     │  ├─ category.html
│     │  ├─ home.html
│     │  ├─ login.html
│     │  ├─ navbar.html
│     │  ├─ product.html
│     │  ├─ register.html
│     │  ├─ search.html
│     │  ├─ update_info.html
│     │  ├─ update_password.html
│     │  └─ update_user.html
│     ├─ urls.py
│     ├─ views.py
│     │
└─ README.md

```

## 2.User
### Register -->Login -->Update_user, Update_password or Update_info.

## 3.Product
### Searching product, Product pages, Add to cart.

## 4.Checkout
### Check -->Billing_info -->Process_order -->Payment_success or Payment_failed

## 5.Admin Session
### Shipped_dashboard -->Order_shipped or Order_unshipped
