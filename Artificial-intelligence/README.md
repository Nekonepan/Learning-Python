# Artificial Intelligence

This folder contains Python exercises and small experiments for learning basic Artificial Intelligence concepts.

---

## Purpose

This directory is used to practice AI topics such as:

- Blind search / uninformed search
- Heuristic search and tracking
- Knowledge representation
- Basic reasoning implementation

The code is organized by topic so each example can be studied and run independently.

---

## Folder Structure

```text
Artificial-intelligence/
├── Blind-tracking/
├── Heuristic-tracking/
│   ├── Heuristic-Tracking/
│   └── Post/
├── Implementation-of-Reasoning/
│   ├── Main/
│   └── Post/
└── Knowledge-Representation/
    ├── Knowledge-Representation/
    └── Post/
```

---

## Requirements

General requirements:

- Python 3
- pip
- venv support
- make

On Debian, Ubuntu, or Linux Mint:

```bash
sudo apt install python3 python3-pip python3-venv make
```

On Arch Linux:

```bash
sudo pacman -S python python-pip make
```

On macOS with Homebrew:

```bash
brew install python make
```

Windows users should run these examples through WSL, Git Bash, or MSYS2. The Makefiles use Unix-style shell commands.

---

## How to Run

Some folders include a `Makefile`. From inside one of those folders, run:

```bash
make run
```

Example:

```bash
cd Heuristic-tracking/Heuristic-Tracking
make run
```

or:

```bash
cd Knowledge-Representation/Post
make run
```

The Makefiles will:

- Detect `python3` or `python`
- Try to use the system Python environment
- Create a local `.venv` if system package installation is unavailable
- Install the local `ai_pkg` wheel when needed
- Run the Python script

---

## Running Scripts Manually

For folders without a Makefile, run Python files directly:

```bash
python3 filename.py
```

Example:

```bash
cd Blind-tracking
python3 main.py
```

If a script requires extra packages, create a virtual environment first:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 filename.py
```

---

## Notes

The `Heuristic-tracking` and `Knowledge-Representation` examples use local `ai_pkg` wheel files included in their folders.

Do not commit generated virtual environment folders such as:

```text
.venv/
venv/
```

They can be recreated when needed.

---

## Author

Nekonepan
