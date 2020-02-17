import sys
import os
import json
import importlib

def dispatch_RPC(input_data, pkg=''):
    """Dispatch."""
    if input_data:
        input_ = json.loads(input_data)
        method = input_['method']
        args = input_['args']
        kwargs = input_['kwargs']

    importlib.import_module(pkg)

    return ''


def main(PKG):
    """...."""
    # Database, input and output files ...
    DATABASE_URI = os.environ.get('DATABASE_URI')
    INPUT_FILE = '/app/input.txt'
    OUTPUT_FILE = '/app/output.txt'

    # Input/output defaults
    input_data = None
    output_data = ''

    # Get crackin'
    print(f'Using {DATABASE_URI} as database')

    # Load the input from disk
    print(f'Loading {INPUT_FILE}')

    try:
        with open(INPUT_FILE) as fp:
            input_data = fp.read()
    except Exception as e:
        print(f'Could not load input: {e}')

    # Do some dispatching ...
    output_data = dispatch_RPC(input_data, PKG)

    # Write output ...
    # with open(OUTPUT_FILE, 'w') as fp:
    #     fp.write(output_data)

    # All done ...
    print('Done!')



# ------------------------------------------------------------------------------
# __main__
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    PKG = sys.argv[1]
    main(PKG)