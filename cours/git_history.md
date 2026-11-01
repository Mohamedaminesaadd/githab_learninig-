# Git History Investigation

Git History Investigation means examining the history of changes made to a Git repository.

Git records commits, authors, dates, and commit messages. By investigating this history, you can understand:

- Who modified the code?
- When was a modification made?
- What files were changed?
- Why was a change introduced?
- What was the previous version of a file?

## 1. The `git log` command

The most basic command to inspect Git history is:

```
git log
```

Example output:

```
commit a82f1c3
Author: Mohamed Amine
Date:   Sun Nov 1 14:00:00 2026

    Add BankAccount class

commit b73e9d2
Author: Mohamed Amine
Date:   Sun Nov 1 13:30:00 2026

    Initial commit
```

Each commit contains:

- Commit hash: unique identifier.
- Author: person who created the commit.
- Date: when the commit was created.
- Message: description of the changes.

## 2. Important Git history commands

| Command               | Description                       |
| --------------------- | --------------------------------- |
| `git log`             | Display commit history            |
| `git log --oneline`   | Display compact history           |
| `git log --graph`     | Display history as a graph        |
| `git log --all`       | Show commits from all references  |
| `git log -5`          | Show the last 5 commits           |
| `git show`            | Show details of a commit          |
| `git diff`            | Compare changes                   |
| `git blame file.java` | Identify who modified each line   |
| `git log --stat`      | Show files changed and statistics |

### A. Compact history

```
git log --oneline
```

Example:

```
a82f1c3 Add BankAccount class
b73e9d2 Initial commit
```

### B. Visualize commit history

```
git log --oneline --graph --all
```

Example:

```
* a82f1c3 Add authentication
* b73e9d2 Add BankAccount class
* c64d8f1 Initial commit
```

This is particularly useful when working with branches.

### C. Investigate a specific commit

```
git show a82f1c3
```

Displays:

- Commit information.
- Modified files.
- Changes introduced by the commit.

### D. Investigate who modified a line

```
git blame BankAccount.java
```

Example:

```
a82f1c3 (Mohamed 2026-11-01) private double balance;
b73e9d2 (Mohamed 2026-11-01) public String getOwner()
```

This helps identify the author of each line according to Git history.

## 3. Practical Lab: Git History Investigation

Let's create a small project and investigate its history.

Step 1 — Initialize a repository

```
mkdir GitHistoryLab
cd GitHistoryLab
git init
```

Step 2 — Create a Java file

Create `BankAccount.java`:

```
public class BankAccount {

    private double balance;

    public BankAccount(double balance) {
        this.balance = balance;
    }

    public double getBalance() {
        return balance;
    }
}
```

Step 3 — Create the first commit

```
git add .
git commit -m "Create BankAccount class"
```

Step 4 — Modify the file

Add a deposit method:

```
public void deposit(double amount) {
    balance += amount;
}
```

Create another commit:

```
git add .
git commit -m "Add deposit method"
```

Step 5 — Investigate the history

Execute:

```
git log --oneline
```

Then:

```
git show HEAD
```

And:

```
git blame BankAccount.java
```

You can now identify the changes introduced by each commit.

## 4. Understanding HEAD

In Git, `HEAD` is a reference that normally points to the currently checked-out commit (or branch).

For example:

```
A ---- B ---- C
             ↑
            HEAD
```

- A: Initial commit.
- B: Add BankAccount class.
- C: Add deposit method.
- HEAD: Current position.

To inspect the current commit:

```
git show HEAD
```

To inspect the previous commit:

```
git show HEAD~1
```

To inspect two commits before:

```
git show HEAD~2
```

## 5. Summary: Commands to remember

| Command                | Purpose                     |
| ---------------------- | --------------------------- |
| `git log`              | Explore history             |
| `git log --oneline`    | Compact history             |
| `git show HEAD`        | Inspect current commit      |
| `git show HEAD~1`      | Inspect previous commit     |
| `git blame file`       | Investigate line authorship |
| `git diff HEAD~1 HEAD` | Compare two commits         |

Important: Git History Investigation is useful for debugging, tracking modifications, understanding project evolution, and collaborating with other developers.

Next concept to learn: Git Branching and Merging.




## Git Commands – Tracking History

```
# Initialize repository
git init

# Check repository status
git status

# Add files to staging
git add .
git add file.java

# Display unstaged changes
git diff

# Display staged changes
git diff --staged
git diff --cached

# Display all changes compared to last commit
git diff HEAD

# Display commit history
git log

# Display compact commit history
git log --oneline

# Display last 5 commits
git log -5

# Display history as a graph
git log --oneline --graph --all

# Display details of the latest commit
git show

# Display details of a specific commit
git show <commit-hash>

# Compare two commits
git diff <commit-hash-1> <commit-hash-2>

# Display modified files in a commit
git show --stat <commit-hash>

# Track who modified each line
git blame file.java

# Display history of a specific file
git log -- file.java

# Display file history with changes
git log -p -- file.java

# Create a commit
git commit -m "Commit message"

# Remove changes from staging
git restore --staged file.java

# Discard unstaged modifications
git restore file.java
```

Most important commands to memorize for Git History Investigation:

```
git status
git log
git log --oneline
git show
git diff
git diff --staged
git diff HEAD
git blame file.java
```