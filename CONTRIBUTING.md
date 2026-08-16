# Contributing to Nexora

Thank you for your interest in contributing to **Nexora**! We welcome contributions from everyone to help make Nexora a robust e-commerce and business intelligence platform.

---

## 🛠️ Getting Started

### 1. Prerequisites
- **Python**: Version 3.10, 3.11, or 3.12 (or newer).
- **Git**: For version control.

### 2. Fork and Clone
```bash
git clone https://github.com/VasanthaGudapati/Nexora.git
cd Nexora
```

### 3. Set Up a Virtual Environment
- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 💻 Development Workflow

### 1. Create a Topic Branch
Branch from `main` with a clear, descriptive name:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Code Style & Quality
Nexora uses **Ruff** for linting and formatting. Ensure your code conforms to our standards before committing:

```bash
# Check for linting issues
ruff check .

# Automatically fix linting issues
ruff check --fix .

# Format code
ruff format .
```

### 3. Running Automated Tests
We use **Pytest** for our automated test suite. Run tests locally from the root folder:

```bash
pytest
```

Ensure all tests pass before opening a Pull Request.

---

## 📝 Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` A new feature (e.g., `feat: add customer sales aggregation endpoint`)
- `fix:` A bug fix (e.g., `fix: resolve division by zero in average order value`)
- `docs:` Documentation only changes (e.g., `docs: update README with API setup`)
- `test:` Adding missing tests or correcting existing tests (e.g., `test: add unit tests for orders router`)
- `refactor:` Code change that neither fixes a bug nor adds a feature
- `chore:` Changes to the build process, tooling, or auxiliary dependencies

---

## 🚀 Submitting a Pull Request

1. Push your branch to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Open a Pull Request on GitHub against the `main` branch.
3. Fill out the **Pull Request Template** provided.
4. Ensure the GitHub Actions CI workflow passes.
5. Address any code review feedback promptly.

---

## 💬 Questions and Support
If you encounter any bugs or have feature suggestions, please open an issue using our [Issue Templates](https://github.com/VasanthaGudapati/Nexora/issues).
