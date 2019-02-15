# falcon-test

Minimal instructions to run the project:

```
$ virtualenv falcon
$ falcon/bin/activate
(falcon) $ pip install -r requirements.txt
(falcon) $ gunicorn app:api --reload
```

Running the client:

```
$ falcon/bin/activate
(falcon) $ python client.py
Code: 200
Text: {"age": "Unknown", "name": "Oscar"}
...
```
