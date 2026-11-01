## `.gitignore` — Résumé

`.gitignore` est un fichier qui indique à Git quels fichiers et dossiers il doit ignorer (ne pas suivre).

Exemples : fichiers compilés, dossiers temporaires, logs, configurations IDE et fichiers contenant des secrets.

### 1. Exemple de `.gitignore`

```
# Java
*.class

# Maven
target/

# IntelliJ
.idea/

# Logs
*.log

# Environment variables
.env
```

### 2. Les commandes importantes

```
# Create .gitignore
touch .gitignore

# Edit .gitignore
nano .gitignore

# Check repository status
git status

# Show ignored files
git status --ignored

# Check why a file is ignored
git check-ignore -v target/file.class

# Remove an already tracked file but keep it locally
git rm --cached file.txt

# Remove all tracked files from index (keep local files)
git rm -r --cached .

# Add files again, respecting .gitignore
git add .

# Commit changes
git commit -m "Add gitignore"
```

### 3. Important points for the exam

| Concept               | Meaning                                |
| --------------------- | -------------------------------------- |
| `.gitignore`          | Specifies files Git should ignore      |
| `*.class`             | Ignore all `.class` files              |
| `target/`             | Ignore target directories              |
| `!file.txt`           | Exclude a file from ignore rules       |
| `git check-ignore -v` | Check why a file is ignored            |
| `git rm --cached`     | Stop tracking without deleting locally |

À retenir

- `.gitignore` ignores untracked files matching its rules.
- It does not automatically stop tracking files already committed.
- Use `git rm --cached` to stop tracking an existing file.
- Use `git commit` to record the cleanup.