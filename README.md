# My Django-Ecom-App retry
 The old one is dead...

I am working on being a back-end engineer, so I start learning Python and using django frame to build a E-commerce website for study purpose.

I've tried building this website multiple times, but some of them look bad so I deleted their commit, this website won't make any money, all of the products are data and still I don't have the operating rights to run these products as well as I do not actually own them.

PayPal paying function is working, please use sandbox account.

Credit Cards paying isn't working, click the button will create order at the back-end of PostgreSQL on railway or localhost's PostgreSQL.


```
Ecom-retry
├─ ecom                                      
│  ├─ cart
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ cart.py
│  │  ├─ context_processors.py
│  │  ├─ migrations
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     └─ __init__.cpython-312.pyc
│  │  ├─ models.py
│  │  ├─ templates
│  │  │  └─ cart_summary.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ admin.cpython-312.pyc
│  │     ├─ apps.cpython-312.pyc
│  │     ├─ cart.cpython-312.pyc
│  │     ├─ context_processors.cpython-312.pyc
│  │     ├─ models.cpython-312.pyc
│  │     ├─ urls.cpython-312.pyc
│  │     ├─ views.cpython-312.pyc
│  │     └─ __init__.cpython-312.pyc
│  ├─ db.sqlite3
│  ├─ ecom
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ settings.cpython-312.pyc
│  │     ├─ urls.cpython-312.pyc
│  │     ├─ wsgi.cpython-312.pyc
│  │     └─ __init__.cpython-312.pyc
│  ├─ manage.py
│  ├─ media
│  │  └─ uploads
│  │     └─ product
│  │        ├─ 16pm.webp
│  │        ├─ 4080s.webp
│  │        ├─ 4090.jpg
│  │        ├─ 5080.webp
│  │        ├─ 5090.webp
│  │        ├─ 7800X3D.jpg
│  │        ├─ 9800x3d.webp
│  │        ├─ 9800x3d_8nCcdfg.webp
│  │        ├─ 990P.jpg
│  │        ├─ 9950x.webp
│  │        ├─ ASUS_ROG_Phone_9_Pro_Edition.webp
│  │        ├─ BeastBlackDDR5.jpg
│  │        ├─ FURY_Beast_DDR5_5600_64GB.webp
│  │        ├─ H610I-PLUS_D4-CSM.webp
│  │        ├─ i16.webp
│  │        ├─ i7-14700K.jpg
│  │        ├─ iPhone_14.webp
│  │        ├─ iPhone_16_Pro_Max_256G.webp
│  │        ├─ MSI_5090.webp
│  │        ├─ MSI_MAG_X670E.webp
│  │        ├─ MX5002T.webp
│  │        ├─ PNYDDR5.jpg
│  │        ├─ S24U.webp
│  │        ├─ s25u.webp
│  │        ├─ Samsung_990_PRO_2TB_NVMe_M.2_2280_PCIe.webp
│  │        ├─ SONY_Xperia_1_VI.webp
│  │        ├─ SPARKLE_Arc_A750_ORC_.webp
│  │        ├─ T700.jpg
│  │        ├─ T700_4TB.webp
│  │        ├─ Ultra_7_265K.webp
│  │        ├─ Ultra_7_265K_pA1sQoF.webp
│  │        ├─ V-ColorDDR5_6800_96GB.webp
│  │        ├─ ZOTAC_GAMING_GeForce_RTX_4070_SUPER.webp
│  │        ├─ 十銓_T-FORCE_XTREEM_ARGB_DDR4-3200_32GB16Gx2.webp
│  │        └─ 技嘉Z890.webp
│  ├─ payment
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ hooks.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_rename_address1_shippingaddress_shipping_full_name_and_more.py
│  │  │  ├─ 0003_rename_shipping_fulladdress1_shippingaddress_shipping_address1_and_more.py
│  │  │  ├─ 0004_order_orderitem.py
│  │  │  ├─ 0005_order_shipped.py
│  │  │  ├─ 0006_order_date_shipped.py
│  │  │  ├─ 0007_order_invoice_order_paid.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ 0001_initial.cpython-312.pyc
│  │  │     ├─ 0002_rename_address1_shippingaddress_shipping_full_name_and_more.cpython-312.pyc
│  │  │     ├─ 0003_rename_shipping_fulladdress1_shippingaddress_shipping_address1_and_more.cpython-312.pyc
│  │  │     ├─ 0004_order_orderitem.cpython-312.pyc
│  │  │     ├─ 0005_order_shipped.cpython-312.pyc
│  │  │     ├─ 0006_order_date_shipped.cpython-312.pyc
│  │  │     ├─ 0007_order_invoice_order_paid.cpython-312.pyc
│  │  │     └─ __init__.cpython-312.pyc
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
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ admin.cpython-312.pyc
│  │     ├─ apps.cpython-312.pyc
│  │     ├─ forms.cpython-312.pyc
│  │     ├─ hooks.cpython-312.pyc
│  │     ├─ models.cpython-312.pyc
│  │     ├─ urls.cpython-312.pyc
│  │     ├─ views.cpython-312.pyc
│  │     └─ __init__.cpython-312.pyc
│  ├─ procfile
│  ├─ railway.json
│  ├─ requirements.txt
│  ├─ runtime.txt
│  ├─ static
│  │  ├─ asia-god-tone-wayne75525.gif
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
│  │  ├─ admin
│  │  │  ├─ css
│  │  │  │  ├─ autocomplete.css
│  │  │  │  ├─ base.css
│  │  │  │  ├─ changelists.css
│  │  │  │  ├─ dark_mode.css
│  │  │  │  ├─ dashboard.css
│  │  │  │  ├─ forms.css
│  │  │  │  ├─ login.css
│  │  │  │  ├─ nav_sidebar.css
│  │  │  │  ├─ responsive.css
│  │  │  │  ├─ responsive_rtl.css
│  │  │  │  ├─ rtl.css
│  │  │  │  ├─ unusable_password_field.css
│  │  │  │  ├─ vendor
│  │  │  │  │  └─ select2
│  │  │  │  │     ├─ LICENSE-SELECT2.md
│  │  │  │  │     ├─ select2.css
│  │  │  │  │     └─ select2.min.css
│  │  │  │  └─ widgets.css
│  │  │  ├─ img
│  │  │  │  ├─ calendar-icons.svg
│  │  │  │  ├─ gis
│  │  │  │  │  ├─ move_vertex_off.svg
│  │  │  │  │  └─ move_vertex_on.svg
│  │  │  │  ├─ icon-addlink.svg
│  │  │  │  ├─ icon-alert.svg
│  │  │  │  ├─ icon-calendar.svg
│  │  │  │  ├─ icon-changelink.svg
│  │  │  │  ├─ icon-clock.svg
│  │  │  │  ├─ icon-deletelink.svg
│  │  │  │  ├─ icon-hidelink.svg
│  │  │  │  ├─ icon-no.svg
│  │  │  │  ├─ icon-unknown-alt.svg
│  │  │  │  ├─ icon-unknown.svg
│  │  │  │  ├─ icon-viewlink.svg
│  │  │  │  ├─ icon-yes.svg
│  │  │  │  ├─ inline-delete.svg
│  │  │  │  ├─ LICENSE
│  │  │  │  ├─ README.txt
│  │  │  │  ├─ search.svg
│  │  │  │  ├─ selector-icons.svg
│  │  │  │  ├─ sorting-icons.svg
│  │  │  │  ├─ tooltag-add.svg
│  │  │  │  └─ tooltag-arrowright.svg
│  │  │  └─ js
│  │  │     ├─ actions.js
│  │  │     ├─ admin
│  │  │     │  ├─ DateTimeShortcuts.js
│  │  │     │  └─ RelatedObjectLookups.js
│  │  │     ├─ autocomplete.js
│  │  │     ├─ calendar.js
│  │  │     ├─ cancel.js
│  │  │     ├─ change_form.js
│  │  │     ├─ core.js
│  │  │     ├─ filters.js
│  │  │     ├─ inlines.js
│  │  │     ├─ jquery.init.js
│  │  │     ├─ nav_sidebar.js
│  │  │     ├─ popup_response.js
│  │  │     ├─ prepopulate.js
│  │  │     ├─ prepopulate_init.js
│  │  │     ├─ SelectBox.js
│  │  │     ├─ SelectFilter2.js
│  │  │     ├─ theme.js
│  │  │     ├─ unusable_password_field.js
│  │  │     ├─ urlify.js
│  │  │     └─ vendor
│  │  │        ├─ jquery
│  │  │        │  ├─ jquery.js
│  │  │        │  ├─ jquery.min.js
│  │  │        │  └─ LICENSE.txt
│  │  │        ├─ select2
│  │  │        │  ├─ i18n
│  │  │        │  │  ├─ af.js
│  │  │        │  │  ├─ ar.js
│  │  │        │  │  ├─ az.js
│  │  │        │  │  ├─ bg.js
│  │  │        │  │  ├─ bn.js
│  │  │        │  │  ├─ bs.js
│  │  │        │  │  ├─ ca.js
│  │  │        │  │  ├─ cs.js
│  │  │        │  │  ├─ da.js
│  │  │        │  │  ├─ de.js
│  │  │        │  │  ├─ dsb.js
│  │  │        │  │  ├─ el.js
│  │  │        │  │  ├─ en.js
│  │  │        │  │  ├─ es.js
│  │  │        │  │  ├─ et.js
│  │  │        │  │  ├─ eu.js
│  │  │        │  │  ├─ fa.js
│  │  │        │  │  ├─ fi.js
│  │  │        │  │  ├─ fr.js
│  │  │        │  │  ├─ gl.js
│  │  │        │  │  ├─ he.js
│  │  │        │  │  ├─ hi.js
│  │  │        │  │  ├─ hr.js
│  │  │        │  │  ├─ hsb.js
│  │  │        │  │  ├─ hu.js
│  │  │        │  │  ├─ hy.js
│  │  │        │  │  ├─ id.js
│  │  │        │  │  ├─ is.js
│  │  │        │  │  ├─ it.js
│  │  │        │  │  ├─ ja.js
│  │  │        │  │  ├─ ka.js
│  │  │        │  │  ├─ km.js
│  │  │        │  │  ├─ ko.js
│  │  │        │  │  ├─ lt.js
│  │  │        │  │  ├─ lv.js
│  │  │        │  │  ├─ mk.js
│  │  │        │  │  ├─ ms.js
│  │  │        │  │  ├─ nb.js
│  │  │        │  │  ├─ ne.js
│  │  │        │  │  ├─ nl.js
│  │  │        │  │  ├─ pl.js
│  │  │        │  │  ├─ ps.js
│  │  │        │  │  ├─ pt-BR.js
│  │  │        │  │  ├─ pt.js
│  │  │        │  │  ├─ ro.js
│  │  │        │  │  ├─ ru.js
│  │  │        │  │  ├─ sk.js
│  │  │        │  │  ├─ sl.js
│  │  │        │  │  ├─ sq.js
│  │  │        │  │  ├─ sr-Cyrl.js
│  │  │        │  │  ├─ sr.js
│  │  │        │  │  ├─ sv.js
│  │  │        │  │  ├─ th.js
│  │  │        │  │  ├─ tk.js
│  │  │        │  │  ├─ tr.js
│  │  │        │  │  ├─ uk.js
│  │  │        │  │  ├─ vi.js
│  │  │        │  │  ├─ zh-CN.js
│  │  │        │  │  └─ zh-TW.js
│  │  │        │  ├─ LICENSE.md
│  │  │        │  ├─ select2.full.js
│  │  │        │  └─ select2.full.min.js
│  │  │        └─ xregexp
│  │  │           ├─ LICENSE.txt
│  │  │           ├─ xregexp.js
│  │  │           └─ xregexp.min.js
│  │  ├─ asia-god-tone-wayne75525.gif
│  │  ├─ assets
│  │  │  └─ github.png
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
│  └─ store
│     ├─ admin.py
│     ├─ apps.py
│     ├─ forms.py
│     ├─ migrations
│     │  ├─ 0001_initial.py
│     │  ├─ 0002_alter_category_options.py
│     │  ├─ 0003_profile.py
│     │  ├─ 0004_profile_oldcart.py
│     │  ├─ 0005_alter_profile_oldcart.py
│     │  ├─ __init__.py
│     │  └─ __pycache__
│     │     ├─ 0001_initial.cpython-312.pyc
│     │     ├─ 0002_alter_category_options.cpython-312.pyc
│     │     ├─ 0003_profile.cpython-312.pyc
│     │     ├─ 0004_profile_oldcart.cpython-312.pyc
│     │     ├─ 0005_alter_profile_oldcart.cpython-312.pyc
│     │     └─ __init__.cpython-312.pyc
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
│     ├─ tests.py
│     ├─ urls.py
│     ├─ views.py
│     ├─ __init__.py
│     └─ __pycache__
│        ├─ admin.cpython-312.pyc
│        ├─ apps.cpython-312.pyc
│        ├─ forms.cpython-312.pyc
│        ├─ models.cpython-312.pyc
│        ├─ urls.cpython-312.pyc
│        ├─ views.cpython-312.pyc
│        └─ __init__.cpython-312.pyc
├─ list.txt
└─ README.md

```

Website link:https://django-ecom-app-production-d8d0.up.railway.app/

