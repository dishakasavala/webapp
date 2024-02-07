from django.shortcuts import render,redirect
from webapp.models import enter,enterForm,slider,sliderForm,maincatagory,maincatForm,subcatagory,subcatForm,petacatgory,petacatForm

# Create your views here.
def loginpage(request):
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
    return render(request,'login.html',{'msg':msg})
def enterpage(request):
    s = ''
    frm = enterForm()
    if 'register' in request.POST:
        frm = enterForm(request.POST)
        frm.save()
        s = "suceessfully enter"
        return redirect('/login')
    return render(request,'enter.html',{'ans':s,'frm':frm})
def datapage(request):
    # if 'user_id' not in request.session:
    #     return redirect('/login')
    # user_id = request.session['user_id']
    # return render(request,'data.html',{'id':user_id})
    return render(request,'data.html')
def sliderpage(request):
    frmobj = sliderForm()
    if 'submit' in request.POST:
        frmobj = sliderForm(request.POST,request.FILES)
        frmobj.save()
        print('sucees')
        return redirect('/tables')
    return render(request,'slider.html',{'frm':frmobj})
def basictable(request):
    sdata = slider.objects.all()
    return render(request,'basic-table.html',{'sdata':sdata})
def editslider(request,sed_id):
    obj = slider.objects.filter(id=sed_id).get()
    frmobj = sliderForm(instance=obj)
    if 'submit'in request.POST:
        frmobj = sliderForm(request.POST,request.FILES,instance=obj)
        frmobj.save()
        return redirect('/tables')
    return render(request,'edit_slider.html',{'frm':frmobj})
def deleteslider(request,sdel_id):
    slider.objects.filter(id=sdel_id).delete()
    return redirect('/tables')

def maincategorytable(request):
    mcatd = maincatagory.objects.all()
    return render(request,'catagory-table.html',{'mcatd':mcatd})
def maincatogry(request):
    frm = maincatForm()
    if 'submit' in request.POST:
        frm = maincatForm(request.POST,request.FILES)
        frm.save()
        return redirect('/maincata_tables')
    return render(request,'main-catagory.html',{'frm':frm})
def editmaincat(request,maied_id):
    s=''
    obj = maincatagory.objects.filter(id=maied_id).get()
    frm = maincatForm(instance=obj)
    if 'submit' in request.POST:
        frm = maincatForm(request.POST,request.FILES,instance=obj)
        frm.save()
        return redirect('/maincata_tables')
    return render(request,'edit-maincat.html',{'frm':frm})
def deletemaincat(request,maidel_id):
    maincatagory.objects.filter(id=maidel_id).delete()
    return redirect('/maincata_tables')

def subcattable(request):
    subd = subcatagory.objects.all()
    return render(request,'subcat-table.html',{'subd':subd})
def subcat(request):
    frm = subcatForm()
    if 'submit' in request.POST:
        frm = subcatForm(request.POST,request.FILES)
        frm.save()
        return redirect('/subcat_table')
    return render(request,'sub-catagory.html',{'frm':frm})
def editsubcat(request,subed_id):
    obj = subcatagory.objects.filter(id=subed_id).get()
    frm = subcatForm(instance=obj)
    if 'submit' in request.POST:
        frm = subcatForm(request.POST,request.FILES,instance=obj)
        frm.save()
        return redirect('/subcat_table')
    return render(request,'edit-subcat.html',{'frm':frm})
def delsubcat(request,subdel_id):
    subcatagory.objects.filter(id=subdel_id).delete()
    return redirect('/subcat_table')

def petacattale(request):
    petad = petacatgory.objects.all()
    return render(request,'petacat-table.html',{'petad':petad})
def patacat(request):
    pdata = subcatagory.objects.all()
    frm = petacatForm
    if 'submit' in request.POST:
        frm = petacatForm(request.POST,request.FILES)
        frm.save()
        return redirect('/petacat_table')
    return render(request,'petacatagory.html',{'pdata':pdata,'frm':frm})
def editpetacat(request,petaed_id):
    obj = petacatgory.objects.filter(id=petaed_id).get()
    frm = petacatForm(instance=obj)
    if 'submit' in request.POST:
        frm = petacatForm(request.POST,request.FILES,instance=obj)
        frm.save()
        return redirect('/petacat_table')
    return render(request,'edit-petacat.html',{'frm':frm})
def delpetacat(request,petadel_id):
    petacatgory.objects.filter(id=petadel_id).delete()
    return redirect('/petacat_table')


    


