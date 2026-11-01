## 1. What is `git init`?

`git init` is a Git command used to initialize a new Git repository inside a project directory.

It tells Git: "Start tracking this project and its changes."

Before initialization, your project is just a normal directory. After initialization, Git creates a hidden directory called `.git` that stores repository information, configuration, and commit history.

## 2. Practical example

Imagine you have this project:

```
MyProject/
├── BankAccount.java
├── BankAccountTest.java
└── README.md
```

Open your terminal inside `MyProject`:

```
cd MyProject
```

Initialize Git:

```
git init
```

You will see something similar to:

```
Initialized empty Git repository in /home/user/MyProject/.git/
```

Your project now looks like:

```
MyProject/
├── .git/
├── BankAccount.java
├── BankAccountTest.java
└── README.md
```

The `.git` directory is hidden and contains Git's internal data.

## 3. Complete initialization workflow

```
# 1. Create a project directory
mkdir MyProject

# 2. Enter the directory
cd MyProject

# 3. Initialize Git
git init

# 4. Create a file
echo "# My Project" > README.md

# 5. Check repository status
git status

# 6. Add the file to staging
git add README.md

# 7. Create your first commit
git commit -m "Initial commit"
```

## 4. Useful commands after initialization

| Command                                     | Description               |
| ------------------------------------------- | ------------------------- |
| `git init`                                  | Initialize a repository   |
| `git status`                                | Check repository status   |
| `git config --list`                         | Display Git configuration |
| `git config user.name "Your Name"`          | Configure username        |
| `git config user.email "email@example.com"` | Configure email           |
| `git log`                                   | Display commit history    |
| `git rev-parse --show-toplevel`             | Display repository root   |

## 5. Configure your Git identity

Before making commits, configure your identity:

```
git config --global user.name "Mohamed Amine"
git config --global user.email "your-email@example.com"
```

`--global` means this configuration applies to all your Git repositories for your current user account.

To configure it for only one project, remove `--global`.

## 6. Important: `git init` vs `git clone`

| `git init`                            | `git clone`                         |
| ------------------------------------- | ----------------------------------- |
| Creates a new local repository        | Copies an existing repository       |
| Starts with no project commit history | Retrieves existing commit history   |
| Used for a new project                | Used for an existing GitHub project |

Remember: `git init` creates a local Git repository. It does not automatically create a GitHub repository or upload your code.

Next, learn `git remote add origin`, which connects your local repository to a remote GitHub repository.