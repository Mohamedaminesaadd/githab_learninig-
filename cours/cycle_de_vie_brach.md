# Remote Branch Lifecycle Management — Résumé

| Commande                              | Explication                                                                                        |
| ------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `git branch -a`                       | Afficher toutes les branches locales et distantes.                                                 |
| `git branch -r`                       | Afficher les branches distantes.                                                                   |
| `git remote -v`                       | Afficher les dépôts distants configurés.                                                           |
| `git fetch origin`                    | Récupérer les nouvelles références et commits distants sans les intégrer dans la branche actuelle. |
| `git fetch --all`                     | Récupérer les informations de tous les remotes.                                                    |
| `git fetch --prune origin`            | Récupérer les informations et supprimer les références distantes obsolètes.                        |
| `git switch -c feature-a`             | Créer une branche locale et basculer dessus.                                                       |
| `git push -u origin feature-a`        | Publier une branche et configurer son upstream.                                                    |
| `git branch -vv`                      | Afficher les branches et leurs relations de tracking.                                              |
| `git switch --track origin/feature-b` | Créer une branche locale qui suit une branche distante.                                            |
| `git pull`                            | Récupérer et intégrer les changements de la branche distante suivie.                               |
| `git push`                            | Envoyer les commits locaux vers la branche distante suivie.                                        |
| `git push origin --delete feature-a`  | Supprimer une branche distante sur GitHub.                                                         |
| `git branch -d feature-a`             | Supprimer une branche locale déjà intégrée.                                                        |
| `git branch -D feature-a`             | Forcer la suppression d'une branche locale.                                                        |

## Les différences essentielles à retenir

| Concept  | Signification                                              |
| -------- | ---------------------------------------------------------- |
| Fetch    | Télécharger les informations distantes.                    |
| Pull     | Fetch + Merge (par défaut).                                |
| Push     | Envoyer les commits vers le serveur distant.               |
| Tracking | Associer une branche locale à une branche distante.        |
| Prune    | Nettoyer les références des branches distantes supprimées. |
| Clone    | Copier un repository distant en local.                     |

## Cycle de vie d'une branche

```
# 1. Create
git switch -c feature-a

# 2. Publish
git push -u origin feature-a

# 3. Synchronize
git fetch origin

# 4. Update
git pull

# 5. Integrate
git switch develop
git merge feature-a

# 6. Delete remote branch
git push origin --delete feature-a

# 7. Delete local branch
git branch -d feature-a
```

À retenir : une branche distante suit généralement ce cycle :

`Create → Publish → Track → Synchronize → Integrate → Delete`