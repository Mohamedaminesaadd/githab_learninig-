# Professional Branching Strategies

Les Branching Strategies sont des méthodes utilisées par les équipes de développement pour organiser le travail avec Git, éviter les conflits et contrôler l'intégration du code.

Il existe plusieurs stratégies professionnelles.

## 1. Git Flow

Git Flow est une stratégie adaptée aux projets qui ont des versions et des cycles de release structurés.

[\[코인 자동투자 봇 제작기 3\] Git branch 흐름 설계 및 코드 작성](https://images.openai.com/static-rsc-4/o5EnXMguEY3GBOZ1r4VSKeatSWF66tfhHWmy4A5zO1DcgCumfyjQvWBCjwwhyJUzfOcRtXgb5m5E0a_-i2cWutVPM4G-F2Ob3wTte0jFOdhbv13_i0DxM_7np6nJ5lfDXpzRy-f5-4KBmh8fEsro0sJ7qoC7Wg5m3Br3y8OEwS8?purpose=inline)

[woghd-dev.tistory.com](https://woghd-dev.tistory.com/entry/%EC%BD%94%EC%9D%B8-%EC%9E%90%EB%8F%99%ED%88%AC%EC%9E%90-%EB%B4%87-%EC%A0%9C%EC%9E%91%EA%B8%B0-3-Git-branch-%ED%9D%90%EB%A6%84-%EC%84%A4%EA%B3%84-%EB%B0%8F-%EC%BD%94%EB%93%9C-%EC%9E%91%EC%84%B1?utm_source=chatgpt.com)

Elle utilise principalement 5 types de branches :

| Branche     | Rôle                                     |
| ----------- | ---------------------------------------- |
| `main`      | Code stable en production                |
| `develop`   | Branche principale de développement      |
| `feature/*` | Développer une nouvelle fonctionnalité   |
| `release/*` | Préparer une nouvelle version            |
| `hotfix/*`  | Corriger rapidement un bug en production |

Exemple de workflow :

```
# Créer la branche develop
git switch -c develop

# Développer une fonctionnalité
git switch -c feature/login

# Après développement
git add .
git commit -m "Add login feature"

# Revenir sur develop et intégrer
git switch develop
git merge feature/login

# Préparer une release
git switch -c release/1.0

# Après validation, intégrer dans main
git switch main
git merge release/1.0
```

Quand utiliser Git Flow ?

- Projets de grande taille.
- Plusieurs versions du logiciel.
- Releases planifiées.
- Applications nécessitant une maintenance structurée.

## 2. GitHub Flow

GitHub Flow est une stratégie simple basée sur une seule branche principale et des branches de fonctionnalités.

[GitHub - regnaer/Release-Based-Workflow](https://images.openai.com/static-rsc-4/0v7dXbyDiHTnNnzfVbjEjpJEu19L4SLkhdhG9Sp0Xeu1zrJDEyy7L_-BIzoxQPnoGs8a_ymdFgGiIsOgcNAJCauQahbQ29Jzu0nU8ZWqYKO2HfET96n4G1c4ha-5gsSahiUUoSPBm8NTI_c9K-mUWPBStAsxZEB0GsJyaV-6NFg?purpose=inline)

[github.com](https://github.com/regnaer/Release-Based-Workflow?utm_source=chatgpt.com)

Branches utilisées :

- `main` : branche principale, toujours prête à être déployée.
- `feature/*` : branches temporaires pour développer des fonctionnalités.

Workflow :

```
# 1. Récupérer les dernières modifications
git switch main
git pull origin main

# 2. Créer une branche
git switch -c feature/login

# 3. Développer
git add .
git commit -m "Add login"

# 4. Envoyer la branche
git push -u origin feature/login

# 5. Créer une Pull Request sur GitHub
# 6. Code Review
# 7. Merge dans main
```

Quand utiliser GitHub Flow ?

- Projets Web.
- Équipes Agile.
- Déploiement continu (Continuous Deployment).
- Projets qui évoluent fréquemment.

## 3. GitLab Flow

GitLab Flow combine le travail avec des branches de fonctionnalités et la gestion des environnements ou des versions.

[Mastering Git Branching Strategies: Finding the Right Fit for Your Team - DEV Community](https://images.openai.com/static-rsc-4/BsUvp0g8jsPULYBJF9qrvjjh_WAzO0nlkEe8eHomiFPpUaBRduBn60kIDlovoHT0AUSTbRu-DNiS44vqE_8IVX5PneKcikQfCIqwg-yKTc3r8tYPq9HBqNvX8CExOdSGiflbPFePe0j_GuoXbUBiWlG49exSyhc8tsqVDKXglJs?purpose=inline)

[dev.to](https://dev.to/trinitezinsou/mastering-git-branching-strategies-finding-the-right-fit-for-your-team-4p2n?utm_source=chatgpt.com)

Exemple de branches :

```
main
  |
  |---- feature/login
  |
  |---- feature/payment
  |
  v
staging
  |
  v
production
```

Les branches `staging` et `production` peuvent représenter des environnements de déploiement.

Quand utiliser GitLab Flow ?

- Projets avec plusieurs environnements.
- Applications avec un processus de validation.
- Déploiement contrôlé.

## 4. Trunk-Based Development

Dans cette stratégie, tous les développeurs intègrent régulièrement leurs modifications dans une branche principale appelée `main` ou `trunk`.

[How Spotify Ships to 675 Million Users Every Week Without Breaking Things](https://images.openai.com/static-rsc-4/ufxBXFitp15y8Cdk6mCzb9edcdqRJcSVITMNKNZuXKMdEhKpeFBorE13tHhldWwAD1vzhnVx-1kmZqyQzHdtT3JttHUTH_-A6jQn9J_1F6ScqHHEcMJroZwkkEqfRww_rFA25EB64NNkBiWl5p-JJJKZGm2YD5gL9hRo-gUa_Uc?purpose=inline)

[blog.bytebytego.com](https://blog.bytebytego.com/p/how-spotify-ships-to-675-million?utm_source=chatgpt.com)

Principes :

- Une branche principale.
- Branches secondaires très courtes.
- Intégration fréquente.
- Tests automatisés.
- Éviter les branches longues.

Exemple :

```
git switch main
git pull origin main

git switch -c feature/search

# Développement rapide
git add .
git commit -m "Add search"

git push -u origin feature/search
```

Après validation, la branche est rapidement fusionnée dans `main`.

Quand utiliser cette stratégie ?

- Continuous Integration (CI).
- Continuous Deployment (CD).
- Équipes expérimentées.
- Projets avec tests automatisés.

## 5. Comparaison des stratégies

| Critère          | Git Flow         | GitHub Flow | GitLab Flow              | Trunk-Based    |
| ---------------- | ---------------- | ----------- | ------------------------ | -------------- |
| Complexité       | Élevée           | Faible      | Moyenne                  | Faible         |
| Branches longues | Oui              | Non         | Selon le workflow        | Non            |
| Pull Request     | Possible         | Centrale    | Possible                 | Selon l'équipe |
| Releases         | Structurées      | Continues   | Structurées              | Continues      |
| Utilisation      | Grandes releases | Web/Agile   | Environnements multiples | CI/CD          |

## 6. Quelle stratégie choisir ?

- Git Flow : si ton application possède des versions et des releases planifiées.
- GitHub Flow : si tu travailles avec GitHub et des Pull Requests.
- GitLab Flow : si tu gères plusieurs environnements de déploiement.
- Trunk-Based Development : si tu veux intégrer rapidement et continuellement le code.

## 7. Résumé pour l'examen

| Terme        | Signification                          |
| ------------ | -------------------------------------- |
| `main`       | Branche principale                     |
| `develop`    | Branche de développement dans Git Flow |
| `feature`    | Nouvelle fonctionnalité                |
| `release`    | Préparation d'une version              |
| `hotfix`     | Correction urgente en production       |
| Pull Request | Proposition de fusion                  |
| Code Review  | Vérification du code                   |
| CI/CD        | Intégration et déploiement continus    |

À retenir : Git Flow organise le développement autour de plusieurs branches spécialisées, GitHub Flow privilégie les Pull Requests, et Trunk-Based Development privilégie l'intégration fréquente dans une branche principale.