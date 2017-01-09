from django.contrib import admin

from .models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "province", "ecg_field", "ecg_seed")
    fieldsets = [
        (
            "Datos generales", {
                "fields": [
                    "name", "registered_name", "cif_nif", "address", "province",
                    "economic_sector", "legal_form", "legal_form_other",
                    "number_of_employees", "turnover",
                ]
            }
        ),
        (
            "Contacto", {
                "classes": ("collapse",),
                "fields": [
                    "contact_person", "contact_email", "contact_phone",
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
                    "score_a1", "score_b1",
                    "score_c1", "score_c2", "score_c3", "score_c4", "score_c5",
                    "score_d1", "score_d2", "score_d3", "score_d4", "score_d5",
                    "score_e1", "score_e2", "score_e3", "score_e4", "score_e5",
                ]
            }
        ),
    ]

admin.site.register(Organization, OrganizationAdmin)

