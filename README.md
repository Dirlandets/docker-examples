# Install 
```
pip install --upgrade pip && pip install pipenv && pipenv install --dev
```

# Run
```
export FLASK_ENV=development FLASK_APP=app && flask run
```

# Run with docker
```
docker build .
docker run -p 5000:5000 -e FLASK_APP=app -e FLASK_ENV=development -e DB_URL=sqlite:///mydb2.db d70529204d17
```