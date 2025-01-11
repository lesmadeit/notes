from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    notes = Note.objects.filter(Q(title__icontains=q)).order_by("-updated", "-created")
    context = {"notes": notes}
    return render(request, "notes_app/home.html", context)


def display_note(request, pk):
    note = Note.objects.get(id=pk)
    context = {"note": note}
    return render(request, "notes_app/display_note.html", context)


def add_note(request):
    if request.method == "POST":
        Note(
            title = request.POST.get("title"),
            body = request.POST.get("body"),
        ).save()
        return redirect("home")
    return render(request, "notes_app/edit_note.html")


def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == "POST":
        note.delete()
        return redirect("home")
    context = {"note": note}
    return render(request, "notes_app/delete_note.html", context)


def edit_note(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == "POST":
        note.title = request.POST.get("title")
        note.body = request.POST.get("body")
        note.save()
        return redirect("home")
    context = {"note": note}
    return render(request, "notes_app/edit_note.html", context)
