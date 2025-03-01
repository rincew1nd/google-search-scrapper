### Example Application on the Theme "How to Scrape Google Search"

- Headless mode with Firefox:
```docker-compose -f docker-compose-headless.yml up --build```

- Headed mode with Chromium:
```docker-compose -f docker-compose-headed.yml up --build```

- Local run
```
set HEADLESS=True && python run.py
set HEADLESS=False && python run.py
```

- Unit tests
```python -m unittest discover```