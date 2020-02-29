# eval_word_embeddings
Evaluate the word embeddings similarity with ease

## Usage
```
python3 evaluate.py --embeddings [embedding.file] --datasets [word-sim.folder]
```

## Example
```
git clone https://github.com/chihming/eval_word_embeddings
wget http://vectors.nlpl.eu/repository/20/6.zip
unzip 6.zip
python3 evaluate.py --embeddings model.txt --datasets data/word-sim/
```
this example receieves
```
Serial              Dataset         # Pairs       Not found       Rho (all)     Rho (found)
     1     EN-MTurk-287.txt             287              67          0.4739          0.6718
     2    EN-WS-353-ALL.txt             353               0          0.7126          0.7177
     3        EN-YP-130.txt             130               0          0.5594          0.5093
     4    EN-WS-353-REL.txt             252               0          0.5759          0.6463
     5         EN-MC-30.txt              30               0          0.5504          0.8390
     6     EN-MTurk-771.txt             771               2          0.5160          0.6342
     7     EN-MEN-TR-3k.txt            3000              10          0.5472          0.7408
     8   EN-RW-STANFORD.txt            2034             616          0.4629          0.5069
     9         EN-RG-65.txt              65               0          0.4541          0.8025
    10    EN-SIMLEX-999.txt             999               4          0.3599          0.3965
    11      EN-VERB-143.txt             144               0          0.3622          0.4087
    12    EN-WS-353-SIM.txt             203               0          0.3652          0.7945
    13  EN-SimVerb-3500.txt            3500              73          0.2857          0.2961
```
