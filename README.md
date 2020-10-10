**Source**
https://github.com/15Dkatz/python-blockchain-tutorial

**Activate the virtual environment**
´´´
python -m venv .venv
´´´

**Install all packages**
´´´
pip install -r requirements.txt
´´´

**Running tests**

Make sure to activate the virtual environment.

´´´
python -m pytest backend/tests
´´´

**Running the application and API**

Make sure to activate the virtual environment.

´´´
python -m backend.app
´´´

**Running a peer**
Make sure to activate the virtual environment.

´´´

\$env:PEER = 'True'; python -m backend.app

´´´
