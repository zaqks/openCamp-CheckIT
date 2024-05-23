<img width=100% src="https://github.com/zaqks/openCamp-CheckIT/blob/main/docs/Screenshot_20240217-151849.jpg"></img>

 
demo video
<a>
https://youtu.be/j9HAMbuEXYk?si=zQW1PlTiQDOUn81T
</a>

after understanding the project topic you must know
that the schedule management system hasn't been implemented
the functionality consists of reseting the statuses everyday
and only show the current day to the user
the concept is pretty easy to code since we just need to yo add 
a block before the return statement inthe get function
we return only the rooms referenced by the current time 
and date
otherwise everything is fine

# openCampProject
Salut OMC , donc on a choisi le premier challenge  "trouver
une solution pour un problème fréquemment commun dans notre université USTHB";
 Je vais vous expliquer d’une façon simple le problème et la solution inventé par nous la team DA BOYZ .

## MEMBERS :
1. Aymen Berbiche
2. Bourabia chems eddine
3. Eladj Salim Zakaria
4. Menhour Adem 

## Problème :

Donc je suis un mathématicien informaticien je vais proposer le
problème en posant des questions :
A ) Dans la période des examens , tu est allé à la bibliothèque de la
fac pour réviser ( bien sûr ) pour le prochain examen mais
malheureusement tu trouve pas de place pour réviser , donc là tu as
perdu une demi-heure pour chercher une place et tu la trouve
mempa , tu finiras par ne pas réviser .
B ) Le prof veux vous faire une séance de révision pour un examen
ou bien une interrogation mais vous ne trouverai pas de salle pour la
faire , malheureusement vous avez perdu une séance de révision .
C ) Un prof de la 2 et 3 ème séance n'est pas venu donc vous n'avez
pas de cour et td est la ca fini avec 3h de creux, si un autre prof vous
propose de ne pas attendre 3h pour faire le td après le creux et il veut
vous regrouper avec le groupe de la 1 ère séance mais il risque de ne
pas trouver une salle double ou triplé et ca fini par attendre 3h .
Donc on conclue que les profs et les étudiants parfois veulent trouver
des salle pour des besoins comme révision et faire monter un td ou
regrouper 2 groupe mais la problème se pose comme suite :
Ni les profs ni les étudiants savent s’il y ‘a des salles vident pour faire
leur besoin et on plus dés fois il perdent de temps pour aller à la
bibliothèque et ça fini souvent par ne pas trouver des places et espace.
Mais dans l’autre cote y ‘a des salles vident mais personne ne déclare
qu’ils sont vides.
Et ça c’est à cause de nombre d’étudiants qui augmente an par an .
Solution :
Donc notre team présente une application web qui a comme base de
donnes les informations des étudiants, et tous les emplois du temps
de l’uni et fais le tri pour avoir le temps vide de chaque salle et elle va
avoir un plan de solution comme suite :
1. Quand un étudiant entre à l’application il va trouver les salles vides
dans les salles 100 200 300 400 pour aller réviser là-bas et ne pas
aller jusqu’au bib, il va gagner de temps et il ne marche pas trop.
2. Un détecteur qui sera en contact avec notre application qui détecte
le nombre d’étudiants qui est dans le bib est quand Y ‘a le nombre
max il sera afficher dans l’application quelle est complet et comme
ça l’étudiant serai au courant, il ne perd pas de temp pour aller
jusqu’au bib pour la trouver complète.
3. Quand un prof veux regrouper 2\3 groupes, ou bien il veut faire une
séance de remplacement ou révision il entre dans l’application et il
trouvera si y a une disponibilité de classe et de quelle genre ( simple
, doublé , triplé ) , on vas gagner de temps et ça fini pas par faire le
tour des 100 200 300 400 par finir sans trouve une salle .
4. Si un prof déclare qu’il ne viendra pas le jour x pour faire la séance
dans la salle officielle dans l’emploi du temp, il entre dans l’application
et annule la prise de salle automatiquement la salle sera affiche en état
libre.
5. Si un étudiant veut faire une révision pour des camarades il peut
chercher si y a une salle dispo et comme ca il peut la faire sans gène
et il aura un tableau pour faire la révision dans des meuliers condition.
6.
Comment ca marche ?
4 | P a g e
Donc si un prof prend une salle qui est de base vide il entre dans
l’application et modifie sons état de « libre » a « non libre », et comme
ca
Elle sera affichée non libre.
Dans le cas où le prof s’absente et il aura une possibilité de ne pas
déclarer que la salle est libre, un accès est autorisé aux délègues pour
Changer l’Etat de la salle.
S’il y a juste une salle libre par exemple la salle 122, et il y a un prof
qui veut faire une séance et des étudiants qui veulent réviser dans
cette salle, bien sur que la priorité est pour le prof.
Pour voir si la bib est chargé ou non cela sera fais automatiquement
En utilisant les détecteurs de mouvement. 
