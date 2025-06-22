# fullstack_mercedes_backend
The BackEnd repository of FullStack Mercedez Quiz 

For start the app, use this command:
```bash
python -m uvicorn app.main:app --reload
```

To generate tests:
```bash
python -m pytest -v
```

Or if you want also generate a coverge of tests result:
```bash
python -m pytest --cov=app -v
```

And if also wants the HTML report:
```bash
python -m pytest --cov=app --cov-report=html
```