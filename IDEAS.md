# IDEAS

## Priorites produit proposees

### 1. Logiques de victoire sur le long terme

- Mettre en place des **saisons** courtes (mensuelles par defaut) avec:
  - remise a zero partielle des classements,
  - conservation des trophees, du Hall of Fame et des metriques historiques,
  - divisions / ligues pour separer nouveaux eleveurs et veterans.
- Renforcer l'**anti-snowball** pour eviter qu'un joueur dominant ecrase durablement la concurrence:
  - fatigue apres sorties consecutives,
  - rendements decroissants a l'entrainement,
  - buffs de comeback pour les cochons frais ou les joueurs moins actifs.
- Ajouter un systeme de **reproduction, lignee et heritage**:
  - retraite honorable des cochons legendaires,
  - bonus permanents de porcherie ou de lignee,
  - genealogie exploitable comme objectif meta.
- Formaliser un **Hall of Fame** saisonnier:
  - vainqueur `Saint Grouin`,
  - meilleurs eleveurs,
  - cochons les plus rentables,
  - survivants emblematiques du `Challenge de la Mort`.

## Rythme des courses

- Eviter `1 course par heure` comme regle par defaut. Garder la main cote admin sur le rythme, avec une config simple `mode calme / normal / evenement`.
- Prevoir une reponse claire si une course n'a qu'un seul vrai participant:
  - soit completer avec des PNJ,
  - soit annuler ou reporter la course si le plateau est trop vide.
- Ajouter des evenements ponctuels `grosse course du soir` ou `grand prix du vendredi` pour donner des rendez-vous plus memorables.

## Convention collective de la porcherie

- Ajouter une logique de `quota hebdomadaire` type `35 heures de l'auge`: un cochon ne peut courir que `2 a 3 courses maximum par semaine`.
- Forcer l'eleveur a choisir a l'avance ses sorties importantes selon les adversaires, le jour, les bonus de course ou l'etat du cochon.
- Rendre la programmation des courses plus strategique que le simple spam de participations.
- Ajouter une lecture claire de la semaine a venir dans l'interface: jours de course, quota restant, prochaine sortie planifiee.

## Calendrier des courses

- Ajouter un vrai menu `Liste des courses` ou `Calendrier des courses`.
- Afficher les courses a venir sur la semaine et idealement sur le mois:
  - date,
  - type de course,
  - regle speciale du jour,
  - slots disponibles,
  - cochons deja inscrits.
- Permettre d'inscrire son cochon a l'avance sur une ou plusieurs courses selon son quota hebdomadaire.
- Ajouter une vue `planification`:
  - quota restant pour la semaine,
  - jours deja reserves,
  - alertes de fatigue si deux courses s'enchainent,
  - buff potentiel si le cochon se repose avant une grande course.
- Cette page peut devenir le coeur du jeu asynchrone: on vient planifier sa semaine, pas juste cliquer sur une course ouverte.

## Statistiques, conditions de course et equilibrage

- Donner une vraie utilite aux statistiques secondaires via des **themes de course** et la **meteo**:
  - `Pataugeoire du Lundi` sur piste boueuse pour favoriser Force et Endurance,
  - piste seche pour favoriser Vitesse,
  - formats speciaux pour mettre en valeur Intelligence, Agilite ou Moral.
- Rendre le **poids de forme** plus lisible et plus punitif / strategique:
  - un cochon sur-nourri au mais perd en Agilite,
  - il gagne en Force et capacite de contact,
  - la presentation visuelle doit rendre l'etat du cochon immediatement compréhensible.
- Revoir l'**Ecole porcine** pour eviter le maxage trop rapide des stats:
  - limiter les gains bruts,
  - introduire des specialisations (`sprinteur`, `roublard`, `marathonien`, etc.),
  - garder le cout moral comme vrai arbitrage plutot qu'une formalite.

## Fatigue, porc-out et RTT

- Si un cochon court deux jours de suite, lui appliquer un malus de fatigue du type `Sueur de Porc` avec baisse temporaire de vitesse ou de condition.
- Si l'eleveur force une troisieme sortie consecutive, le cochon attrape une `Fievre Porcine` et passe le reste de la semaine en arret maladie.
- A l'inverse, un cochon qui se repose `4 a 5 jours` gagne un gros buff ponctuel du type `Frais comme un Porcelet` pour sa prochaine course.
- Cette boucle doit aider les joueurs occasionnels:
  - les joueurs tres presents ne peuvent pas abuser du volume,
  - les joueurs absents quelques jours peuvent revenir avec un vrai coup a jouer.

## Bauge, absences et survie passive

- Ajouter des `Conges Porcins`: si un joueur ne se connecte pas pendant `36 a 48 heures`, son elevage passe en mode hibernation et les jauges critiques sont gelees.
- Faire baisser la faim de base tres lentement pour que la survie du cochon ne ressemble pas a une corvee quotidienne.
- Garder une logique de bonus actif:
  - la nourriture standard sert a maintenir,
  - une `Truffe de Luxe` ou autre friandise avant course donne un buff de motivation ou de performance.
- Ajouter un mode `Stagiaire Ramasse-Purin` ou `delegation vacances`:
  - le joueur active une option avant de partir,
  - le systeme maintient le minimum vital de l'enclos,
  - le joueur absent ne perd pas son cochon juste parce qu'il etait en deplacement.

## Anti-snowball et seasons

- Eviter que les memes eleveurs soient toujours en tete des stats globales.
- Ajouter des saisons avec remise a zero partielle des classements, tout en gardant les trophees et l'historique.
- Creer des ligues ou divisions par niveau d'elevage pour aider les nouveaux a exister.
- Ajouter des mecanismes de comeback: fatigue, blessures, rendements decroissants a l'entrainement, bonus de rattrapage.

## Pari mutuel porcin

- Remplacer une partie du spam de paris par des `Tickets Bacon` limites, par exemple `3 tickets par semaine` redonnes le lundi.
- Faire du pari un vrai choix strategique: impossible de miser sur tout ce qui bouge, il faut sentir la bonne course.
- Ajouter une logique `Copains comme Cochons`:
  - un cochon programme en avance mais dont le proprietaire est absent peut devenir plus rentable a jouer,
  - cela encourage les discussions de bureau et les pronostics collectifs.
- Associer ces tickets limites a la semaine de course pour creer des pics d'attention plutot qu'un bruit constant.

## Blessures et veterinaire

- Un cochon pourrait se blesser pendant une course.
- En cas de blessure grave, passage chez le veterinaire avec un mini-jeu type `Docteur Maboul` ou puzzle d'os.
- Le mini-jeu aurait un temps limite:
  - reussite: le cochon survit, avec eventuellement un malus temporaire,
  - echec: grosse sequelle ou deces sur la table d'operation dans les cas critiques.
- Les blessures legeres peuvent aussi enrichir la vie du cochon sans tuer la run: repos, medicaments, stats temporairement baissees.

## Reproduction et lignee

- Autoriser la reproduction entre cochons pour creer des porcelets.
- Heriter partiellement des stats, de la rarete, de l'origine ou d'un trait special.
- Permettre de tenter des combinaisons improbables pour faire apparaitre des cochons legendaires, meme a partir de `grouillots`.
- Ajouter un arbre genealogique ou historique de lignee pour raconter les familles de champions.

## Semaine de la porcherie

- Donner un theme et des regles specifique a chaque jour pour que le calendrier hebdomadaire devienne une vraie mecanique.
- Lundi: `Pataugeoire du Lundi Matin`
  - piste boueuse, forte variance, jour parfait pour les outsiders.
- Mardi et jeudi: `Trot du Jambon`
  - courses classiques, stables, ideales pour jouer la securite.
- Mercredi: `Marathon de la Conf' Call`
  - grosse mise en avant de l'endurance et du cardio.
- Vendredi: `Grande Finale du Cochon Roti`
  - derby principal de la semaine, recompenses et gains potentiellement doubles.
- Le but est de pousser l'eleveur a construire un `agenda`, pas seulement un bon cochon.

## Meta-jeu et communaute

- Creer un systeme d'**ecuries / clans** pour jouer en groupe et mutualiser une partie des ressources ou des objectifs.
- Ajouter des **alertes et webhooks** vers Slack / Teams pour:
  - resultats de courses,
  - ouverture et cloture des encheres,
  - urgences veterinaire,
  - rappels de quota ou de course planifiee.
- Ajouter un Hall of Fame des saisons, des champions et des eleveurs les plus marquants.
- Faire du trophee physique un vrai prolongement du jeu:
  - nom possible: `Le Saint Grouin`,
  - version bureau ou impression 3D,
  - transmission de gagnant en gagnant,
  - ceremonie pendant les reunions sur site.
- Variante delire assume: le trophee pourrait aussi servir de chope de victoire.

## Menus et interfaces manquants

- Ajouter un **menu Calendrier / Planification** interactif comme coeur du jeu asynchrone:
  - vue hebdomadaire / mensuelle,
  - quota `35h de l'auge`,
  - themes de course,
  - inscription en un clic.
- Ajouter un **menu Genealogie / Arbre genealogique**:
  - anciens cochons du joueur,
  - morts, retraites, legendes,
  - statistiques globales de l'elevage.
- Renforcer le **dashboard d'accueil** avec des pronostics de communaute et des signaux pre-course (`70% des joueurs ont parie sur Porcinator`).
- Ajouter une page de **statistiques globales / PMU porcin**:
  - cotes historiques,
  - cochons les plus rentables,
  - plus gros gains de la semaine,
  - tendances utiles pour les Tickets Bacon.

## Trophees et ceremonies

- Ajouter des trophees rares et marquants plutot qu'une pluie de petites recompenses permanentes.
- Exemples de rendez-vous:
  - `Trophee de fin de mois`,
  - `Trophee trimestriel`,
  - `Grande distinction annuelle`,
  - `Trophee de reunion sur site`.
- Lors des reunions physiques, utiliser le jeu pour `delivrer officiellement` un trophee au gagnant:
  - remise ceremonielle,
  - photo du vainqueur,
  - inscription dans un Hall of Fame,
  - passation du trophee au cycle suivant.
- Penser le trophee comme un objet meta:
  - recompense IG,
  - evenement social IRL,
  - folklore d'equipe.
- Possibilite d'avoir des trophees differents selon le rythme:
  - meilleur eleveur du mois,
  - meilleur retour inattendu,
  - champion du derby du vendredi,
  - cochon legendaire du trimestre.

## Ton du projet

- Assumer le ton absurde et ceremoniel du projet: trophes, titres honorifiques, passation, folklore maison.
- Transformer les meilleures blagues internes en features cosmetiques plutot qu'en mecaniques critiques.

## Direction forte a garder

- Aller vers un `jeu de bureau asynchrone`:
  - peu de connexions obligatoires,
  - peu de punition pour les absents,
  - beaucoup de valeur dans la planification de la semaine.
- Faire en sorte qu'un joueur puisse se connecter `5 minutes le lundi`, programmer son cochon, poser ses tickets, puis revenir en fin de semaine pour un gros moment social.
