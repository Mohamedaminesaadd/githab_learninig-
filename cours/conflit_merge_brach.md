# Conflict Detection & Manual Resolution (Git)

A Merge Conflict occurs when Git cannot automatically combine changes from two branches.

This commonly happens when two branches modify the same lines of the same file.

## 1. How does a conflict happen?

Imagine you have two branches: `main` and `feature`.

Both modify the same line in `BankAccount.java`.

main branch:

```
private double balance = 100;
```

feature branch:

```
private double balance = 200;
```

Git cannot decide which value to keep.

## 2. Conflict Detection

When you execute:

```
git switch main
git merge feature
```

Git may display:

```
CONFLICT (content): Merge conflict in BankAccount.java
Automatic merge failed; fix conflicts and then commit the result.
```

To identify conflicting files:

```
git status
```

## 3. Manual Conflict Resolution

Git modifies the conflicting file and inserts conflict markers:

```
<<<<<<< HEAD
private double balance = 100;
=======
private double balance = 200;
>>>>>>> feature
```

Explanation:

| Marker            | Meaning                         |
| ----------------- | ------------------------------- |
| `<<<<<<< HEAD`    | Start of current branch changes |
| `=======`         | Separator between versions      |
| `>>>>>>> feature` | End of incoming branch changes  |

You must manually edit the file and choose the correct result.

For example:

```
private double balance = 150;
```

Remove all conflict markers.

## 4. Complete the merge

After resolving the conflict:

```
# 1. Check status
git status

# 2. Stage resolved file
git add BankAccount.java

# 3. Complete merge
git commit -m "Resolve merge conflict"

# 4. Check history
git log --oneline --graph --all
```

## 5. Cancel a merge

If you don't want to continue the merge:

```
git merge --abort
```

This attempts to restore the state before the merge started.

## 6. Complete workflow

```
# Create feature branch
git switch -c feature

# Modify file and commit
git add .
git commit -m "Modify balance"

# Return to main
git switch main

# Modify the same line and commit
git add .
git commit -m "Update balance"

# Merge feature into main
git merge feature

# Detect conflicts
git status

# Manually resolve conflicts in the file

# Stage resolution
git add BankAccount.java

# Complete merge
git commit
```

## 7. Commands to memorize

| Command             | Purpose                   |
| ------------------- | ------------------------- |
| `git merge branch`  | Merge another branch      |
| `git status`        | Detect conflicting files  |
| `git diff`          | Inspect differences       |
| `git add file`      | Mark conflict as resolved |
| `git commit`        | Complete the merge        |
| `git merge --abort` | Cancel the merge          |

À retenir pour l'examen

Conflict Detection: Git identifies incompatible changes.

Manual Resolution: Developer chooses or combines the correct changes.

Completion: `git add` → `git commit`.

Important: Git does not automatically know which version is correct. The developer makes that decision.