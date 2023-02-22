""" read in genotypes from VCF file and predict outcome """
import sys
import os
import argparse
import numpy as np
import pickle
from tqdm import tqdm
import subprocess as sp

parser = argparse.ArgumentParser(description='Predict outcome from VCF file')
parser.add_argument('--vcf', help='VCF file', required=True)
parser.add_argument('--model', help='model file', required=True)
parser.add_argument('--out', help='output file', required=True)
args = parser.parse_args()

# load model
items = pickle.load(open(args.model, "rb"))
clf = items['model']
positions = items['positions']



# extract genotypes
genos = {}
for l in sp.Popen(r"bcftools query -f '%POS[\t%GT\n]' "+ "test.vcf.gz",shell=True,stdout=sp.PIPE).stdout:
    row = l.decode().strip().split()
    if row[1]!="0/0":
        genos[int(row[0])] = 1
    else:
        genos[int(row[0])] = 0


for p in positions:
    if p not in genos:
        genos[p] = 0

genos = [[genos[p] for p in positions]]
# predict outcome
pred = clf.predict(genos)
# write output
with open(args.out, "w") as f:
    f.write("drug,prediction\npenicillin,%s\n" % pred[0])