from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'success.html', {'name': name, 'email': email, 'message': message})
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})



def success_view(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    return render(request, 'success.html', {'name': name, 'email': email, 'message': message})

