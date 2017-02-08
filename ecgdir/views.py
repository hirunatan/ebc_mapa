from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.forms import ModelForm
from django.urls import reverse_lazy

from .models import Organization

import csv


class IndexView(generic.ListView):
    template_name = "ecgdir/index.html"
    context_object_name = "organizations"

    def get_queryset(self):
        return Organization.objects.active()


class DetailView(generic.DetailView):
    template_name = "ecgdir/detail.html"
    model = Organization


class CSVView(generic.View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="organizaciones_ebc.csv"'

        writer = csv.writer(response)
        writer.writerow([
            "name", "registered_name", "cif_nif", "address_street_number", "address_other",
            "zipcode", "city", "province", "economic_sector", "legal_form", "legal_form_other",
            "number_of_employees", "turnover", "contact_person", "contact_email", "contact_phone",
            "ecg_link_person", "ecg_field", "ecg_seed", "balance_date", "balance_version",
            "balance_version_other", "global_score", "consultant", "auditor", "evaluation",
            "score_a1",  "score_a2",  "score_a3",  "score_a4",  "score_a5",
            "score_b1",  "score_b2",  "score_b3",  "score_b4",  "score_b5",
            "score_c1",  "score_c2",  "score_c3",  "score_c4",  "score_c5",
            "score_d1",  "score_d2",  "score_d3",  "score_d4",  "score_d5",
            "score_e1",  "score_e2",  "score_e3",  "score_e4",  "score_e5",
            "score_n1",  "score_n2",  "score_n3",  "score_n4",  "score_n5",
            "score_n6",  "score_n7",  "score_n8",  "score_n9",  "score_n10",
            "score_n11", "score_n12", "score_n13", "score_n14", "score_n15",
            "score_n16", "score_n17",
        ])
        for organization in Organization.objects.active():
            writer.writerow([
                organization.name,
                organization.registered_name,
                organization.cif_nif,
                organization.address_street_number,
                organization.address_other,
                organization.zipcode,
                organization.city,
                organization.province,
                organization.economic_sector,
                organization.legal_form,
                organization.legal_form_other,
                organization.number_of_employees,
                organization.turnover,
                organization.contact_person,
                organization.contact_email,
                organization.contact_phone,
                organization.ecg_link_person,
                organization.ecg_field,
                organization.ecg_seed,
                organization.balance_date,
                organization.balance_version,
                organization.balance_version_other,
                organization.global_score,
                organization.consultant,
                organization.auditor,
                organization.evaluation,
                organization.score_a1,
                organization.score_a2,
                organization.score_a3,
                organization.score_a4,
                organization.score_a5,
                organization.score_b1,
                organization.score_b2,
                organization.score_b3,
                organization.score_b4,
                organization.score_b5,
                organization.score_c1,
                organization.score_c2,
                organization.score_c3,
                organization.score_c4,
                organization.score_c5,
                organization.score_d1,
                organization.score_d2,
                organization.score_d3,
                organization.score_d4,
                organization.score_d5,
                organization.score_e1,
                organization.score_e2,
                organization.score_e3,
                organization.score_e4,
                organization.score_e5,
                organization.score_n1,
                organization.score_n2,
                organization.score_n3,
                organization.score_n4,
                organization.score_n5,
                organization.score_n6,
                organization.score_n7,
                organization.score_n8,
                organization.score_n9,
                organization.score_n10,
                organization.score_n11,
                organization.score_n12,
                organization.score_n13,
                organization.score_n14,
                organization.score_n15,
                organization.score_n16,
                organization.score_n17,
            ])

        return response


class AddForm(ModelForm):
    class Meta:
        model = Organization
        fields = (
            "name", "registered_name", "cif_nif", "address_street_number", "address_other",
            "zipcode", "city", "province", "economic_sector", "legal_form", "legal_form_other",
            "number_of_employees", "turnover", "contact_person", "contact_email", "contact_phone",
            "ecg_link_person", "ecg_field", "ecg_seed", "balance_date", "balance_version",
            "balance_version_other", "global_score", "consultant", "auditor", "evaluation",
            "score_a1",  "score_a2",  "score_a3",  "score_a4",  "score_a5",
            "score_b1",  "score_b2",  "score_b3",  "score_b4",  "score_b5",
            "score_c1",  "score_c2",  "score_c3",  "score_c4",  "score_c5",
            "score_d1",  "score_d2",  "score_d3",  "score_d4",  "score_d5",
            "score_e1",  "score_e2",  "score_e3",  "score_e4",  "score_e5",
            "score_n1",  "score_n2",  "score_n3",  "score_n4",  "score_n5",
            "score_n6",  "score_n7",  "score_n8",  "score_n9",  "score_n10",
            "score_n11", "score_n12", "score_n13", "score_n14", "score_n15",
            "score_n16", "score_n17",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from cities.models import Subregion
        self.fields['province'].queryset = \
            Subregion.objects.order_by('name').filter(region__country__code="ES")


class AddView(generic.edit.CreateView):
    template_name = "ecgdir/add.html"
    model = Organization
    form_class = AddForm
    success_url = reverse_lazy("add-ok")


class AddOkView(generic.TemplateView):
    template_name = "ecgdir/add_ok.html"

