from django.db import models

from cities.models import Subregion, City


# Alternatives to django-cities for the address
# https://code.activestate.com/pypm/django-postal
# https://github.com/scaleway/postal-address
# https://github.com/furious-luke/django-address
# https://github.com/openvenues/libpostal
# http://django-autocomplete-light.readthedocs.io/en/master/


class OrganizationsManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)


class Organization(models.Model):
    is_active = models.BooleanField(
        null = False, blank = True, default = False,
        verbose_name = "activa"
    )
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
    address_street_number = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "calle y número"
    )
    address_other = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "portal / piso / puerta"
    )
    zipcode = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "código postal"
    )
    city = models.CharField(
        null = False, blank = True, max_length = 100,
        verbose_name = "población"
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
            ("comunidad de bienes", "Comunidad de bienes"),
            ("empresario individual", "Empresario individual"),
            ("sociedad anonima", "Sociedad anónima (S.A.)"),
            ("sociedad civil", "Sociedad civil"),
            ("cooperativa", "Sociedad cooperativa"),
            ("sociedad laboral", "Sociedad laboral"),
            ("sociedad limitada", "Sociedad limitada (S.L.)"),
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
            ("1", "1 (emprendedor-trabajador)"),
            ("2", "2"),
            ("3-5", "3-5"),
            ("6-10", "6-10"),
            ("11-20", "11-20"),
            ("21-50", "21-50"),
            ("51-100", "51-100"),
            ("101-200", "101-200"),
            ("201-350", "201-350"),
            ("351-500", "351-500"),
            ("501-750", "501-750"),
            ("751-1000", "751-1000"),
            ("1001-1500", "1001-1500"),
            ("1501-2500", "1501-2500"),
            (">2500", ">2500"),
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
    website = models.URLField(
        null = False, blank = True,
        verbose_name = "página web"
    )
    contact_email = models.EmailField(
        null = False, blank = False,
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
            ("4.0", "4.0"),
            ("4.1", "4.1"),
            ("5.0", "5.0"),
            ("Rubi-Brilla (RB)-Zaragoza", "Rubi-Brilla (RB)-Zaragoza"),
            ("Versiones anteriores", "Versiones anteriores"),
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

    objects = OrganizationsManager()

    class Meta:
        verbose_name = "Organización"
        verbose_name_plural = "Organizaciones"

