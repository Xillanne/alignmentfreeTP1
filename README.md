

# Alignment free - TP 1

L'objectif du TP est de comparer 5 especes de bactéries entre elles.
Vous trouverez les données en suivant [ce lien](https://we.tl/t-ACiDxJko7s)

## Composer le TP

Vous devez forker ce projet puis compléter ses fonctions.
Le rendu sera le dépot git dans lequel vous aurrez forké.

Le but est d'obtenir toutes les distances paire à paire des différentes bactéries.
Vous devez compléter le README pour y afficher la matrice des distances des bactéries.
Vous devez également y indiquer le temps d'exécution qu'il a fallu pour calculer cette matrice ainsi que l'espace mémoire maximale. Pour cela vous pouvez utiliser la commande ```/usr/bin/time -v```.

En observant les distances obtenues, que pouvez-vous dire des espèces présentes dans cet échantillon ?

### Résultats MAJ ###
On a des nucléotides qui ne sont pas défini dans nos séquences : on décide de les garder et des les attribuer à un de nucléotides qu'ils peuvent représenter, ainsi on a comme encodage :
$${'A':0b00,'C':0b01,'T':0b10,'G':0b11,'Y':0b10,'M':0b01,'R':0b00,'W':0b00,'K':0b11,'S':0b00}$$

Les fonctions ont été modifiées pour garder les k_mers canoniques et l'initialisation a été modifiée. On obtient alors les résultats suivants :

Jaccard Table:
	 020526745.1	 020535205.1	 014892695.1	 000006945.2	 008244785.1
020526745.1	 -	 0.6139027671100382	 0.0019466253653915354	 0.019091889920944443	 0.019327764464620357
020535205.1	 0.6139027671100382	 -	 0.0039007084501784146	 0.01791173059511927	 0.018016662252293467
014892695.1	 0.0019466253653915354	 0.0039007084501784146	 -	 0.0017591971757668513	 0.0017684627614227755
000006945.2	 0.019091889920944443	 0.01791173059511927	 0.0017591971757668513	 -	 0.93785631871861
008244785.1	 0.019327764464620357	 0.018016662252293467	 0.0017684627614227755	 0.93785631871861	 -

Le retour de la commande time -v donne :
Command being timed: "python3 main.py"
        User time (seconds): 64.25
        System time (seconds): 0.92
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 1:05.28
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 410804
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 433023
        Voluntary context switches: 1
        Involuntary context switches: 76
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0


Nos résultats indiquent que 008244785.1 et 000006945.2 sont extrémement proches, il doit s'agir de bactérie de la même espèces, voire de la même souche car elles ont une distance de Jaccard de 0.94.
020535205.1 et 020526745.1 sont proches, avec un indice de Jaccard de 0.61, on peut supposer qu'elles sont de la même espèce mais dans des environnements différents ou d'espèces différentes mais proches.
Les autres bactéries sont toutes très différentes les une des autres ~0.

# TP 2
Implémenter la méthode de sketching de notre choix

On obtient les résultats ci dessous en utilisant un échantillonnage de 900.

Jaccard Table:
         000006945.2     020526745.1     008244785.1     020535205.1     014892695.1
000006945.2      -       0.01637492941840768     0.9047619047619048      0.017524024872809497    0.0
020526745.1      0.01637492941840768     -       0.01637492941840768     0.41843971631205673     0.0005558643690939411
008244785.1      0.9047619047619048      0.01637492941840768     -       0.017524024872809497    0.0
020535205.1      0.017524024872809497    0.41843971631205673     0.017524024872809497    -       0.0033444816053511705
014892695.1      0.0     0.0005558643690939411   0.0     0.0033444816053511705   -


        Command being timed: "python3 main.py"
        User time (seconds): 50.97
        System time (seconds): 0.06
        Percent of CPU this job got: 100%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:51.03
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 38844
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 14328
        Voluntary context switches: 1
        Involuntary context switches: 14
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0

Les résultats sont similaires à ceux obtenus précédemment. Avec les bactéries 008244785.1 et 000006945.2 avec une distance de jaccard de 0.9 et les bactéries 020535205.1 et 020526745.1  qui sont proches, cependant leur similarité est moins élevées que précédemment avec 0.42, cela peut s'expliquer par l'échantillonnage, prendre les 900 plus petits kmer ne semble pas refleter avec précision la distribution globale des kmers.
On remarque que comme attendu le sketching permet d'executer plus rapidement (51 sec contre 1min:05) avec un temps système qui passe de 0.92 sec à 0.06, ce qui suggère une utilisation plus efficace des ressources. L'utilisation avec les sketching utilise moins de mémoire avec la taille maximale de l'ensemble résident qui est à 38844 kbytes alors qu'elle était à 410804 précédemment.
On a bien réussi à optimiser notre comparaison de séquence.