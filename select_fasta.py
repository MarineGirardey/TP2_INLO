#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:04:02 2021

@author: Marine Girardey
"""
# Add argparse
import argparse

program_descrption = '''
What the program does.
'''

def create_parser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-i','--inputfile',
                        help="Path",
                        default=None,
                        metavar="FASTA",
                        type=argparse.FileType('r'),
                        required=True)
    
    parser.add_argument('-s','--sequence',
                        help="Path",
                        default=None,
                        required=True,
                        nargs="+")
    return parser

def fasta_file(inputfile,sequence):
    seq_dict = {}
    for lines in inputfile:
        for elem in sequence:
            if elem in lines:
                next_line = next(inputfile)
                accession = lines.strip('>').strip('\n')
                full_seq = next_line.strip('>').strip('\n')
                seq_dict[accession]=full_seq
    print(seq_dict)

def main():
	parser = create_parser()
	args = parser.parse_args() ; args = args.__dict__
	fasta_file(args["inputfile"],args["sequence"])

if __name__ == "__main__": 
    main()
