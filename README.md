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

## 2.How to install?
### a.Localhost
1.Edit Settings.py
```python
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
2.python manage.py migrate

3.python manage.py runserver (Use another port if there's an error, for instance:8080)

### b.Use your own PostgreSQL
1.Edit Settings.py
```python
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "postgres(default, or use yours.)",
        'USER': 'postgres(default, or use yours.)',
        'PASSWORD': 'Your password',
        'HOST': '127.0.0.1(default, or use yours.)',
        'PORT': '5432(default, or use yours.)',
    }
}
```
2.python manage.py migrate

3.python manage.py runserver (Use another port if there's an error, for instance:8080)

### c.Use your own Railway
1.Why I use Railway?It's cheap. $5 a month, you get this when you create your account.
Maybe you want to use professional version, and it's $20 also cheap.
AWS is cool but too expensive, need more time to create and learn.

2.Create your account and use free version to create New project

3.Deploy PostgreSQL

4.Make sure installing all the stuff in my requirements.txt

5.You may see this on your screen which means deployed sucessfully
<img src="https://imgur.com/y5293Kb.jpeg" width="500">

6.touch .env(at ecom/ecom/)and put password in it. Make sure touch .gitignore if you want to upload
<img src="https://imgur.com/G8guFd9.jpeg" width="500">

7.Edit your settings.py with your variables

<img src="https://imgur.com/noUPAnM.jpeg" width="500">

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "railway",
        'USER': 'postgres',
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'mainline.proxy.rlwy.net',
        'PORT': '5432(default, or use yours.)',
    }
}
```

If you're having issue like with port or host : 
go to railway -> architecture -> settings  -> networking
There you will fing a combination of real host and port. I replaced them with those that I found in variables and it worked

8.Install PostgreSQL 17, add the PostgreSQL bin directory to the Windows environment variable Path, and restart your computer

9.python manage.py migrate

10.











## 3.Product
### Searching product, Product pages, Add to cart.


## 4.Checkout
### Checkout -->Billing_info -->Process_order -->Payment_success or Payment_failed


## 5.Admin Session
### Shipped_dashboard -->Order_shipped or Order_unshipped


