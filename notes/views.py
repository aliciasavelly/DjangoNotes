from django.shortcuts import render

def note_list(request):
    return render(request, 'notes/note_list.html', {})
