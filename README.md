A RESTful flask api for interacting with my Postgresql database.

Initial functionality will be limited to allowing users to pull down quiz sets that I upload.  Eventually I'll figure out a good way to implement user submissions.

**Credit to Onwuka Gideon, author of [this](https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx) tutorial which my project is loosely(ish) based upon.**

**NOTE**
I have left out my config.py file as it contains the username/password of my postgres db, as well as the venv directory I created for this project (less issues if everyone just creates their own venv).

You may have to install the required modules (will check after commit).  To do so activate your venv, and from within your venv run the following:

```bash
    $ pip3 install -r requirements.txt
```

For instructions on how to set up your own config.py: follow the link above to Onwuka's tutorial and locate **Step 2: Setting up configuration**
