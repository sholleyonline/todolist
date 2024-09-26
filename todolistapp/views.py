from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDoList, ToDoItem


def index(request):
    lists = ToDoList.objects.all()
    return render(request, 'index.html',{'lists':lists})

def view_list(request, list_id):
    todo_list = get_object_or_404(ToDoList, id=list_id)
    return render(request, 'list.html',{'list':todo_list})


def add_item(request, list_id):
    todo_list = get_object_or_404(ToDoList, id=list_id)
    if request.method == 'POST':
        text = request.POST['text']
        if text == "":
            return render(request, 'add_item.html', {'list':todo_list})
        else:
            ToDoItem.objects.create(list=todo_list, text=text)
            return redirect('view_list', list_id=list_id)
    return render(request, 'add_item.html', {'list':todo_list})

def delete_item(request, item_id):
    listItem = get_object_or_404(ToDoItem, id=item_id)

    listItem.delete()
    return redirect('view_list', listItem.list_id)
    
    
    # todo_list = get_object_or_404(ToDoList, id=list_id)
    # return render(request, 'list.html',{'list':todo_list})
