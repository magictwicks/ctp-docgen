import re
from classes import Param, Function, Component

COMMENT_REGEX = r'\/\*[\s\S]*?\*\/'
ELEMENT_REGEX = r'^@(\S+)\s+(.+)$'
PARAM_REGEX = r'^@param\s+\{(\w+)\}\s+(.*)$'

def parse_source(source):
    # Use re.findall to extract comments
    matches = re.findall(COMMENT_REGEX, source)

    # Process matches in a single list comprehension
    formatted_matches = [
        [line.lstrip("* ") for line in match.splitlines()[1:-1]] # strip leading asterisk and spaces and get rid of beginnning and end of comment
        for match in matches
    ]
    return [list(filter(bool, match)) for match in formatted_matches] # get rid of any empty strings in matches


def gen_component(source) -> Component:
    elements = parse_source(source)
    comp = Component()

    for element in elements:
        element_header = re.match(ELEMENT_REGEX, element[0])

        if element_header is None:
            # @TODO: add custom exceptions
            raise Exception("Error: Element type indicator not found")

        match element_header.group(1):
            case 'component':
                desc = ''
                for i in range(1, len(element)):
                    line = re.match(PARAM_REGEX, element[i])
                    if line: # if match, add prop
                        if len(line.groups()) == 2:
                            comp.add_prop(line.group(1), line.group(2))
                        else:
                            comp.add_prop(line.group(1), line.group(2), line.group(3))
                    else: # add to description
                        desc += element[i].replace('\n', ' ')
                comp.add_name(element_header.group(2))
                comp.add_desc(desc)

            case 'function':
                func = Function()
                desc = ''
                for i in range(1, len(element)):
                    line = re.match(PARAM_REGEX, element[i])
                    if line: # if match, add prop
                        func.add_param(line.group(1), line.group(2),  line.group(3))
                    else: # add to description
                        desc += element[i].replace('\n', ' ')
                func.add_name(element_header.group(2))
                func.add_desc(desc)
                comp.add_func(func)

            case _:
                raise Exception('Unknown type in element header')

    return comp
