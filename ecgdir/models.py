from django.db import models

from cities.models import Subregion


class Organization(models.Model):
    name = models.CharField(
        null = False, blank = False, max_length = 50,
        verbose_name = "nombre"
    )
    registered_name = models.CharField(
        null = False, blank = True, max_length = 50,
        verbose_name = "razón social"
    )
    cif_nif = models.CharField(
        null = False, blank = True, max_length = 10,
        verbose_name = "cif/nif"
    )
    address = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "dirección"
    )
    province = models.ForeignKey(
        Subregion,
        null = True, blank = True,
        verbose_name = "provincia",
        on_delete = models.SET_NULL,
        limit_choices_to = {"region__country__code": "ES"}
    )
    economic_sector = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "sector económico"
    )
    legal_form = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "forma jurídica",
        choices = (
            ("autonomo", "trabajador autónomo"),
            ("cooperativa", "cooperativa"),
            ("SL", "sociedad de responsabilidad limitada (S.L.)"),
            ("comunidad de bienes", "comunidad de bienes"),
            ("SA", "sociedad anónima (S.A.)"),
            ("SC", "sociedad civil"),
            ("otra", "otra"),
        )
    )
    legal_form_other = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "forma jurídica (otros)"
    )
    number_of_employees = models.CharField(
        null = False, blank = True, max_length = 20,
        verbose_name = "número de empleados",
        choices = (
            ("0", "0 (emprendedor-trabajador)"),
            ("1-3", "1-3"),
            ("4-10", "4-10"),
            ("11-25", "10-25"),
            ("26-50", "26-50"),
            ("51-100", "51-100"),
            ("+100", "+100"),
        )
    )
    turnover = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "facturación"
    )
    contact_person = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "persona de contacto"
    )
    contact_email = models.EmailField(
        null = False, blank = True,
        verbose_name = "email de contacto"
    )
    contact_phone = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "teléfono de contacto"
    )
    ecg_link_person = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "contacto en la EBC"
    )
    ecg_field = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "campo de energía"
    )
    ecg_seed = models.CharField(
        null = False, blank = False, max_length = 1,
        verbose_name = "semilla EBC",
        choices = (
            ("-", "simpatizante"),
            ("1", "semilla 1"),
            ("2", "semilla 2"),
            ("3", "semilla 3"),
        )
    )
    balance_date = models.DateField(
        null = True, blank = True,
        verbose_name = "fecha del balance"
    )
    balance_version = models.CharField(
        null = False, blank = True, max_length = 20,
        verbose_name = "versión utilizada de la matriz",
        choices = (
            ("4.1", "4.1"),
            ("Rubi-Brilla (RB)-Zaragoza", "Rubi-Brilla (RB)-Zaragoza"),
            ("Versiones anteriores", "Versiones anteriores"),
            ("5.0", "5.0"),
            ("otra", "otra"),
        )
    )
    balance_version_other = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "versión utilizada (otra)"
    )
    global_score = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación global"
    )
    consultant = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "consultor"
    )
    auditor = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "auditor"
    )
    evaluation = models.TextField(
        null = False, blank = True,
        verbose_name = "valoración y buenas prácticas detectadas"
    )
    score_a1 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación A1"
    )
    score_b1 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación B1"
    )
    score_c1 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación C1"
    )
    score_c2 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación C2"
    )
    score_c3 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación C3"
    )
    score_c4 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación C4"
    )
    score_c5 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación C5"
    )
    score_d1 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación D1"
    )
    score_d2 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación D2"
    )
    score_d3 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación D3"
    )
    score_d4 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación D4"
    )
    score_d5 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación D5"
    )
    score_e1 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación E1"
    )
    score_e2 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación E2"
    )
    score_e3 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación E3"
    )
    score_e4 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación E4"
    )
    score_e5 = models.PositiveIntegerField(
        null = True, blank = True,
        verbose_name = "puntuación E5"
    )

    class Meta:
        verbose_name = "Organización"
        verbose_name_plural = "Organizaciones"

