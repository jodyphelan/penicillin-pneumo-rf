from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import pickle

genos = []
offset = 3
from tqdm import tqdm
positions = []
for l in tqdm(open("snps.mat.bin")):
    row = l.strip().split()
    if row[0]=="chr":
        header = row
        for i in range(offset,len(row)):
            genos.append([])
        continue
    positions.append(int(row[1]))
    for i in range(offset,len(row)):
        if row[i] == "N":
            row[i] = "0"
        genos[i-offset].append(row[i])


pheno = []
for l in open("resistances.pheno"):
    row = l.strip().split()
    if row[0]=="samples": continue
    pheno.append(int(row[1]))

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(genos, pheno)

pickle.dump({"model":clf,"positions":positions}, open("model.pkl","wb"))