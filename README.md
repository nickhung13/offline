Web automation testing with page object (simple version)

Installation Guide
-----------
#### Mac (M1 chip) ####


- According to your OS to download Chrome driver
    - In OSX/Linux: 
        - `$ brew install --cask chromedriver`
        - switch to your chromedriver path
        - fix permission issue on Mac `$ xattr -d com.apple.quarantine chromedriver`
- Install Python >= 3.11
    - `$ brew install python 3`
- Install a virtual environment tool
- Use a virtual env to install requirements.txt
    - `$ pip install -r requirements.txt`

* The project is running on Selenium 3, not 4. Please check the requirements.txt

* Run  test case

```no-highlight
    $ python -m unittest tests/test_login.py
```

