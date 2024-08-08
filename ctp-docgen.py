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
    path = args.input_dir

    if not os.path.isdir(path):
        print('The input directory provided is not valid.')
        sys.exit(1)

    if os.path.isdir(path + '/components'):
        for comp_file in os.listdir(path + '/components'):
            with open(path + '/components/' + comp_file, 'r') as file:
                source = file.read()
                component = gen_component(source)
                print(gen_markdown(component, source))
    else:
        print('There is not components directory.')


if __name__ == "__main__":
    main()
