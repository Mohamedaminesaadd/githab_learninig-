# Résumé — Git Rebase

## 1. Définition

`git rebase` permet de rejouer les commits d'une branche au-dessus d'une autre branche afin d'obtenir un historique Git linéaire et propre.

## 2. Quand utiliser Rebase ?

- Actualiser sa branche personnelle avec les dernières modifications de `develop`.
- Éviter les merge commits inutiles.
- Garder un historique linéaire et facile à lire.

## 3. Exemple pratique

Amine travaille sur `feature-a`, mais Mariem a ajouté des commits dans `develop`.

```
# Récupérer les modifications distantes
git fetch origin

# Aller sur sa branche
git switch feature-a

# Rejouer ses commits au-dessus de develop
git rebase origin/develop
```

## 4. Commandes importantes

| Commande                          | Rôle                       |
| --------------------------------- | -------------------------- |
| `git rebase develop`              | Rebaser sur develop        |
| `git rebase --continue`           | Continuer après un conflit |
| `git rebase --abort`              | Annuler le rebase          |
| `git status`                      | Vérifier l'état du rebase  |
| `git log --oneline --graph --all` | Visualiser l'historique    |

## 5. Merge vs Rebase

| Merge                                  | Rebase                                        |
| -------------------------------------- | --------------------------------------------- |
| Fusionne deux historiques              | Rejoue les commits                            |
| Peut créer un merge commit             | Pas de merge commit                           |
| Préserve l'historique existant         | Réécrit l'historique des commits rejoués      |
| Idéal pour intégrer une fonctionnalité | Idéal pour actualiser une branche personnelle |

Règle à retenir

- Rebase : actualiser sa branche personnelle.
- Merge : intégrer une fonctionnalité dans `develop` ou `main`.
- Éviter de rebaser une branche partagée sans coordination.

Phrase pour l'entretien : Git Rebase is a way to integrate changes from one branch into another by replaying commits on top of a new base, creating a linear history.