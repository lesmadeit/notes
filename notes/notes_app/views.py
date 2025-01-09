from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *

def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    notes = Note.objects.filter(Q(title__icontains=q)).order_by("-updated", "-created")
    context = {"notes": notes}
    return render(request, "notes_app/home.html", context)
