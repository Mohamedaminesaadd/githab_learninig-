Upstream est la branche distante associée à une branche locale. Elle indique à Git avec quelle branche distante synchroniser automatiquement les modifications avec `git pull` et `git push`.

### 1. Exemple

Tu as une branche locale `main` et une branche distante `origin/main`.

```
Local Repository          GitHub

main       ──────────────> origin/main
       Upstream relationship
```

Cela signifie que `main` suit `origin/main`.

### 2. Configurer Upstream

Avec `git push -u` :

```
git push -u origin main
```

L'option `-u` signifie `--set-upstream`.

Elle configure `origin/main` comme upstream de ta branche locale `main`.

### 3. Vérifier Upstream

```
git branch -vv
```

Exemple de résultat :

```
* main       abc123 [origin/main] Initial commit
  feature    def456 [origin/feature] Add login
```

`[origin/main]` indique que la branche locale `main` suit `origin/main`.

### 4. Pourquoi utiliser Upstream ?

Une fois configuré, tu peux utiliser directement :

```
git pull
git push
```

Sans préciser `origin main` à chaque fois.

### 5. Résumé

| Terme         | Signification                                  |
| ------------- | ---------------------------------------------- |
| `main`        | Branche locale                                 |
| `origin`      | Nom du dépôt distant                           |
| `origin/main` | Référence locale de la branche distante        |
| `upstream`    | Branche distante suivie par une branche locale |
| `git push -u` | Envoyer et configurer le suivi                 |

À retenir : Upstream = la branche distante que ta branche locale suit pour les opérations `pull` et `push`.