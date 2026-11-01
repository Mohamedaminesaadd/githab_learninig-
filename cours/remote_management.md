Pour faire un `git push` vers GitHub, tu dois t'authentifier. Il existe 2 méthodes principales : HTTPS avec un Personal Access Token (PAT) ou SSH avec une clé SSH.

## 1. Méthode HTTPS : Personal Access Token (PAT)

C'est une méthode simple pour commencer.

Étape 1 — Créer un token GitHub

1. Ouvre [GitHub Personal Access Tokens](https://github.com/settings/tokens?utm_source=chatgpt.com).
2. Va dans Personal access tokens → Fine-grained tokens.
3. Clique sur Generate new token.
4. Configure :
   - Repository access : Only select repositories.
   - Sélectionne ton dépôt.
   - Repository permissions : Contents → Read and write.
5. Génère et copie ton token.



Important

&#x20;Le token est affiché une seule fois. Ne le partage jamais et ne le mets jamais dans ton code.



Étape 2 — Faire un push

```
git push -u origin main
```

Git te demande :

```
Username: your_github_username
Password: YOUR_PERSONAL_ACCESS_TOKEN
```

Attention : dans le champ Password, tu colles le token, pas ton mot de passe GitHub.

## 2. Méthode SSH : utiliser une clé SSH

Cette méthode est pratique parce que tu n'as pas besoin de saisir ton token à chaque push.

Étape 1 — Générer une clé SSH

Sur Ubuntu :

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Appuie sur Entrée pour accepter le chemin proposé et configure éventuellement une passphrase.

Étape 2 — Démarrer ssh-agent

```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Étape 3 — Copier la clé publique

```
cat ~/.ssh/id_ed25519.pub
```

Copie tout le contenu affiché.

Étape 4 — Ajouter la clé à GitHub

1. Ouvre [GitHub → New SSH key](https://github.com/settings/ssh/new?utm_source=chatgpt.com).
2. Donne un titre à ta clé.
3. Colle la clé publique.
4. Clique sur Add SSH key.

Étape 5 — Tester l'authentification

```
ssh -T git@github.com
```

Résultat attendu :

```
Hi username! You've successfully authenticated,
but GitHub does not provide shell access.
```

Étape 6 — Utiliser SSH pour ton dépôt

Si ton remote utilise HTTPS, remplace-le par l'URL SSH :

```
git remote set-url origin git@github.com:username/git-lab.git
```

Puis :

```
git push -u origin main
```

## 3. Comparaison

| Critère                        | HTTPS + PAT                           | SSH                                |
| ------------------------------ | ------------------------------------- | ---------------------------------- |
| Authentification               | Token                                 | Clé SSH                            |
| Configuration                  | Simple                                | Quelques étapes                    |
| Saisir un secret à chaque push | Pas nécessaire avec credential helper | Pas nécessaire après configuration |
| Sécurité                       | Bonne si token protégé                | Bonne si clé privée protégée       |

Ma recommandation : utilise SSH sur Ubuntu pour tes projets GitHub.

À retenir pour ton cours :

- HTTPS → Username + Personal Access Token.
- SSH → Clé privée sur ton ordinateur + clé publique sur GitHub.
- La clé privée ne doit jamais être envoyée à GitHub.