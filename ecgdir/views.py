from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.forms import ModelForm


from .models import Organization


class IndexView(generic.ListView):
    template_name = "ecgdir/index.html"
    context_object_name = "organizations"

    def get_queryset(self):
        return Organization.objects.all()


class DetailView(generic.DetailView):
    template_name = "ecgdir/detail.html"
    model = Organization


class AddForm(ModelForm):
    class Meta:
        model = Organization
        fields = (
            "name", "registered_name", "cif_nif", "address", "province",
            "economic_sector", "legal_form", "legal_form_other", "number_of_employees",
            "turnover", "contact_person", "contact_email", "contact_phone",
            "ecg_link_person", "ecg_field", "ecg_seed", "balance_date", "balance_version",
            "balance_version_other", "global_score", "consultant", "auditor",
            "evaluation", "score_a1", "score_b1", "score_c1", "score_c2", "score_c3",
            "score_c4", "score_c5", "score_d1", "score_d2", "score_d3", "score_d4",
            "score_d5", "score_e1", "score_e2", "score_e3", "score_e4", "score_e5",
        )


class AddView(generic.edit.CreateView):
    template_name = "ecgdir/add.html"
    model = Organization
    form_class = AddForm

