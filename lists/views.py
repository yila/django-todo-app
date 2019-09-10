from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import ToDoItem

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        ToDoItem.objects.create(description=request.POST['item_text'])
        return redirect('/')
    return render(request, 'index.html')
