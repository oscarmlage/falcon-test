# falcon-test

Minimal instructions:

```
$ virtualenv falcon
$ falcon/bin/activate
(falcon) $ pip install -r requirements.txt
(falcon) $ gunicorn app:api --reload
```