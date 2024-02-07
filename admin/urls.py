"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from panel.views import *
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index),
    path('about/',about),
    path('blog/',blog),
    path('contact/',contactp),
    path('shop/',shop),
    path('single_post/',singlepost),
    path('style/',styles),
    path('thank_you/',thankyou),
    path('blog_masonry/',blogmasony),
    path('blog_sidebar/',blogsidebar),
    path('cart/',cartp),
    path('checkout/',checkout),
    path('coming_soon/',comingsoon),
    path('error/',error),
    path('faqs/',faqs),
    path('login_admin/',loginadmin),
    path('shop_grid/',shpogrid),
    path('shop_list/',shoplist),
    path('shop_slider/',shopslider),
    path('wishlist/',wishlist),
    path('single_product/<int:product_id>/',singleprouct),

    # webapp urls
    path('login/',loginpage),
    path('enter/',enterpage),
    path('data/',datapage),
    path('slider/',sliderpage),
    path('tables/',basictable),
    path('edit-slider/<int:sed_id>',editslider),
    path('delete-slider/<int:sdel_id>',deleteslider),
    path('maincata_tables/',maincategorytable),
    path('main_catagory/',maincatogry),
    path('edit-maincat/<int:maied_id>',editmaincat),
    path('delete-maincat/<int:maidel_id>',deletemaincat),
    path('sub_catagory/',subcat),
    path('subcat_table/',subcattable),
    path('editsub_catagory/<int:subed_id>',editsubcat),
    path('delsub_catagory/<int:subdel_id>',delsubcat),
    path('petacat_table/',petacattale),
    path('peta_catagory/',patacat),
    path('editpeta_catagory/<int:petaed_id>',editpetacat),
    path('delpeta_catagory/<int:petadel_id>',delpetacat),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
