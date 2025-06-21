# fullstack_mercedes_backend
The BackEnd repository of FullStack Mercedez Quiz 

For start the app, use this command:
```
python -m uvicorn app.main:app --reload
```

To generate tests:
```
python -m pytest -v
```

Or if you want also generate a coverge of tests result:
```
python -m pytest --cov=app -v
```

And if also wants the HTML report:
```
python -m pytest --cov=app --cov-report=html
```