
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def stream_kmers(text, k):
    # Equivalent à énumarateKmers
    # On veut récupérer le kmer et son reverse
    
    #On doit les convertir
    # A = 00, C = 01, T = 10, G =11
    #print(text)
    encodage = {'A':0b00,'C':0b01,'T':0b10,'G':0b11,'Y':0b10,'M':0b01,'R':0b00,'W':0b00,'K':0b11,'S':0b00}
    correspondance = {'A':'T','C':'G','T':'A','G':'C','Y':'A','M':'G','R':'T','W':'T','K':'C','S':'T'}
    
    kmer = 0
    rkmer = 0
    ### Initialisation
    for letter in text[:k]:
        #kmer ->
        kmer <<= 2 #Décale de 2 vers la gauche (un nt après un nt)
        letter_value = encodage[letter]
        kmer+=letter_value
        #print('kmer :',kmer2str(kmer,k))
        
        #reverse kmer
        rkmer >>=2 #Décale de 2 vers la droite (lis à l'envers)
        letter_value = encodage[correspondance[letter]]
        rkmer += letter_value << 2 * (k-1)#On déplace la valeur de la lettre tout devant
        #print('rkmer :',kmer2str(rkmer,k))
        
    #Récurrence
    #On définit le mask
    mask = (1<<(2*k))-1 #On récupère les bits qui correspondent à la longeur d'un kmer
    for letter in text[k:]: #On parcourt le texte on veut récupèrer toute la séquence
        #kmer ->
        kmer <<= 2 #Décale de 2 vers la gauche (un nt après un nt)
        letter_value = encodage[letter]
        kmer+=letter_value
        ## On filtre avec le mask : bits au délà k_mer mis à 0
        kmer &= mask
        #print('kmer :',kmer2str(kmer,k))
        
        
        #reverse kmer
        rkmer >>=2 #Décale de 2 vers la droite (lis à l'envers)
        letter_value = encodage[correspondance[letter]]
        rkmer=(letter_value << 2*(k-1))+rkmer #On déplace la valeur de la lettre tout devant
        rkmer &= mask
        #print('rkmer :',kmer2str(rkmer,k))
        
        yield kmer,rkmer
