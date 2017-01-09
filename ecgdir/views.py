from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Organization


class IndexView(generic.ListView):
    template_name = "ecgdir/index.html"
    context_object_name = "organizations"

    def get_queryset(self):
        return Organization.objects.all()


class DetailView(generic.DetailView):
    template_name = "ecgdir/detail.html"
    model = Organization

