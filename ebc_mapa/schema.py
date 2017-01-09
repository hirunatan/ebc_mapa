import ecgdir.schema
import graphene


class Query(ecgdir.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
