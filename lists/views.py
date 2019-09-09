from django.shortcuts import render
from django.http import HttpResponse
from lists.models import ToDoItem

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        toDoItem = ToDoItem()
        toDoItem.description = request.POST.get('item_text')
        toDoItem.save()
        
        return render(request, 'index.html', {'new_item_text':toDoItem.description})
    return render(request, 'index.html')
