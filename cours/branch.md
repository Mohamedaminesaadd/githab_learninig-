# Branch Creation & Branch Navigation

In Git, a Branch is an independent development line that allows you to work on new features or modifications without directly affecting the main development line.

For example, you can develop a login feature in a separate branch while keeping your `main` branch stable.

## 1. Understanding branches

Imagine your Git history:

```
A ---- B ---- C  (main)
```

You create a new branch called `feature-login`:

```
A ---- B ---- C  (main)
             \
              (feature-login)
```

Both branches initially point to the same commit, but they can evolve independently.

## 2. Branch creation commands

| Command                       | Description                    |
| ----------------------------- | ------------------------------ |
| `git branch`                  | List local branches            |
| `git branch feature-login`    | Create a branch                |
| `git branch -a`               | List local and remote branches |
| `git branch -d feature-login` | Delete a merged branch         |
| `git branch -D feature-login` | Force-delete a branch          |

## 3. Branch navigation commands

A. Switch to an existing branch

```
git switch feature-login
```

B. Create and switch to a new branch

```
git switch -c feature-login
```

C. Return to main

```
git switch main
```

Alternative older commands:

```
git checkout feature-login
git checkout -b feature-login
```

`git switch` is the modern command specifically designed for branch navigation.

## 4. Practical example

Suppose you have a Java project:

```
BankProject/
└── BankAccount.java
```

You want to develop a deposit feature separately.

Step 1 — Check current branch

```
git branch
```

Output:

```
* main
```

The `*` indicates your current branch.

Step 2 — Create a new branch

```
git branch feature-deposit
```

Step 3 — Switch to the new branch

```
git switch feature-deposit
```

Step 4 — Verify

```
git branch
```

Output:

```
* feature-deposit
  main
```

Step 5 — Modify your Java code and commit

```
git add .
git commit -m "Add deposit feature"
```

Step 6 — Return to main

```
git switch main
```

Your main branch does not contain the new feature commit yet.

## 5. Important concept: HEAD

`HEAD` indicates your current position in the Git repository.

Example:

```
A ---- B ---- C  (main)
             \
              D  (feature-deposit)
              ↑
             HEAD
```

Here:

- `main` points to commit C.
- `feature-deposit` points to commit D.
- `HEAD` points to your current branch, `feature-deposit`.

## 6. Commands to memorize

```
# List branches
git branch

# Create branch
git branch feature-login

# Switch branch
git switch feature-login

# Create and switch
git switch -c feature-login

# Return to main
git switch main

# List all branches
git branch -a

# Delete branch
git branch -d feature-login

# Force delete branch
git branch -D feature-login

# Check current branch and status
git status
```

## 7. Test your understanding

Mini quiz

1\. Which command creates a branch and switches to it immediately?

git branch feature

git switch -c feature

git merge feature



2\. What does the \* symbol mean in git branch output?

Deleted branch

Current branch

Remote branch



3\. Which command switches back to main?

git switch main

git branch main

git init main



Check answers



Remember: Branches allow you to develop different features independently without disturbing the main branch.

Next concept: Git Branch Merging (`git merge`).


# Git Branch & Merge — Command Summary

## 1. Branch Management

```
# List local branches
git branch

# List local and remote branches
git branch -a

# Create a new branch
git branch feature-login

# Create and switch to a new branch
git switch -c feature-login

# Switch to an existing branch
git switch feature-login

# Switch to main
git switch main

# Rename current branch
git branch -m new-name

# Delete a merged branch
git branch -d feature-login

# Force delete a branch
git branch -D feature-login

# Show current branch
git branch --show-current
```

## 2. Branch Integration (Merge)

```
# Switch to the destination branch
git switch main

# Merge feature branch into main
git merge feature-login

# Merge without fast-forward (force merge commit)
git merge --no-ff feature-login

# Abort an unfinished merge
git merge --abort

# Check merge status
git status

# Display branch history graph
git log --oneline --graph --all
```

## 3. Merge Conflict Resolution

```
# Check conflicting files
git status

# Edit conflicting files manually

# Stage resolved files
git add file.java

# Complete merge
git commit

# Abort merge if necessary
git merge --abort
```

## 4. Complete Workflow Example

```
# 1. Create feature branch
git switch -c feature-login

# 2. Modify files

# 3. Stage changes
git add .

# 4. Commit changes
git commit -m "Add login feature"

# 5. Return to main
git switch main

# 6. Merge feature branch
git merge feature-login

# 7. Verify history
git log --oneline --graph --all

# 8. Delete feature branch
git branch -d feature-login
```

## 5. Most Important Commands for the Exam

| Command                           | Purpose           |
| --------------------------------- | ----------------- |
| `git branch`                      | List branches     |
| `git branch name`                 | Create branch     |
| `git switch name`                 | Switch branch     |
| `git switch -c name`              | Create and switch |
| `git branch -d name`              | Delete branch     |
| `git merge name`                  | Merge branch      |
| `git merge --abort`               | Cancel merge      |
| `git status`                      | Check conflicts   |
| `git log --oneline --graph --all` | Visualize history |

Remember the workflow:

Create

git switch -c feature

Develop

git add . → git commit

Return

git switch main

Integrate

git merge feature