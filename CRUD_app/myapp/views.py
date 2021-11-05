from django.shortcuts import render
from .forms import book_form
from .models import Book
from django.http import HttpResponseRedirect
# Create your views here.

# This function is use for add and show data
def add_book(request):
    if request.method == 'POST':
        fm = book_form(request.POST)
        if fm.is_valid():
            bn = fm.cleaned_data['book_name']
            ba = fm.cleaned_data['book_author']
            bp = fm.cleaned_data['book_price']
            alldata = Book(book_name=bn,book_author=ba,book_price=bp)
            alldata.save()
            fm = book_form()
    else:        
       fm = book_form()
    data = Book.objects.all()
    return render(request,'myapp/addbook.html',{'form':fm,'data':data})

# This function is use for delete
def delete_data(request,id):
    if request.method == 'POST':
        dl = Book.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')

# This function is use for Edit & Update 
def edit_data(request,id):
    if request.method == 'POST':
        ed = Book.objects.get(pk=id)
        fm = book_form(request.POST,instance=ed)
        if fm.is_valid():
            fm.save()
    else:
        ed = Book.objects.get(pk=id)
        fm = book_form(instance=ed)    
    return render(request,'myapp/edit.html',{'form':fm})    

               
