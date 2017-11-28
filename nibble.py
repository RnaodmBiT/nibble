import os
from argparse import ArgumentParser
import lexer

# Parse the command line arguments
parser = ArgumentParser()
parser.add_argument("-d", "--directory", type=str, help="Directory to parse structures from.", default="samples")
args = parser.parse_args()

# Get the list of input files from the source directory
input_files = []
for root, dirs, files in os.walk(args.directory):
    for name in files:
        input_files.append(os.path.join(root, name))

# Go through all of the input files and process them
for filename in input_files:
    print("Processing nibble: {}".format(filename))

    lexer.lexer.input(open(filename).read())

    # Just print out the tokens for now. Just for testing
    while True:
        token = lexer.lexer.token()
        if not token:
            break

        print(token)