from django.shortcuts import redirect, render
from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            request.session['name'] = name
            request.session['email'] = email
            request.session['message'] = message
            return redirect('output_view')
    else:
        form = MyForm()
    return render(request, 'input.html', {'form': form})


def output_view(request):
    name = request.session['name']
    email = request.session['email']
    message = request.session['message']
    context = {
        'name': name,
        'email': email,
        'message': message
    }
    return render(request, 'output.html', context)
