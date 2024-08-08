class Param:
    def __init__(self, name, type, desc) -> None:
        self.name = name
        self.type = type
        self.desc = desc

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.type

    def get_desc(self) -> str:
        return self.desc

    def __str__(self):
        return '{}, {}'.format(self.name, self.desc)

class Function:
    def __init__(self) -> None:
        self.name = ''
        self.desc = ''
        self.params = []

    def get_name(self) -> str:
        return self.name

    def get_desc(self) -> str:
        return self.desc

    def add_name(self, n) -> None:
        self.name = n

    def add_desc(self, d) -> None:
        self.desc = d

    def add_param(self, n, t, d) -> None:
        self.params.append(Param(n, t, d))

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.desc, self.params)

class Component:
    def __init__(self) -> None:
        self.name = ''
        self.desc = ''
        self.props = []
        self.functions = []

    def get_name(self) -> str:
        return self.name

    def get_desc(self) -> str:
        return self.desc

    def add_name(self, n) -> None:
        self.name = n

    def add_desc(self, d) -> None:
        self.desc = d

    def add_prop(self, n, t, d) -> None:
        self.props.append(Param(n, t, d))

    def add_func(self, func : Function) -> None:
       self.functions.append(func)

    def props_to_md(self) -> str:
        if len(self.props) == 0:
            return "None"
        md = "| Name | Type | Description | \n |--|--|--|\n"
        for prop in self.props:
            md += "| {}| {} | {} |\n".format(prop.get_name(), prop.get_type(), prop.get_desc())
        return md

    def __str__(self) -> str:
        return '''
        name: {},
        desc: {},
        params: {},
        functions: {}
        '''.format(self.name, self.desc, [p.__str__() for p in self.props], [f.__str__() for f in self.functions])
