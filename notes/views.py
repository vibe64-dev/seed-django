from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import NoteForm
from .models import Note

RECENT_NOTES = 20


def home(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Note saved.")
            return redirect("home")
    else:
        form = NoteForm()
    notes = Note.objects.all()[:RECENT_NOTES]
    return render(request, "notes/home.html", {"form": form, "notes": notes})
