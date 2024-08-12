import os, sys, argparse
from parser import gen_component
from markdown import gen_markdown

def main():
    parser = argparse.ArgumentParser(
        prog='ctp-docgen',
        description='Markdown documentation generator for the CTP react app.',
        epilog='Designed to be used for Bitbuckets wiki.')
    parser.add_argument('input_dir')
    parser.add_argument('output_dir')
    args = parser.parse_args()
    input_path = args.input_dir
    output_path = args.output_dir

    if not os.path.isdir(input_path):
        print('The input directory provided is not valid.')
        sys.exit(1)

    if os.path.isdir(input_path + '/components'):
        comp_arr = []
        for comp_file in os.listdir(input_path + '/components'):
            with open(input_path + '/components/' + comp_file, 'r') as file:
                source = file.read()
                component = gen_component(source)
            comp_arr.append(component.get_name())
            with open(output_path + "" + component.get_name(), 'w') as file:
                content = gen_markdown(component, source)
                file.write(content)
        # write components page
        with open(output_path + "Components", 'w') as file:
            content = "# React Components\n"
            for c in sorted(comp_arr):
                content += "- [{}]({})\n".format(c, c)
            file.write(content)

    else:
        print('There is not components directory.')

    print("Documentation generated!")


if __name__ == "__main__":
    main()
