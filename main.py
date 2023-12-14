from loading import load_directory
from kmers import stream_kmers



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
        for res in stream_kmers(seq, k):
            kmer = min(res) #On prend le kmer canonique (ie le plus petit)
            #print(kmer)
            # Permet de comparer la même chose dans les deux séquences
            if kmer not in dico:
                dico[kmer] = 1
            else:
                dico[kmer] += 1
            taille_U += 1
            #print(taille_U)
    #print('\n')
    for seq in fileB:
        for res in stream_kmers(seq, k):
            kmer = min(res) #On prend le kmer canonique (ie le plus petit)
            #print(kmer)
            if kmer in dico:
                taille_I += 1
                dico[kmer] -= 1
                if dico[kmer] == 0:
                    del dico[kmer]
            else:
                taille_U += 1
            #print(taille_U)
    j = taille_I / taille_U
    return j




if __name__ == "__main__":
	#seqA=['ATGCATGC']
	#seqB=['ATGCCGTA']
	#j=jaccard(seqA,seqB,3)
	#print(j)

    # Load all the files in a dictionary
    files = load_directory("../data")
    k = 21
    
    filenames = list(files.keys())
    jaccard_table = {}

    for i in range(len(files)):
        for j in range(i+1, len(files)):
            filename_i = filenames[i]
            filename_j = filenames[j]

            jaccard_values = jaccard(files[filename_i], files[filename_j], k)

            # Store the Jaccard value in the table
            if filename_i not in jaccard_table:
                jaccard_table[filename_i] = {}
            jaccard_table[filename_i][filename_j] = jaccard_values

            # Repeat for the other direction since the matrix is symmetric
            if filename_j not in jaccard_table:
                jaccard_table[filename_j] = {}
            jaccard_table[filename_j][filename_i] = jaccard_values

            # Print the results if needed
            print(filename_i, filename_j, jaccard_values)

    # Print or save the Jaccard table
    print("Jaccard Table:")
    for filename_i in filenames:
        print("\t", filename_i.split('_')[1], end="")
    print()
    for filename_i in filenames:
        print(filename_i.split('_')[1], end="")
        for filename_j in filenames:
            if filename_j in jaccard_table[filename_i]:
                print("\t", jaccard_table[filename_i][filename_j], end="")
            else:
                print("\t", "-", end="")
        print()

