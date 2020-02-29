import os
import argparse
from collections import defaultdict
from scipy import spatial
from scipy.stats import spearmanr

parser = argparse.ArgumentParser(description='Argument Parser')
parser.add_argument('--embeddings', required=True, help='file for the embeddings')
parser.add_argument('--datasets', required=True, help='folder for word datasets')
args = parser.parse_args()

embeddings = {}
with open(args.embeddings, 'r') as f:
    for line in f:
        try:
            line = line.rstrip().split()
            embeddings[line[0]] = list(map(float, line[1:]))
        except:
            pass

print("%6s %20s %15s %15s %15s %15s" % ("Serial", "Dataset", "# Pairs", "Not found", "Rho (all)", "Rho (found)"))
anwsers, predictions = [], []
anwsers_all, predictions_all = [], []
for e, file_name in enumerate(os.listdir(args.datasets), 1):
    del anwsers[:]
    del predictions[:]
    not_found, total_size = 0, 0
    file_path = os.path.join(args.datasets, file_name)
    with open(file_path, 'r') as f:
        for line in f:
            word1, word2, val = line.rstrip().split()
            anwsers_all.append(float(val))
            if word1 in embeddings and word2 in embeddings:
                anwsers.append(float(val))
                predictions.append(1.-spatial.distance.cosine(embeddings[word1], embeddings[word2]))
                predictions_all.append(predictions[-1])
            else:
                not_found += 1
                predictions_all.append(0.)
            total_size += 1
        print("%6s %20s %15s %15s %15.4f %15.4f" % (
            str(e), file_name, str(total_size), str(not_found),
            spearmanr(anwsers_all, predictions_all)[0],
            spearmanr(anwsers, predictions)[0]))

