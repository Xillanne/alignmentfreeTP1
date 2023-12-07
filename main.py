from loading import load_directory
from kmers import stream_kmers
import pandas as pd



def jaccard(fileA, fileB, k):
    """Transforme fichiers fasta en set de kmer et calcule leur intersection
    :param array fileA: array de string où chaque string correspond à une séquence
    :param assay fileB: idem fileA
    :param int k: taille du kmer
    :return j: jaccard distance A inter B / A union B"""
    j = 0  # Jaccard distance
    # --- To complete ---
    dico = {}  # Compare kmers
    taille_U = 0  # Taille Union
    taille_I = 0  # Taille Intersection
    for seq in fileA:
        for kmer, rkmer in stream_kmers(seq, k):
            if kmer not in dico:
                dico[kmer] = 1
            else:
                dico[kmer] += 1
            taille_U += 1

    for seq in fileB:
        for kmer, rkmer in stream_kmers(seq, k):
            if kmer in dico:
                taille_I += 1
                dico[kmer] -= 1
                if dico[kmer] == 0:
                    del dico[kmer]
            else:
                taille_U += 1

    j = taille_I / taille_U
    return j




if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    
    filenames = list(files.keys())
    res = pd.DataFrame(index=filenames, columns=filenames)
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            
            # --- Complete here ---

            jaccard_values = jaccard(files[filenames[i]], files[filenames[j]], k)
            print(filenames[i], filenames[j], jaccard_values)
            # Stocker les résultats dans le DataFrame
            res.at[filenames[i], filenames[j]] = jaccard_values
    res.to_csv('Resultats.csv')
