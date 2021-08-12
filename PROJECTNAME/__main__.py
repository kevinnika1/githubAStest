import sys
import json
import argparse
import logging

from . import __all__ as methods
from . import *

logger = logging.getLogger(__name__)

def main():
    """
    Entry point when calling the module from the command line.

    Run `python -m PROJECTNAME.main -h` for instructions
    """
    parser = argparse.ArgumentParser(description=f'')
    parser.add_argument('method',
                        type=str,
                        choices=methods,
                        help=f'Entry point to call, one of {methods}.')
    parser.add_argument('-c', '--credentials', type=str, default='{}',
                        help='Dictionary of {system={user=, password=}}, encoded as JSON.')
    parser.add_argument('-p', '--parameters', type=str, default='{}',
                        help='Dictionary of parameters, encoded as JSON.')

    args = parser.parse_args()
    
    credentials = json.loads(args.credentials)
    paramters = json.loads(args.parameters)

    ##
    # Use the method name from __all__ to dynamicly select the correct function
    # from the globals() dict.
    ##
    function = globals()[args.method]
    function(credentials, paramters)
  

if __name__ == '__main__':
    main()
