
class Model:

    identifier = ''   # Class name
    ref = ''          # json file reference, used for injection later in process
    namespace = ''    # package -> com.barrettotte.models
    access = "public" # might never change?
    imports = []      # package imports
    annotations = []  # class level annotations (jackson)
    properties = []   # 
    inheritance = []  # extends
    interfaces = []   # might never be used

    def __init__(self, identifier, ref):
        self.identifier = identifier
        self.ref = ref

    def __str__(self):
        return "\n".join([
            "identifier:  " + self.identifier,
            "ref       :  " + self.ref,
            "access:      " + self.access,
            "namespace:   " + str(self.namespace),
            "inheritance: " + str(self.inheritance),
            "imports:     " + str(self.imports),
            "properties:  " + str(self.properties)
        ])


class Property:
    identifier = ""
    kind = ""           # class type
    access = "private"  # [private,protected]
    annotations = []    # unused
    required = False    # might be able to use for param ctor later?
    max_items = None    # used for primitive arrays -> ...new String[10]
    default = None      #
    parse_to = None     # attempt to parse property to this class...not guaranteed results

    def __init__(self, identifier, kind, access):
        self.identifier = identifier
        self.kind = kind
        self.access = access

    def __str__(self):
        return self.kind + " " + self.identifier

    def __repr__(self):
        return self.__str__()

