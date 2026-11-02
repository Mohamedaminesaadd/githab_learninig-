# Lab 17 — Interactive Rebase & Commit Surgery

## 1. Comprendre le concept

Interactive Rebase est une fonctionnalité de Git qui permet de modifier l'historique de plusieurs commits avant de les partager ou de les intégrer dans une autre branche.

Avec un rebase classique, on rejoue les commits sur une nouvelle base.

Avec un Interactive Rebase, on peut également :

- Modifier le message d'un commit.
- Fusionner plusieurs commits en un seul.
- Supprimer un commit.
- Réorganiser les commits.
- Modifier le contenu d'un ancien commit.

C'est ce qu'on appelle parfois Commit Surgery (chirurgie des commits).

## 2. La commande principale

```
git rebase -i HEAD~3
```

Explication :

- `rebase` : lancer un rebase.
- `-i` : Interactive, mode interactif.
- `HEAD~3` : examiner les trois derniers commits.

Git ouvre un éditeur avec une liste de commits.

## 3. Les commandes interactives

| Commande     | Signification | Action                                                      |
| ------------ | ------------- | ----------------------------------------------------------- |
| `pick` (p)   | Pick          | Garder le commit                                            |
| `reword` (r) | Reword        | Modifier son message                                        |
| `edit` (e)   | Edit          | Modifier le contenu du commit                               |
| `squash` (s) | Squash        | Fusionner avec le commit précédent et combiner les messages |
| `fixup` (f)  | Fixup         | Fusionner avec le commit précédent sans garder son message  |
| `drop` (d)   | Drop          | Supprimer le commit                                         |

## 4. Exemple pratique

Imaginons que tu as réalisé ces trois commits dans `feature-a` :

```
git log --oneline
```

Résultat :

```
a123456 Add account service
b234567 Fix account service
c345678 Update account service
```

Tu veux fusionner les trois commits en un seul.

Étape 1 : lancer Interactive Rebase

```
git rebase -i HEAD~3
```

Étape 2 : modifier la liste

Git ouvre un fichier semblable à celui-ci :

```
pick c345678 Update account service
squash b234567 Fix account service
squash a123456 Add account service
```

Attention : Git affiche normalement les commits du plus ancien au plus récent. Vérifie l'ordre dans ton éditeur.

Étape 3 : enregistrer et fermer

Git te proposera ensuite de choisir le message du commit final.

Par exemple :

```
feat: implement account service
```

Étape 4 : vérifier le résultat

```
git log --oneline
```

Tu obtiendras un seul commit regroupant les trois changements.

## 5. Autres exemples

Modifier le message d'un commit :

```
git rebase -i HEAD~3
```

Puis remplacer `pick` par `reword`.

Supprimer un commit :

```
pick abc123 Add account model
drop def456 Temporary debug code
pick ghi789 Add account service
```

Modifier le contenu d'un commit :

```
pick abc123 Add account model
edit def456 Add account service
pick ghi789 Add account tests
```

Git s'arrêtera sur le commit choisi. Après tes modifications :

```
git add .
git commit --amend
git rebase --continue
```

## 6. Gérer les problèmes

| Commande                | Rôle                       |
| ----------------------- | -------------------------- |
| `git status`            | Vérifier l'état            |
| `git rebase --continue` | Continuer                  |
| `git rebase --abort`    | Annuler toute l'opération  |
| `git rebase --skip`     | Ignorer le commit en cours |

## 7. Attention : règle professionnelle

Interactive Rebase réécrit l'historique : les commits modifiés obtiennent de nouveaux identifiants.

- Utilise-le avant de partager tes commits, pour nettoyer ton historique.
- Évite de l'utiliser sur une branche partagée avec d'autres développeurs sans coordination.
- Si tu as déjà publié la branche, un `git push --force-with-lease` peut être nécessaire après le rebase. Ne l'utilise pas sans vérifier les changements distants.

## 8. Questions pour vérifier ta compréhension

1. Quelle est la différence entre `git rebase` et `git rebase -i` ?
2. Quelle est la différence entre `squash` et `fixup` ?
3. Quelle commande permet de modifier le message d'un ancien commit ?
4. Comment supprimer un commit de l'historique ?
5. Pourquoi Interactive Rebase est-il dangereux sur une branche partagée ?

À retenir :

```
git rebase -i HEAD~N
```

C'est la commande essentielle pour nettoyer, réorganiser et modifier tes derniers commits Git.