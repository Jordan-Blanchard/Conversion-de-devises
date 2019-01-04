# Conversion-de-devises
Il s'agit d'un programme Python permettant de convertir automatiquement des montants d’une devise vers une autre.

Le programme doit être exécuté avec comme seul argument un chemin vers un fichier contenant les données d’initialisation défini comme suit.

La première ligne contient :
• La devise source DS
• Le montant source MS
• La devise de destination DD
Ces informations sont stockées au format DS;MS;DD.

Les lignes suivantes contiennent des taux de change au format :
• La devise source TDS
• La devise de destination TDD
• Le taux de change au format décimal TC
Ces informations sont stockées au format TDS;TDD;TC.

Exemple :
EUR;20;USD
EUR;CHF;1.14651
USD;GBP;0.742190
USD;XPF;100.714
GBP;XPF;135.704
XPF;CHF;0.00960574


Après avoir exécuté, le programme affiche le montant dans la devise de destination, arrondi à deux chiffres après la virgule.

Vous pouvez consulter le fichier "test technique -backend-opengst.pdf" si vous voulez plus d'informations.
