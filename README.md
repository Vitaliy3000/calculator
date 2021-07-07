# calculator

Web service can add two integer numbers.

# Frontend

## Running
```
cd frontend
npm install
npm run dev
```

# Backend

## Running
```
cd backend
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
deactivate
```

## Methods
* POST /calc


# Running tests
```
cd backend
virtualenv .venv_test
source .venv_test/bin/activate
pip install -r requirements.txt -r requirements.test.txt
python -m pytest
deactivate
```