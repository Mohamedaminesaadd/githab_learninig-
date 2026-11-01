# Clone, Pull & Synchronize a Team Repository

L'objectif est d'apprendre à travailler sur un même projet GitHub avec plusieurs développeurs et à synchroniser les modifications.

## 1. Git Clone

`git clone` permet de récupérer un dépôt distant sur ton ordinateur.

```
git clone https://github.com/username/project.git
```

Git crée automatiquement :

- Un dossier contenant le projet.
- Un dépôt Git local (`.git`).
- Un remote appelé `origin`.
- L'historique des commits.

Exemple :

```
git clone git@github.com:username/project.git
cd project
```

## 2. Git Pull

`git pull` permet de récupérer les dernières modifications du dépôt distant et de les intégrer dans ta branche locale.

```
git pull origin main
```

Exemple :

```
Avant pull :

GitHub (main)           Local (main)
    A                       A
    B                       B

Un collègue ajoute C :

GitHub (main)           Local (main)
    A                       A
    B                       B
    C

Après git pull :

GitHub (main)           Local (main)
    A                       A
    B                       B
    C                       C
```

## 3. Git Fetch vs Git Pull

| Commande    | Fonction                                                 |
| ----------- | -------------------------------------------------------- |
| `git fetch` | Télécharge les modifications distantes sans les intégrer |
| `git pull`  | Télécharge et intègre les modifications distantes        |

Exemple :

```
git fetch origin
git log HEAD..origin/main --oneline
```

Pour intégrer ensuite les modifications :

```
git merge origin/main
```

## 4. Synchroniser son travail avec l'équipe

Imaginons deux développeurs :

- Developer A travaille sur le projet.
- Developer B travaille sur le même projet.
- Tous les deux utilisent le dépôt GitHub.

Workflow recommandé :

```
# 1. Récupérer les dernières modifications
git pull origin main

# 2. Créer sa propre branche
git switch -c feature/login

# 3. Modifier les fichiers

# 4. Ajouter les modifications
git add .

# 5. Créer un commit
git commit -m "Add login feature"

# 6. Envoyer sa branche sur GitHub
git push -u origin feature/login
```

Ensuite, le développeur crée une Pull Request (PR) sur GitHub pour proposer l'intégration de sa branche dans `main`.

## 5. Pull Request (PR)

Une Pull Request permet de proposer des modifications avant de les intégrer dans la branche principale.

[GitHub Issues and Pull Requests — GitHub without the command line](https://images.openai.com/static-rsc-4/062pphxhKrwUY80PRttWw_t5HSrPgc7zOMuSDTVMwbcTC2DYma1PRmFxSXrrMlhxNGMmNzZts9oAjhkYEuK5n-UTgpcimpZFqNVncl5-k-RNUF8FmvXhjLxkiZpPRfhn0YzLfH1GlcM8q6q-Ex54qC48DSimzvQ-hFqUAaRC0sY?purpose=inline)

[miketrizna.github.io](https://miketrizna.github.io/github-without-command-line/contributing.html?utm_source=chatgpt.com)

Processus :

1. Developer A crée une branche `feature/login`.
2. Il développe la fonctionnalité.
3. Il pousse sa branche sur GitHub.
4. Il crée une Pull Request.
5. L'équipe examine le code (Code Review).
6. La Pull Request est acceptée et fusionnée dans `main`.

Attention : `git pull` et GitHub Pull Request sont deux choses différentes.

- `git pull` : commande Git pour synchroniser ton dépôt local.
- Pull Request : mécanisme GitHub pour proposer et examiner des modifications.

## 6. Gérer les conflits pendant la synchronisation

Supposons que deux développeurs modifient la même ligne.

Après :

```
git pull origin main
```

Git peut afficher :

```
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

Résolution :

```
# 1. Identifier les fichiers en conflit
git status

# 2. Ouvrir et corriger manuellement les fichiers

# 3. Ajouter les fichiers corrigés
git add .

# 4. Terminer le merge
git commit
```

Si tu souhaites annuler le merge :

```
git merge --abort
```

## 7. Résumé des commandes

| Commande            | Rôle                                       |
| ------------------- | ------------------------------------------ |
| `git clone URL`     | Cloner un dépôt                            |
| `git pull`          | Synchroniser avec le remote                |
| `git fetch`         | Récupérer sans intégrer                    |
| `git merge`         | Fusionner deux branches                    |
| `git push`          | Envoyer les commits                        |
| `git branch -a`     | Afficher les branches locales et distantes |
| `git switch branch` | Changer de branche                         |
| `git remote -v`     | Afficher les dépôts distants               |

## 8. Workflow complet d'une équipe

[Create a simple GitHub Actions Workflow - DEV Community](https://images.openai.com/static-rsc-4/Ag65zGNKlCb_dbMhizn5JDd0T4ZFM1bPihMtveHp2azYe2o7gm5vlBjyg22Aou2HF5K0UXePN-Kf2aFgc_LXBRhVcPLK9N6I35MldPBxg44OHeW24H4wybeSBpv6tmqwbLuO5MPnJ7bHSl5LEbcqYYWfRJ5yw3atnF6JFgs-ySg?purpose=inline)

[dev.to](https://dev.to/ambujsahu81/create-a-simple-github-actions-workflow-347n?utm_source=chatgpt.com)

```
# Première utilisation
git clone URL
cd project

# À chaque nouvelle tâche
git pull origin main
git switch -c feature/my-feature

# Développement
git add .
git commit -m "Implement my feature"

# Envoyer le travail
git push -u origin feature/my-feature

# Sur GitHub : créer une Pull Request
# Après validation et merge :

git switch main
git pull origin main
```

À retenir pour l'examen :

- `clone` = télécharger un dépôt pour la première fois.
- `fetch` = récupérer les changements distants sans les intégrer.
- `pull` = récupérer et intégrer les changements.
- `push` = envoyer ses commits.
- `Pull Request` = proposer une fusion et faire une revue de code.