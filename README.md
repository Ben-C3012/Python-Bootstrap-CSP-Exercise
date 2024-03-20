# Content Security Policy + XSS Exercise 

## Installation

1. Create a new virtual environment:
```python3 -m venv env```
2. Activate the virtual environment:
 ```source env/bin/activate```
3. Install the packages from the requirements.txt file:
 ```pip install -r requirements.txt```

## Usage

1. Run a live server instance of the HTML page. 
2. Run the Flask server using ```python app.py```

## Instructions

1. The app is vulnerable to XSS. Try to inject iframes and scripts into the page.
2. Uncomment the meta tag CSP in the index.html file.
3. The website is broken because the CSP is not written correctly.
4. Delete the malicious comments from the "Database".
5. Fix the CSP so the website will work - scripts, styles, iframes, etc. 
6. Fix the XSS vulnerability using a sanitizing library of your choice.
