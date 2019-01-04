# Conversion-de-devises
Il s'agit d'un programme Python permettant de convertir automatiquement des montants d’une devise vers une autre.

Le programme doit être exécuté avec comme seul argument un chemin vers un fichier contenant les données d’initialisation défini comme suit.

La première ligne contient :<br />
• La devise source DS<br />
• Le montant source MS<br />
• La devise de destination DD<br />
Ces informations sont stockées au format DS;MS;DD.<br />

Les lignes suivantes contiennent des taux de change au format :<br />
• La devise source TDS<br />
• La devise de destination TDD<br />
• Le taux de change au format décimal TC<br />
Ces informations sont stockées au format TDS;TDD;TC.

Exemple :<br />
EUR;20;USD<br />
EUR;CHF;1.14651<br />
USD;GBP;0.742190<br />
USD;XPF;100.714<br />
GBP;XPF;135.704<br />
XPF;CHF;0.00960574<br />

<br />
Après avoir exécuté, le programme affiche le montant dans la devise de destination, arrondi à deux chiffres après la virgule.

Vous pouvez consulter le fichier "test technique-backend.pdf" si vous voulez plus d'informations.
