

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


|                           | GCF_000006945.2_ASM694v2_genomic.fna | GCF_008244785.1_ASM824478v1_genomic.fna | GCF_014892695.1_ASM1489269v1_genomic.fna | GCF_020526745.1_ASM2052674v1_genomic.fna | GCF_020535205.1_ASM2053520v1_genomic.fna |
|---------------------------|----------------------------------------|-------------------------------------------|---------------------------------------------|----------------------------------------|----------------------------------------|
| GCF_000006945.2_ASM694v2_genomic.fna |                                      | 0.9373626421312458                        | 0.001550675872048986                        | 0.012140803514976201                   | 0.003013548168815185                   |
| GCF_008244785.1_ASM824478v1_genomic.fna |                                      |                                           | 0.001557468892236945                        | 0.012245770914016619                   | 0.003125830417644714                   |
| GCF_014892695.1_ASM1489269v1_genomic.fna |                                      |                                           |                                             | 0.0015157390722817707                  | 0.002382203690118471                   |
| GCF_020526745.1_ASM2052674v1_genomic.fna |                                      |                                           |                                             |                                      | 0.07879644967649506                    |
| GCF_020535205.1_ASM2053520v1_genomic.fna |                                      |                                           |                                             |                                      |                                        |


La distance de jaccard mesure la similarité entre des séquences, la majorité des génomes de ces bactéries sont très éloignés les uns des autres car les indices sont proches de 0. Le bactéries GCF_000006945.2 et GCF_008244785.1 au contraire ont des séquences très similaires. On peut imagine qu'on a deux bactéries de la même espèce et que les autres sont d'espèces différentes éloignées.

real    0m48,420s
user    0m47,216s
sys     0m1,112s
