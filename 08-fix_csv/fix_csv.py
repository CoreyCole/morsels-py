"""
This week we're going to practice normalizing CSV files. Write a program fix_csv.py that turns a pipe-delimited file into a CSV file. I'll explain how it should work by example.

Your original file will look like this:

Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
You'll then run your script by typing this at the command line:

$ python fix_csv.py cars-original.csv cars.csv
Note : "$" is not typed; that is simply the beginning of the prompt.

Your fixed file should then look like this:

Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
Hint: you'll likely want to use the csv module (in the Python standard library) for this because you'll find yourself struggling pretty quickly without it.

For the first bonus, I want you to allow the input delimiter and quote character to be optionally specified. ✔️

For example any of these should work (all specify input delimiter as pipe and the last two additionally specifies the quote character as single quote):

$ python fix_csv.py --in-delimiter="|" cars.csv cars-fixed.csv
$ python fix_csv.py cars.csv cars-fixed.csv --in-delimiter="|"
$ python fix_csv.py --in-delimiter="|" --in-quote="'" cars.csv cars-fixed.csv
$ python fix_csv.py --in-quote="'" --in-delimiter="|" cars.csv cars-fixed.csv
This bonus will require looking into parsing command-line arguments with Python. There are some standard library modules that can help you out with this. There are 3 different solutions in the standard library actually, but only one I'd recommend.

For the second bonus, automatically detect the delimiter if an in-delimiter value isn't supplied (don't assume it's pipe and quote, figure it out). ✔️

The second bonus is a bit trickier and I don't expect it to work correctly for all files. You'll likely want to consult the csv module documentation if you're going to attempt it.
"""

from sys import exit
from argparse import ArgumentParser
import csv


parser = ArgumentParser(description='Standardizes the given csv file by replacing delimiters and quotes to [ , ] and [ " ]')
parser.add_argument('original_path', type=str,
                    help='The path to the original csv file to be "fixed".')
parser.add_argument('output_path', type=str,
                    help='The path to output the new "fixed" csv file.')
parser.add_argument('--in-delimiter', '--in_delimiter', dest='in_delimiter',
                    help='The delimeter used in the original csv file.')
parser.add_argument('--in-quote', '--in_quote', dest='in_quote',
                    help='The quote used in the original csv file.')
args = parser.parse_args()
original_path: str = args.original_path
output_path: str = args.output_path
in_delimiter: str = args.in_delimiter if args.in_delimiter else None
in_quote: str = args.in_quote if args.in_quote else None

try:
    original_csv_file = open(original_path, 'rt')
except OSError as e:
    print(f'Error reading file [{original_path}]: {str(e)}')
    exit(1)
try:
    output_csv_file = open(output_path, 'wt')
except OSError as e:
    print(f'Error opening file [{output_path}] for writing: {str(e)}')
    exit(1)

if in_delimiter is None or in_quote is None:
    dialect = csv.Sniffer().sniff(original_csv_file.read())
    original_csv_file.seek(0)
    original_csv = csv.reader(original_csv_file, dialect=dialect)
else:
    original_csv = csv.reader(original_csv_file, delimiter=in_delimiter, quotechar=in_quote)

output_csv = csv.writer(output_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for row in original_csv:
    output_csv.writerow(row)

original_csv_file.close()
output_csv_file.close()
