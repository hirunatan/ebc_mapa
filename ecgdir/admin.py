from django.contrib import admin

from .models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "province", "ecg_field", "ecg_seed")
    fieldsets = [
        (
            "Datos generales", {
                "fields": [
                    "is_active", "name", "registered_name", "cif_nif", "economic_sector",
                    "legal_form", "legal_form_other", "number_of_employees",
                    "turnover",
                ]
            }
        ),
        (
            "Contacto", {
                "classes": ("collapse",),
                "fields": [
                    "address_street_number", "address_other", "zipcode", "city",
                    "province", "contact_person", "contact_email", "contact_phone",
                ]
            }
        ),
        (
            "Datos EBC", {
                "classes": ("collapse",),
                "fields": [
                    "ecg_link_person", "ecg_field", "ecg_seed", "balance_date",
                    "balance_version", "balance_version_other", "global_score",
                    "consultant", "auditor", "evaluation",
                ]
            }
        ),
        (
            "Matriz de resultados", {
                "classes": ("collapse",),
                "fields": [
                    "score_a1",  "score_a2",  "score_a3",  "score_a4",  "score_a5",
                    "score_b1",  "score_b2",  "score_b3",  "score_b4",  "score_b5",
                    "score_c1",  "score_c2",  "score_c3",  "score_c4",  "score_c5",
                    "score_d1",  "score_d2",  "score_d3",  "score_d4",  "score_d5",
                    "score_e1",  "score_e2",  "score_e3",  "score_e4",  "score_e5",
                    "score_n1",  "score_n2",  "score_n3",  "score_n4",  "score_n5",
                    "score_n6",  "score_n7",  "score_n8",  "score_n9",  "score_n10",
                    "score_n11", "score_n12", "score_n13", "score_n14", "score_n15",
                    "score_n16", "score_n17",
                ]
            }
        ),
    ]

admin.site.register(Organization, OrganizationAdmin)

