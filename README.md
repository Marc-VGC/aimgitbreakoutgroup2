# aimgitbreakoutgroup2
Practice push, pull, and merge conflict resolution


Breakout Room Activity:
Git Collaboration Challenge
Overview
Duration 25–30 minutes
Tools Needed GitHub account, Git installed, terminal or VS Code
Goal Practice push, pull, and merge conflict resolution
Related Materials Python Fundamentals Notebook & Practice
Assignment
Phase 1: Setup (5 min)
1. One student creates a GitHub repo called python-collab-lab
2. Add group members as collaborators.
3. Everyone clones the repo
4. Push the starter calculator.py file
Phase 2: Clean Pushes (8 min)
Each member creates a separate file:
Member Task
Student A Create greetings.py
Student B Create temperature.py
Student C Create fizzbuzz.py
Student D Create swap.py
Note: You can use code from the assignment, or just put some AI generated python code.
Each student runs:
git add .
git commit -m "Add <filename> by <your name>"
git push origin main
Important: After the first person pushes, everyone else will need to pull before pushing:

Phase 3: Intentional Merge Conflict (15 min)
All members edit calculator.py simultaneously, adding different functions on the same line
range.
Step 1: Everyone opens calculator.py
Step 2: Each member adds a different function below the TODO comment:
Member Function to Add
Student A def multiply(a, b): return a * b
Student B def divide(a, b): return a / b if b != 0 else "Error"
Student C def power(a, b): return a ** b
Student D def modulus(a, b): return a % b
Step 3: Student A commits and pushes first (this goes through cleanly):
git add .
git commit -m "Add multiply function"
git push origin main
Step 4: Student B tries to push and gets REJECTED:
git add .
git commit -m "Add divide function"
git push origin main ← REJECTED
git pull origin main ← MERGE CONFLICT
Step 5: Student B opens calculator.py and sees something like:
<<<<<<< HEAD
def divide(a, b): return a / b if b != 0 else "Error"
=======
def multiply(a, b): return a * b
>>>>>>> origin/main
Step 6: Resolve by keeping BOTH functions and removing the conflict markers (<<<,
===, >>>), then:
git add calculator.py
git commit -m "Resolve merge conflict — keep both functions"
git push origin main
Step 7: Repeat for Students C and D.
git pull origin main
git push origin main
Checkpoint: Everyone pulls and confirms all files are in the repo.

Note: you can try other git tools (e.g. Github Desktop, VS Code or Cursor extensions).
For experienced developers, please share your experience with the rest of the breakout
room.
Phase 4: Verify & Discuss (10 min)
Everyone pulls, verifies all functions exist, and runs the file.
Git Cheat Sheet
Command What It Does
git clone <url> Download repo
git add . Stage all changes
git commit -m 'msg' Save snapshot locally
git push origin main Upload to GitHub
git pull origin main Download & merge latest
git status See what's changed
