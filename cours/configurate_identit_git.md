configurate identity in git it helps to set up your user information for commits. This is important because Git uses this information to identify the author of each commit. You can configure your identity using the following commands:


 and the githun use the identity to show the author of the commits in the repository.


 # GitHub Problem Summary: Amine vs Mariem Identity

## 1. The problem

We have two GitHub accounts on the same Ubuntu machine:

- Amine: `Mohamedaminesaadd`
- Mariem: `mariembenabdalh5-maker`

We wanted Mariem to contribute to Amine's repository:

`Mohamedaminesaadd/githab_learninig-`

However, when Mariem made commits, GitHub displayed Amine as the author.

Why? Because Git was configured with Amine's identity:

```
git config user.name
# amine saad
```

Even though the remote URL used Mariem's SSH alias, the commit author was still Amine.

## 2. Understand the three independent configurations

This is the most important lesson.

| Configuration       | Purpose                                      | Example             |
| ------------------- | -------------------------------------------- | ------------------- |
| SSH authentication  | Determines which GitHub account connects     | Mariem's SSH key    |
| Git author identity | Determines who appears as commit author      | Mariem's name/email |
| Git remote          | Determines which repository receives commits | Amine's repository  |

Changing one does not automatically change the others.

## 3. Our SSH configuration

We use SSH aliases to distinguish the two GitHub accounts.

File: `~/.ssh/config`

```
# Mariem account
Host github-mariem
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

# Amine account
Host github-amine
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_amine
    IdentitiesOnly yes
```

Test each account:

```
ssh -T git@github-mariem
ssh -T git@github-amine
```

Expected:

```
Hi mariembenabdalh5-maker!
Hi Mohamedaminesaadd!
```

## 4. Configure the identity for each repository

Git identity can be configured globally or locally.

For Mariem's repository:

```
cd ~/Documents/github_mariem/githab_learninig-

git config user.name "mariembenabdalh5-maker"
git config user.email "MARIEM_EMAIL"
```

For Amine's repository:

```
git config user.name "amine saad"
git config user.email "AMINE_EMAIL"
```

Use the correct email associated with each GitHub account.

Check the configuration:

```
git config user.name
git config user.email
```

Use local configuration when the same machine is shared by multiple GitHub users.

## 5. Configure the remote repository

For Mariem to contribute to Amine's repository:

```
git remote set-url origin git@github-mariem:Mohamedaminesaadd/githab_learninig-.git
```

Check:

```
git remote -v
```

Expected:

```
origin git@github-mariem:Mohamedaminesaadd/githab_learninig-.git (fetch)
origin git@github-mariem:Mohamedaminesaadd/githab_learninig-.git (push)
```

Mariem must also have accepted the collaborator invitation.

## 6. The correct workflow before every contribution

Use this workflow to avoid repeating the problem.

```
# 1. Go to the correct repository
cd ~/Documents/github_mariem/githab_learninig-

# 2. Check current branch
git branch

# 3. Check current identity
git config user.name
git config user.email

# 4. Check remote
git remote -v

# 5. Synchronize with GitHub
git switch main
git pull --ff-only origin main

# 6. Create a feature branch
git switch -c feature/mariem-task

# 7. Work on your files
git add .
git commit -m "feat: implement Mariem task"

# 8. Check commit author
git log -1 --format="%h | %an <%ae>"

# 9. Push the branch
git push -u origin feature/mariem-task
```

Then create a Pull Request on GitHub to merge the feature branch into `main`.

## 7. Five commands to remember

| Command                           | Purpose                    |
| --------------------------------- | -------------------------- |
| `git config user.name`            | Check commit name          |
| `git config user.email`           | Check commit email         |
| `git remote -v`                   | Check remote repository    |
| `ssh -T git@github-mariem`        | Test Mariem authentication |
| `git log -1 --format="%an <%ae>"` | Check latest commit author |

## 8. Golden rule

Before making a commit, always verify these three things:

1. Who am I? → `git config user.name`
2. Which account authenticates? → `ssh -T git@github-mariem`
3. Where am I pushing? → `git remote -v`

One final distinction: Changing Git identity affects only new commits. Existing commits remain attributed to their original authors unless their history is rewritten. Never force-push a shared branch just to correct attribution without coordinating with collaborators.

You can save this summary as `github_two_accounts_workflow.md` for future reference.