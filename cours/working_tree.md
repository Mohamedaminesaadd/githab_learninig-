## 1. Working Tree

Working Tree = l'espace de travail où tu crées, modifies et supprimes les fichiers de ton projet avant de les enregistrer dans Git.

## 2. Commands to restore changes

| Command                               | Description                                                      |
| ------------------------------------- | ---------------------------------------------------------------- |
| `git restore file.java`               | Annuler les modifications unstaged                               |
| `git restore .`                       | Annuler toutes les modifications unstaged des fichiers suivis    |
| `git restore --staged file.java`      | Retirer un fichier du Staging Area sans perdre ses modifications |
| `git restore --source=HEAD file.java` | Restaurer un fichier depuis le dernier commit                    |

Example:

```
# Restore one file
git restore code/BankAccount.java

# Restore all modified tracked files
git restore .

# Unstage a file
git restore --staged code/BankAccount.java

# Check status
git status
```



Attention

`git restore` peut supprimer définitivement les modifications locales non sauvegardées.



Remember:

- `git restore` → Working Tree.
- `git restore --staged` → Staging Area.