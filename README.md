### Ducklings Screensaver

---

#### **Project Description**
**Ducklings Screensaver** is a fun and animated screensaver that displays ducklings moving across the screen with various features and characteristics. The project is written in Python and utilizes an object-oriented approach to create and manage animations.

---

#### **How the Screensaver Works**
- Ducklings randomly appear in different "lanes" on the screen.
- Each duckling is composed of a head, body, and feet, displayed sequentially.
- Ducklings can be "chubby" or "very chubby," with different facial expressions and wing positions.
- The animation runs continuously until `Ctrl+C` is pressed.

---

#### **System Requirements**
- Python 3.8 or later
- A terminal that supports text output (e.g., Windows Command Prompt, macOS Terminal, or Linux Terminal).

---

#### **Installation and Running the Project**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ducklings.git
   cd ducklings
   ```

2. **Create a virtual environment (optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies (if any):**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the project:**
   ```bash
   python main.py
   ```

---

#### **Features**
- Random generation of ducklings with unique characteristics.
- Configurable animation speed (`PAUSE`).
- Configurable duckling density on the screen (`DENSITY`).
- Extensible object-oriented codebase.

---

#### **Project Structure**
```
ducklings/
├── ducklings/
│   ├── __init__.py          # Defines the module
│   ├── config.py            # Constants and settings
│   ├── duckling.py          # Duckling class
│   ├── screensaver.py       # Main screensaver logic
│
├── tests/
│   ├── __init__.py          # Test module
│   ├── test_config.py       # Tests for config.py
│   ├── test_duckling.py     # Tests for Duckling class
│   ├── test_screensaver.py  # Tests for Screensaver
│
├── main.py                  # Entry point for the application
├── requirements.txt         # Dependency list
├── README.md                # Documentation
└── .flake8                  # Flake8 configuration
```

---

#### **Customization**
You can modify parameters in the `config.py` file to customize the screensaver:
- **`PAUSE`**: Adjusts animation speed. For example, `0.1` for faster animation or `0.5` for slower animation.
- **`DENSITY`**: Sets the probability of a duckling appearing in each "lane." For example, `0.2` results in more ducklings, while `0.05` results in fewer.

---

#### **Testing**
The project includes unit tests located in the `tests` folder. You can run them using the following commands:

1. **Using `unittest`:**
   ```bash
   python -m unittest discover -s tests
   ```

2. **Using `pytest` (if installed):**
   ```bash
   pytest
   ```

---

#### **Support**
If you have questions or suggestions, feel free to open a new issue on the [project repository](https://github.com/your-username/ducklings/issues).

---

#### **License**
This project is distributed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
