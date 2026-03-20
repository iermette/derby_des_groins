# DONE - Derby des Groins

Liste des fonctionnalités et idées déjà implémentées dans le projet.

## Gestion des Courses
- **Gestion des courses vides / sous-peuplées** : Mise en place d'une règle configurable (`min_real_participants`) pour remplir automatiquement les courses avec des bots ou les annuler.
- **Remboursement automatique** : Les paris sur les courses annulées sont désormais automatiquement remboursés aux utilisateurs.
- **Scaling des Bots** : Les bots ajoutés aux courses s'adaptent désormais au niveau moyen des participants réels (90% à 110% de la puissance moyenne).

## Poids et Stratégie
- **Système de poids tactique** : Le poids influence désormais dynamiquement les statistiques de Force et d'Agilité.
    - **Surnourri** : Gain de Force (effet bulldozer) mais perte massive d'Agilité.
    - **Sous-poids** : Gain d'Agilité (très vif) mais perte de Force (manque d'impact).
- **Indicateurs visuels** : Affichage explicite des modificateurs de stats sur le tableau de bord et la page du cochon.

## Reproduction et Héritage
- **Système de reproduction** : Deux cochons actifs peuvent lancer une portée pour générer un porcelet.
- **Hérédité** : Les porcelets héritent partiellement des statistiques, de la rareté et de l'origine de leurs parents.
- **Retraite d'honneur & Héritage permanent** : Les cochons légendaires ou victorieux peuvent être mis à la retraite pour booster l'héritage de la porcherie et renforcer leur lignée.
- **Pression de nourrissage** : Le coût des céréales augmente avec le nombre de cochons dans la porcherie (+20% par cochon supplémentaire) pour équilibrer la progression.

## Infrastructure et Admin
- **Configuration Admin** : Ajout de réglages dans le panneau d'administration pour les seuils de participants et les modes de gestion des courses vides.
- **Historique étendu** : Les courses annulées apparaissent désormais dans l'historique pour une meilleure transparence.
