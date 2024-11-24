# ALTEN TEST
This project uses Python, behave and Selenium.

<br/>

## Installation

1.  Open your terminal and clone the repository:
    ```bash
    git clone https://github.com/melinapared02/alten_test.git
    cd alten_test
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    ```
    - Windows
        ```bash
        .venv\Scripts\activate
        ```
    - Linux/macOS
        ```bash
        source .venv/bin/activate
        ```
    

3. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

<br/>

## Run tests

```bash
behave
```

<br/>

## Project structure

    alten_test/
    │
    ├── tests/                              # Directory containing the tests
    │   ├── features/                       # Directory containing the BDD test specification files
    │   │   ├── steps/                      # Directory containing step definitions for BDD tests
    │   │   │   └── map_of_locations.py
    │   │   ├── environment.py
    │   │   └── map_of_locations.feature
    │   └── screen/                         # Directory containing classes for interacting with web pages using Selenium
    │       └── home.py
    │
    ├── .gitignore                          # File specifying the files and directories ignored by Git
    ├── behave.ini                          # File with the configuration of the behave library
    ├── README.md                           # Project documentation
    └── requirements.txt                    # File specifying the project dependencies
