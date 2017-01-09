from ecgdir.models import Organization
from graphene import AbstractType, relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class OrganizationNode(DjangoObjectType):

    class Meta:
        model = Organization
        interfaces = (relay.Node, )
        filter_fields = ["name", "registered_name", "cif_nif", "province", "ecg_field"]


class Query(AbstractType):
    organization = relay.Node.Field(OrganizationNode)
    all_organizations = DjangoFilterConnectionField(OrganizationNode)
