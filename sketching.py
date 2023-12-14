#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:08:24 2023

@author: 3708174
"""
import heapq
from kmers import stream_kmers, kmer2str
from loading import load_fna


def sketching(seq,k,s):
    sketch = [float('inf')]*s #On définit la liste de départ
    #sketch=[10,5,4,9,1,7,50]
    sketch = [-i for i in sketch] #On la rend négative pour pouvoir extraire le max
    heapq.heapify(sketch) #Transforme en heapq arbre binaire
    for f in seq: #Parce qu'on regarde des liste de séquence
        for res in stream_kmers(f, k):
            kmer = min(res) #prend kmer canonique
            #Le max correspond à la racine de l'arbre négative
            elem = -sketch[0]
            #print(elem)
            #print(sketch)
            #print(kmer,elem,sketch)
            #break
            if kmer < elem: #si kmer plus petit
                heapq.heappushpop(sketch,-kmer) #On retire le max et remplace par le kmer
        
    sketch = [-i for i in sketch]
    return sketch
    
#filename=('/users/nfs/Etu4/3708174/Documents/PHYG/TME6/data/GCF_000006945.2_ASM694v2_genomic.fna')
#f=load_fna(filename)

#sketching(f[0], 25, 40)
#for i in sketching(['ATGCATGC'], 3, 4):
#    print(kmer2str(i,3))