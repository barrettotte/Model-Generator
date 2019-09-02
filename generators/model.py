
class Model:

    identifier = ''
    namespace = ''
    access = "public"
    imports = []
    annotations = []
    properties = []
    inheritance = []
    interfaces = []

    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return "\n".join([
            "identifier:  " + self.identifier,
            #"access:      " + self.access,
            "namespace:   " + str(self.namespace),
            "inheritance: " + str(self.inheritance),
            "imports:     " + str(self.imports),
            "properties:  " + str(self.properties)
        ])


class Property:
    identifier = ""
    kind = ""          
    obj = None
    access = "private"  # [private,protected]
    annotations = []    # String[]
    getter = []         # String[]
    setter = []         # String[]

    def __init__(self, identifier, kind, access):
        self.identifier = identifier
        self.kind = kind
        self.access = access

    def __str__(self):
        return self.kind + " " + self.identifier

    def __repr__(self):
        return self.__str__()

