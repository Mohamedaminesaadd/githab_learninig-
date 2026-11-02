When a new contributor joins a GitHub project, the best strategy is to use a lightweight version of Fork → Branch → Commit → Pull Request → Review → Merge.

For your project, where Amine owns the repository and Mariem is a new contributor, I recommend the following workflow.

# 1. Choose the collaboration strategy

There are two common approaches:

| Strategy            | Description                                                 | Best for                                       |
| ------------------- | ----------------------------------------------------------- | ---------------------------------------------- |
| Shared repository   | Contributors have write access and create branches directly | Small trusted teams                            |
| Fork-based workflow | Contributors fork the repository and submit Pull Requests   | Open-source projects and external contributors |



Recommended for Amine + Mariem

&#x20;Shared repository with feature branches.



Mariem already has collaborator access, so she doesn't need to fork the repository.

# 2. Recommended Git workflow

## Contributor workflow

main

Stable branch — protected

Amine

`feature/backend-api`

Mariem

`feature/java-examples`

Pull Requests

Code review and approval

Merge into main

Stable version updated

# 3. Step-by-step workflow for Mariem

### Step 1 — Clone the repository

```
git clone git@github-mariem:Mohamedaminesaadd/githab_learninig-.git
cd githab_learninig-
```

### Step 2 — Synchronize with main

Before starting:

```
git switch main
git pull origin main
```

### Step 3 — Create a feature branch

For example, Mariem wants to add Java examples:

```
git switch -c feature/java-examples
```

Branch naming conventions:

```
feature/add-login
feature/java-examples
fix/login-error
docs/update-readme
test/add-unit-tests
```

### Step 4 — Work and commit

```
git add .
git commit -m "feat: add Java examples"
```

Use meaningful commit messages:

| Prefix      | Purpose            |
| ----------- | ------------------ |
| `feat:`     | New feature        |
| `fix:`      | Bug fix            |
| `docs:`     | Documentation      |
| `test:`     | Tests              |
| `refactor:` | Code restructuring |
| `chore:`    | Maintenance        |

### Step 5 — Push the branch

```
git push -u origin feature/java-examples
```

### Step 6 — Create a Pull Request

On GitHub:

1. Open the repository.
2. Select Pull requests.
3. Click New pull request.
4. Base branch: `main`.
5. Compare branch: `feature/java-examples`.
6. Create Pull Request.
7. Describe the changes.

### Step 7 — Code review

Amine reviews Mariem's contribution:

- Does the code work?
- Is it readable?
- Are there bugs?
- Are tests included?
- Does it follow the project conventions?

If changes are needed, Mariem updates her branch and pushes again. The Pull Request updates automatically.

### Step 8 — Merge

Once approved, Amine merges the Pull Request into `main`.

Mariem then synchronizes:

```
git switch main
git pull origin main
```

# 4. Rules for a professional small team

I recommend these rules:

| Rule                  | Policy                     |
| --------------------- | -------------------------- |
| `main` branch         | Always stable              |
| Direct push to `main` | Avoid                      |
| Feature branches      | Required for contributions |
| Pull Requests         | Required before merging    |
| Code review           | At least one reviewer      |
| Commit messages       | Meaningful and consistent  |
| Tests                 | Run before merging         |
| Documentation         | Update when necessary      |

You can configure branch protection in GitHub under:

Settings → Rules → Rulesets

Create a ruleset targeting `main` and require Pull Requests before merging.

# 5. Responsibilities in your team

For example:

| Amine (maintainer)         | Mariem (contributor)          |
| -------------------------- | ----------------------------- |
| Define tasks               | Understand assigned task      |
| Maintain architecture      | Implement assigned feature    |
| Review Pull Requests       | Submit Pull Requests          |
| Manage `main`              | Fix review comments           |
| Resolve integration issues | Write tests and documentation |

# 6. Example of a real collaboration

Suppose your repository contains:

```
githab_learninig-/
├── code/
│   ├── BankAccount.java
│   └── TestBankAccount.java
├── cours/
│   ├── branch.md
│   └── git_history.md
└── README.md
```

You assign Mariem:

> Add Java examples demonstrating inheritance and polymorphism.

She creates:

```
git switch main
git pull origin main
git switch -c feature/java-inheritance
```

She adds her files, commits and pushes:

```
git add .
git commit -m "feat: add inheritance examples"
git push -u origin feature/java-inheritance
```

Then she opens a Pull Request. You review and merge it.

That's a professional contribution workflow.

## 7. What I recommend you learn next

Learn these Git concepts in this order:

1. Branching and branch naming.
2. Git merge.
3. Pull Requests.
4. Code review.
5. Merge conflicts and conflict resolution.
6. Branch protection.
7. GitHub Issues and task assignment.
8. GitHub Projects for project management.

My recommendation: For your two-person team, use GitHub Issues to assign tasks, feature branches for development, and Pull Requests for integration. This gives you a professional workflow without unnecessary complexity.



----------------------------------------------------------------
# Guide: Configure two GitHub accounts with SSH on Ubuntu

The goal is to use two GitHub accounts on the same computer without changing SSH keys manually.

- Mariem: `mariembenabdalh5-maker`
- Amine: `Mohamedaminesaadd`

## Step 1 — Understand your SSH keys

An SSH key consists of two files:

| File             | Purpose     |
| ---------------- | ----------- |
| `id_ed25519`     | Private key |
| `id_ed25519.pub` | Public key  |

- The private key stays on your computer.
- The public key is uploaded to GitHub.
- Never share your private key.

## Step 2 — Generate separate keys

Generate Mariem's key:

```
ssh-keygen -t ed25519 -C "MARIEM_EMAIL" -f ~/.ssh/id_ed25519
```

Generate Amine's key:

```
ssh-keygen -t ed25519 -C "AMINE_EMAIL" -f ~/.ssh/id_ed25519_amine
```

Important: Always use a different filename for each account. Never overwrite an existing key.

## Step 3 — Add public keys to GitHub

Display Mariem's public key:

```
cat ~/.ssh/id_ed25519.pub
```

Display Amine's public key:

```
cat ~/.ssh/id_ed25519_amine.pub
```

For each account:

1. Log in to the corresponding GitHub account.
2. Open [SSH and GPG keys](https://github.com/settings/keys?utm_source=chatgpt.com).
3. Click New SSH key.
4. Choose `Authentication Key`.
5. Give it a title, such as `MSI Ubuntu - Mariem` or `MSI Ubuntu - Amine`.
6. Paste the corresponding public key.

## Step 4 — Start SSH agent and add keys

```
eval "$(ssh-agent -s)"

ssh-add ~/.ssh/id_ed25519
ssh-add ~/.ssh/id_ed25519_amine
```

Check loaded keys:

```
ssh-add -l
```

## Step 5 — Configure SSH aliases

Open the configuration file:

```
nano ~/.ssh/config
```

Add:

```
# Mariem GitHub account
Host github-mariem
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

# Amine GitHub account
Host github-amine
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_amine
    IdentitiesOnly yes
```

Save and set permissions:

```
chmod 600 ~/.ssh/config
```

What does this configuration do?

| Alias           | GitHub server | Private key        |
| --------------- | ------------- | ------------------ |
| `github-mariem` | github.com    | `id_ed25519`       |
| `github-amine`  | github.com    | `id_ed25519_amine` |

The aliases allow SSH to select the correct account.

## Step 6 — Test authentication

Test Mariem:

```
ssh -T git@github-mariem
```

Expected:

```
Hi mariembenabdalh5-maker! You've successfully authenticated...
```

Test Amine:

```
ssh -T git@github-amine
```

Expected:

```
Hi Mohamedaminesaadd! You've successfully authenticated...
```

## Step 7 — Clone repositories

Clone Mariem's repository:

```
git clone git@github-mariem:MariemUsername/repository.git
```

Clone Amine's repository:

```
git clone git@github-amine:Mohamedaminesaadd/repository.git
```

## Step 8 — Configure commit identity per repository

Inside Mariem's project:

```
git config user.name "Mariem"
git config user.email "MARIEM_EMAIL"
```

Inside Amine's project:

```
git config user.name "Mohamed Amine Saad"
git config user.email "AMINE_EMAIL"
```

Check configuration:

```
git config --local --list
```

## Step 9 — Change an existing repository from HTTPS to SSH

If your existing repository uses HTTPS:

```
git remote -v
```

Change it to Amine's SSH alias:

```
git remote set-url origin git@github-amine:Mohamedaminesaadd/repository.git
```

Verify:

```
git remote -v
```

## Final architecture to remember

Your Ubuntu computer

Two GitHub identities

Mariem

github-mariem

Private key: `id_ed25519`

Public key: `id_ed25519.pub`

GitHub Mariem

Amine

github-amine

Private key: `id_ed25519_amine`

Public key: `id_ed25519_amine.pub`

GitHub Amine

## Quick command reference

| Command                   | Purpose                  |
| ------------------------- | ------------------------ |
| `ssh-keygen`              | Generate SSH key         |
| `cat ~/.ssh/*.pub`        | Display public keys      |
| `ssh-add`                 | Add private key to agent |
| `ssh-add -l`              | List loaded keys         |
| `nano ~/.ssh/config`      | Configure SSH aliases    |
| `chmod 600 ~/.ssh/config` | Secure SSH config        |
| `ssh -T git@github-amine` | Test authentication      |
| `git remote -v`           | Display remote URLs      |
| `git remote set-url`      | Change repository remote |

The most important concept: SSH authenticates your GitHub account, Git remote identifies the repository, and Git config identifies the commit author. These are three separate things.