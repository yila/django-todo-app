from django.shortcuts import render
from django.http import HttpResponse
from lists.models import ToDoItem

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        description = request.POST['item_text']
        ToDoItem.objects.create(description=description)
        return render(request, 'index.html', {'new_item_text':description})
    return render(request, 'index.html')
