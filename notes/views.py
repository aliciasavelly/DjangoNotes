from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def note_list(request):
    return render(request, 'notes/note_list.html', {})

def signup(request):
    import pdb; pdb.set_trace()
    if request.method == 'POST' and 'signup' in request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def write_note(request):
    import pdb; pdb.set_trace()
    if request.method == 'POST' and 'new-note' in request.POST:
        import pdb; pdb.set_trace()
        return redirect('/')
