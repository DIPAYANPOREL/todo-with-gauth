from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo
from .forms import TodoForm
import logging


logger = logging.getLogger(__name__)

@login_required(login_url='account_login')
def todo_list(request):
    logger.info(f"Accessing todo_list view with user: {request.user}")
    
    # Remove the is_authenticated check since @login_required already handles it
    try:
        todos = Todo.objects.filter(user=request.user)
        context = {
            'todos': todos,
            'user': request.user
        }
        return render(request, 'todo/todo_list.html', context)
    except Exception as e:
        logger.error(f"Error in todo_list view: {str(e)}")
        messages.error(request, 'Error loading todos. Please try again.')
        return redirect('account_login')
    

@login_required(login_url='account_login')
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, 'Todo created successfully!')
            return redirect('todo_list')
        else:
            messages.error(request, 'Error creating todo. Please check the form.')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})

@login_required(login_url='account_login')
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo updated successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form, 'todo': todo})

@login_required(login_url='account_login')
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo deleted successfully!')
        return redirect('todo_list')
    return render(request, 'todo/todo_delete.html', {'object': todo})