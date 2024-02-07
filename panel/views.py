from django.shortcuts import render,redirect
from webapp.models import slider,maincatagory,subcatagory,enter,enterForm,petacatgory,cart,cartForm

# Create your views here.
def index(request):
    sdata = slider.objects.all()
    mcatd = maincatagory.objects.all()
    subd = subcatagory.objects.all()
    petad = petacatgory.objects.all()
    return render(request,'index.html',{'sdata':sdata,'mcatd':mcatd,'subd':subd,'petad':petad})
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contactp(request):
    return render(request,'contact.html')
def shop(request):
    return render(request,'shop.html')
def singlepost(request):
    return render(request,'single-post.html')
def styles(request):
    return render(request,'styles.html')
def thankyou(request):
    return render(request,'thank-you.html')
def blogmasony(request):
    return render(request,'blog-masonry.html')
def blogsidebar(request):
    return render(request,'blog-sidebar.html')
def cartp(request):
    petad = petacatgory.objects.all()
    return render(request,'cart.html',{'petad':petad})
def checkout(request):
    return render(request,'checkout.html')
def comingsoon(request):
    return render(request,'coming-soon.html')
def error(request):
    return render(request,'error.html')
def faqs(request):
    return render(request,'faqs.html')
def loginadmin(request):
    msg = ''
    if 'user_id' in request.session:
        return redirect('/data')
    if 'login' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        obj = enter.objects.filter(email=email,password=password)
        if obj.count()==1:
            print('success')
            row = obj.get() 
            request.session['user_id'] = row.id
            return redirect("/data")
        else:
            print('failer')
            msg = "Invalid email and password"
    return render(request,'ad_login.html')
def shpogrid(request):
    return render(request,'shop-grid.html')
def shoplist(request):
    return render(request,'shop-list.html')
def shopslider(request):
    return render(request,'shop-slider.html')
def singleprouct(request,product_id):
    user = ''
    if 'eid' in request.session:
        uid = request.session['eid']
        data = enter.objects.filter(id=uid)
        user = data.get().name
    if 'eid' not in request.session:
        return redirect('/login')
    crtobj = cartForm(request.POST)
    if 'add' in request.POST:
        crtobj = cartForm(request.POST)
        crtobj.save()
        return redirect('/cart')
    obj = petacatgory.objects.filter(id=product_id).get()
    ci = obj.catagory_id
    pc = obj.peta_catagory_id
    c = subcatagory.objects.filter(id=ci).get()
    cat = c.catagory
    b = petacatgory.objects.filter(id=pc).get()
    brand = b.name

    return render(request,'single-product.html')
def wishlist(request):
    return render(request,'wishlist.html') 