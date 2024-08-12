from classes import Component

# TODO: Add functions later
def gen_markdown(comp : Component, source: str):
    md = ("# {}\n"
        "← [Components](Components)\n"
        "## Description\n"
        "{}\n"
        "## Props\n"
        "{}\n"
        "## Source\n"
        "```\n{}\n```").format(comp.get_name(), comp.get_desc(), comp.props_to_md(), source)
    return md
