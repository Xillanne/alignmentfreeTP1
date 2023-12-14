from loading import load_directory
from kmers import stream_kmers
from sketching import sketching


def jaccard(s1,s2, k):
    j = 0  # Jaccard distance
    # --- To complete ---
    dico = {}  # Compare kmers
    taille_U = 0  # Taille Union
    taille_I = 0  # Taille Intersection
    for kmer in s1:
            # Permet de comparer la même chose dans les deux séquences
            if kmer not in dico:
                dico[kmer] = 1
            else:
                dico[kmer] += 1
            taille_U += 1

    for kmer in s2:
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
    #seqA=['ATGCATGC']
    #seqB=['ATGCCGTA']
    #for i in list(range(1,7)):
    #    sketchA=list(sketching(seqA, 3, i))
    #    sketchB=list(sketching(seqB, 3, i))
    #    j=jaccard(sketchA, sketchB, 3)
    #    print(i,j)
    
    
    # Load all the files in a dictionary
    files = load_directory("../data")
    k = 21
    
    filenames = list(files.keys())
    jaccard_table = {}

    for i in range(len(files)):
        for j in range(i+1, len(files)):
            filename_i = filenames[i]
            filename_j = filenames[j]

            #jaccard_values = jaccard(files[filename_i], files[filename_j], k)

            #Echantillonnage des deux individus
            #FAUT ADAPTER JACCARD POUR SU'IL fonctionne sur ça
            sketchA = list(sketching(files[filename_i], k, 900))
            sketchB = list(sketching(files[filename_j], k, 900))
            jaccard_values = jaccard(sketchA, sketchB, k)
            
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
