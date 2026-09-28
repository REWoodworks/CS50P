# %% [markdown]
# # APIs and JSON Reference (`requests` + `json`)
#
# An **API** is a URL that returns data instead of a web page. Usually that data is **JSON**:
# text that looks like Python dicts and lists.
# - `requests` fetches it.
# - `.json()` or the `json` module turns it into real dicts and lists.
# - From there, use `GoTo Dict.py` and `GoTo List.py` to work with it.
#
# Setup: `pip install requests` (third-party). `json` is built in.
#
# Every code cell runs on its own. `# -> result` shows what a line returns or prints.
# `# e.g.` marks live data that changes from run to run. Cells that call an API need internet.
#
# 1. Cheat sheet
# 2. JSON ↔ Python types
# 3. `json.loads` / `json.dumps`: strings
# 4. `json.load` / `json.dump`: files
# 5. Navigating nested JSON
# 6. JSON errors
# 7. `requests.get` and the Response object
# 8. Query parameters
# 9. Status codes and error handling
# 10. Headers and API keys
# 11. Sending data: POST / PUT / DELETE
# 12. Sessions
# 13. Complete program pattern (CS50P `itunes.py`)
# 14. Pitfalls
#
# Sources: CS50P Lecture 4 (`itunes0-2.py`), Python docs (`json` module),
# Requests docs (Quickstart, Advanced Usage).
# Test APIs used: jsonplaceholder.typicode.com (fake data that never changes), httpbin.org (echoes back what you send), iTunes Search.


# %% [markdown]
# ## 1. Cheat sheet

# %%
import json
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"id": 1},                # added to the URL as ?id=1
    timeout=10,                      # seconds; always set one
)
response.status_code                 # -> 200
response.ok                          # -> True  # True for any status below 400
response.raise_for_status()          # raises HTTPError for 4xx/5xx; does nothing if OK

data = response.json()               # JSON text -> Python list/dict
data                                 # -> [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}]
data[0]["title"]                     # -> 'delectus aut autem'

text = json.dumps(data[0])           # Python -> JSON string
text                                 # -> '{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}'
json.loads(text)["completed"]        # -> False  # JSON string -> Python
print(json.dumps(data[0], indent=2)) # pretty-print to see the structure
# -> {
# ->   "userId": 1,
# ->   "id": 1,
# ->   "title": "delectus aut autem",
# ->   "completed": false
# -> }

# json.dump(data, file)      # Python -> JSON file   (§4)
# json.load(file)            # JSON file -> Python   (§4)
# Memory aid: the "s" in loads/dumps means "string".


# %% [markdown]
# ## 2. JSON ↔ Python types
#
# | JSON | Python |
# |---|---|
# | object `{"k": v}` | `dict` |
# | array `[1, 2]` | `list` |
# | string `"text"` | `str` |
# | number `5`, `2.5` | `int`, `float` |
# | `true` / `false` | `True` / `False` |
# | `null` | `None` |
#
# JSON rules that differ from Python:
# - Strings use **double quotes** only.
# - Object keys are **always strings**.
# - No trailing commas.
# - No comments.

# %%
import json

text = '{"name": "Harry", "age": 17, "wand": null, "alive": true, "pets": ["Hedwig"]}'
data = json.loads(text)
data                          # -> {'name': 'Harry', 'age': 17, 'wand': None, 'alive': True, 'pets': ['Hedwig']}
type(data)                    # -> <class 'dict'>
type(data["pets"])            # -> <class 'list'>
data["wand"] is None          # -> True


# %% [markdown]
# ## 3. `json.loads` and `json.dumps`: strings
# - `json.loads(text)` reads a **JSON string** and returns Python objects.
# - `json.dumps(obj)` takes Python objects and returns a **JSON string**.

# %%
import json

student = {"name": "Hermione", "house": "Gryffindor", "grades": [98, 100], "prefect": True}

json.dumps(student)                         # -> '{"name": "Hermione", "house": "Gryffindor", "grades": [98, 100], "prefect": true}'
json.dumps(student, sort_keys=True)         # -> '{"grades": [98, 100], "house": "Gryffindor", "name": "Hermione", "prefect": true}'
json.dumps(student, separators=(",", ":"))  # -> '{"name":"Hermione","house":"Gryffindor","grades":[98,100],"prefect":true}'  # most compact

print(json.dumps(student, indent=2))        # readable (CS50P itunes1.py)
# -> {
# ->   "name": "Hermione",
# ->   "house": "Gryffindor",
# ->   "grades": [
# ->     98,
# ->     100
# ->   ],
# ->   "prefect": true
# -> }

json.loads('[1, 2.5, "three", null]')       # -> [1, 2.5, 'three', None]

# %% [markdown]
# ### Round trips don't always come back identical
# - Tuples become lists.
# - Non-string keys become strings.
# - Non-ASCII characters are escaped unless you pass `ensure_ascii=False`.

# %%
import json

json.loads(json.dumps((1, 2)))              # -> [1, 2]  # tuple came back as a list
json.loads(json.dumps({1: "one"}))          # -> {'1': 'one'}  # int key came back as a string
json.dumps({"city": "Zürich"})              # -> '{"city": "Z\\u00fcrich"}'
json.dumps({"city": "Zürich"}, ensure_ascii=False)   # -> '{"city": "Zürich"}'


# %% [markdown]
# ## 4. `json.load` and `json.dump`: files
# Use these to save API results so you can work offline, or to store settings.
# In your own code, a plain filename like `"data.json"` is fine. This cell uses a temp folder to avoid cluttering yours.

# %%
import json
import os
import tempfile

path = os.path.join(tempfile.gettempdir(), "ref_example.json")
students = [{"name": "Harry", "house": "Gryffindor"}, {"name": "Draco", "house": "Slytherin"}]

with open(path, "w") as file:                 # write
    json.dump(students, file, indent=2)

with open(path) as file:                      # read
    loaded = json.load(file)

loaded                                        # -> [{'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Draco', 'house': 'Slytherin'}]
loaded == students                            # -> True

# %% [markdown]
# ### JSON Lines: one JSON object per line
# Good for logs, or for adding records to a file one at a time.

# %%
import json
import os
import tempfile

path = os.path.join(tempfile.gettempdir(), "ref_example.jsonl")
with open(path, "w") as file:
    for record in [{"id": 1}, {"id": 2}]:
        file.write(json.dumps(record) + "\n")

with open(path) as file:
    records = [json.loads(line) for line in file]
records                                       # -> [{'id': 1}, {'id': 2}]


# %% [markdown]
# ## 5. Navigating nested JSON
# API responses are dicts and lists nested inside each other.
# Work **one level at a time**: print it, check `type()` and `.keys()`, then go one step deeper.
# The sample below has the same shape as the iTunes Search API response from CS50P Lecture 4.

# %%
data = {
    "resultCount": 2,
    "results": [
        {"artistName": "Weezer", "trackName": "Buddy Holly", "trackTimeMillis": 159000,
         "collection": {"name": "Weezer (Blue Album)", "year": 1994}},
        {"artistName": "Weezer", "trackName": "Say It Ain't So", "trackTimeMillis": 258000,
         "collection": {"name": "Weezer (Blue Album)", "year": 1994}},
    ],
}

type(data)                                    # -> <class 'dict'>
data.keys()                                   # -> dict_keys(['resultCount', 'results'])
type(data["results"])                         # -> <class 'list'>
data["results"][0].keys()                     # -> dict_keys(['artistName', 'trackName', 'trackTimeMillis', 'collection'])

data["results"][0]["trackName"]               # -> 'Buddy Holly'  # dict -> list -> dict
data["results"][0]["collection"]["year"]      # -> 1994  # one level deeper

for result in data["results"]:                # CS50P itunes2.py
    print(result["trackName"])
# -> Buddy Holly
# -> Say It Ain't So

# %% [markdown]
# ### Extract, reshape, and access missing fields safely

# %%
data = {
    "results": [
        {"trackName": "Buddy Holly", "trackTimeMillis": 159000, "collection": {"year": 1994}},
        {"trackName": "Undone", "collection": {}},                  # missing fields happen in real APIs
    ],
}
results = data["results"]

[r["trackName"] for r in results]                                   # -> ['Buddy Holly', 'Undone']
{r["trackName"]: r.get("trackTimeMillis", 0) // 1000 for r in results}   # -> {'Buddy Holly': 159, 'Undone': 0}  # name -> seconds

results[1].get("trackTimeMillis")                                   # -> None  # .get instead of KeyError
results[1].get("collection", {}).get("year", "unknown")             # -> 'unknown'  # safe two-level lookup
data.get("results", [])                                             # a missing list becomes [], so a for loop just doesn't run

for r in results:
    seconds = r.get("trackTimeMillis", 0) // 1000
    print(f"{r['trackName']:<12} {seconds // 60}:{seconds % 60:02}")
# -> Buddy Holly  2:39
# -> Undone       0:00


# %% [markdown]
# ## 6. JSON errors
# - `json.JSONDecodeError`: the text isn't valid JSON.
# - `TypeError`: the Python object can't be turned into JSON (for example a `set`, `datetime`, or custom object).

# %%
import json

try:
    json.loads("{'name': 'Harry'}")                 # single quotes aren't JSON
except json.JSONDecodeError as e:
    print("JSONDecodeError:", e.msg)              # -> JSONDecodeError: Expecting property name enclosed in double quotes

try:
    json.loads('{"a": 1,}')                         # trailing comma
except json.JSONDecodeError as e:
    print("JSONDecodeError:", e.msg)              # -> JSONDecodeError: Illegal trailing comma before end of object

try:
    json.dumps({"tags": {"a", "b"}})                # sets aren't JSON
except TypeError as e:
    print("TypeError:", e)                        # -> TypeError: Object of type set is not JSON serializable

json.dumps({"tags": sorted({"b", "a"})})           # -> '{"tags": ["a", "b"]}'  # fix: convert to a list first

import datetime
json.dumps({"when": datetime.date(2026, 9, 27)}, default=str)   # -> '{"when": "2026-09-27"}'  # default= converts anything unknown


# %% [markdown]
# ## 7. `requests.get` and the Response object
#
# | Attribute / method | What it is |
# |---|---|
# | `r.status_code` | `200`, `404`, ... |
# | `r.ok` | `True` if the status is below 400 |
# | `r.reason` | `'OK'`, `'Not Found'`, ... |
# | `r.json()` | body parsed as JSON → dict/list (raises if not JSON) |
# | `r.text` | body as a `str` |
# | `r.content` | body as `bytes` (images, files) |
# | `r.headers` | response headers (case-insensitive dict) |
# | `r.url` | final URL, including query string |
# | `r.raise_for_status()` | raises `HTTPError` on 4xx/5xx |

# %%
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
r.status_code                  # -> 200
r.ok                           # -> True
r.reason                       # -> 'OK'
r.url                          # -> 'https://jsonplaceholder.typicode.com/todos/1'
r.headers["content-type"]      # -> 'application/json; charset=utf-8'  # header names aren't case-sensitive
type(r.text)                   # -> <class 'str'>
type(r.json())                 # -> <class 'dict'>
r.json()["title"]              # -> 'delectus aut autem'


# %% [markdown]
# ## 8. Query parameters
# Pass a `params` dict instead of gluing strings together.
# `requests` handles the `?` and `&` and escapes spaces and special characters.
# `requests.Request(...).prepare().url` shows the final URL **without sending anything**.

# %%
import requests

url = "https://itunes.apple.com/search"
params = {"entity": "song", "limit": 1, "term": "the beatles"}

requests.Request("GET", url, params=params).prepare().url
# -> 'https://itunes.apple.com/search?entity=song&limit=1&term=the+beatles'

requests.Request("GET", url, params={"term": "rock & roll"}).prepare().url
# -> 'https://itunes.apple.com/search?term=rock+%26+roll'  # & escaped safely

requests.Request("GET", url, params={"id": [1, 2]}).prepare().url
# -> 'https://itunes.apple.com/search?id=1&id=2'  # a list repeats the key

# %% [markdown]
# ### Live check
# httpbin.org/get echoes back the parameters it received.

# %%
import requests

r = requests.get("https://httpbin.org/get", params={"term": "weezer", "limit": 1}, timeout=10)
r.json()["args"]               # -> {'limit': '1', 'term': 'weezer'}  # the server receives everything as strings


# %% [markdown]
# ## 9. Status codes and error handling
#
# | Code | Meaning | Typical cause |
# |---|---|---|
# | 200 | OK | success |
# | 201 | Created | successful POST |
# | 204 | No Content | success, empty body (often a DELETE) |
# | 400 | Bad Request | wrong/missing parameters |
# | 401 / 403 | Unauthorized / Forbidden | missing or bad API key |
# | 404 | Not Found | wrong URL or ID |
# | 429 | Too Many Requests | rate limited; slow down |
# | 500–599 | Server error | not your fault; retry later |
#
# `requests` does **not** raise an exception for 404 or 500 on its own. Check `r.ok` or call `r.raise_for_status()`.

# %%
import requests

r = requests.get("https://httpbin.org/status/404", timeout=10)
r.status_code                  # -> 404
r.ok                           # -> False
try:
    r.raise_for_status()
except requests.HTTPError as e:
    print("HTTPError:", e.response.status_code)   # -> HTTPError: 404

# %% [markdown]
# ### Network problems raise exceptions
# - `requests.Timeout`: the server took longer than `timeout` seconds.
# - `requests.ConnectionError`: DNS failure, no internet, refused connection.
# - `requests.RequestException` is the parent of all of these. Catch it for "anything went wrong".

# %%
import requests

try:
    requests.get("https://httpbin.org/delay/5", timeout=1)   # server waits 5s, we give up after 1s
except requests.Timeout:
    print("Timed out")                            # -> Timed out

try:
    requests.get("https://no-such-host.invalid", timeout=5)
except requests.ConnectionError:
    print("Could not connect")                    # -> Could not connect

issubclass(requests.Timeout, requests.RequestException)          # -> True
issubclass(requests.HTTPError, requests.RequestException)        # -> True

# %% [markdown]
# ### The safe-fetch pattern
# One function that returns data or `None`, handling every failure type in one place.
# Order matters: `requests.JSONDecodeError` is also a `RequestException`, so catch it **first**.
# Otherwise the general handler catches it.

# %%
import requests

def fetch_json(url, params=None):
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.JSONDecodeError:                   # body wasn't JSON (must come first)
        print("Response was not JSON")
    except requests.RequestException as e:            # network problem, timeout, or 4xx/5xx
        print(f"Request failed: {e.__class__.__name__}")
    return None

fetch_json("https://jsonplaceholder.typicode.com/todos/1")["id"]   # -> 1
fetch_json("https://httpbin.org/status/500")          # returns None
# -> Request failed: HTTPError
fetch_json("https://httpbin.org/html")                # returns None
# -> Response was not JSON


# %% [markdown]
# ## 10. Headers and API keys
# Headers carry extra information: who you are, what format you want, and your credentials.
# Most real APIs need a key. **Never put a key in your code.** Read it from an environment variable.
# In the terminal: `export WEATHER_API_KEY=abc123`

# %%
import os
import requests

api_key = os.environ.get("WEATHER_API_KEY", "demo-key")    # fallback only so this example runs

headers = {
    "User-Agent": "cs50p-notes/1.0",              # identify your program (some APIs require it)
    "Accept": "application/json",                 # ask for JSON
    "Authorization": f"Bearer {api_key}",         # the most common key style; check each API's docs
}
r = requests.get("https://httpbin.org/headers", headers=headers, timeout=10)
echoed = r.json()["headers"]
echoed["User-Agent"]                              # -> 'cs50p-notes/1.0'
echoed["Authorization"]                           # -> 'Bearer demo-key'

# Other APIs put the key in the query string instead:
requests.Request("GET", "https://api.example.com/weather", params={"q": "Boston", "appid": "demo-key"}).prepare().url
# -> 'https://api.example.com/weather?q=Boston&appid=demo-key'


# %% [markdown]
# ## 11. Sending data: POST / PUT / DELETE
#
# | Method | Purpose | `requests` call |
# |---|---|---|
# | GET | read | `requests.get(url, params=...)` |
# | POST | create | `requests.post(url, json=...)` |
# | PUT / PATCH | replace / update | `requests.put(url, json=...)` / `requests.patch(...)` |
# | DELETE | remove | `requests.delete(url)` |
#
# `json=dict` sends a JSON body and sets the `Content-Type` header for you.
# `data=dict` sends HTML-form-style data instead. Use `json=` unless the API docs say otherwise.

# %%
import requests

new_todo = {"title": "learn requests", "completed": False, "userId": 1}
r = requests.post("https://jsonplaceholder.typicode.com/todos", json=new_todo, timeout=10)
r.status_code                  # -> 201
r.json()                       # -> {'title': 'learn requests', 'completed': False, 'userId': 1, 'id': 201}  # server added an id

r = requests.patch("https://jsonplaceholder.typicode.com/todos/1", json={"completed": True}, timeout=10)
r.json()["completed"]          # -> True

r = requests.delete("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
r.status_code                  # -> 200

r = requests.post("https://httpbin.org/post", json={"a": 1}, timeout=10)     # see exactly what was sent
r.json()["json"]               # -> {'a': 1}
r.json()["headers"]["Content-Type"]   # -> 'application/json'


# %% [markdown]
# ## 12. Sessions
# A `Session` reuses the connection and remembers headers you set once.
# Use one when you make many calls to the same API.

# %%
import requests

with requests.Session() as session:
    session.headers.update({"User-Agent": "cs50p-notes/1.0"})
    todos = [session.get(f"https://jsonplaceholder.typicode.com/todos/{i}", timeout=10).json()["id"] for i in (1, 2, 3)]
todos                          # -> [1, 2, 3]


# %% [markdown]
# ## 13. Complete program pattern (CS50P `itunes.py`, improved)
# The Lecture 4 program, updated with `params=`, a timeout, error handling, and `.get()`.
# In a real script, `term` would come from `sys.argv[1]`.

# %%
import requests

def main():
    term = "weezer"
    for name in search_songs(term, limit=3):
        print(name)

def search_songs(term, limit=50):
    try:
        r = requests.get(
            "https://itunes.apple.com/search",
            params={"entity": "song", "limit": limit, "term": term},
            timeout=10,
        )
        r.raise_for_status()
    except requests.RequestException:
        return []
    return [result.get("trackName", "?") for result in r.json().get("results", [])]

main()
# e.g. Island In the Sun
# e.g. Say It Ain't So (2024 Remaster)
# e.g. Buddy Holly (2024 Remaster)

# %% [markdown]
# ### Cache a response to a file and work offline
# Fetch once, save it, then develop against the saved file. That's faster, and it doesn't hit rate limits.

# %%
import json
import os
import tempfile
import requests

path = os.path.join(tempfile.gettempdir(), "todo_cache.json")
if os.path.exists(path):
    with open(path) as file:
        todo = json.load(file)
else:
    todo = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10).json()
    with open(path, "w") as file:
        json.dump(todo, file)
todo["title"]                  # -> 'delectus aut autem'


# %% [markdown]
# ## 14. Pitfalls

# %% [markdown]
# ### Forgetting `()` on `.json()`, or printing the Response itself

# %%
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
print(r)                                  # -> <Response [200]>  # the object, not the data
type(r.json)                              # -> <class 'method'>  # missing ()
type(r.json())                            # -> <class 'dict'>

# %% [markdown]
# ### A 404 or 500 doesn't raise on its own
# Without a check, you end up parsing an error page. Call `raise_for_status()` or check `r.ok` first.

# %%
import requests

r = requests.get("https://httpbin.org/status/500", timeout=10)
r.ok                                      # -> False
r.text                                    # -> ''  # nothing useful to parse

# %% [markdown]
# ### `.json()` on a response that isn't JSON
# HTML error pages, empty bodies, and rate-limit messages all raise `requests.JSONDecodeError`, which is a kind of `ValueError`.

# %%
import requests

r = requests.get("https://httpbin.org/html", timeout=10)
r.headers["Content-Type"]                 # -> 'text/html; charset=utf-8'
try:
    r.json()
except requests.JSONDecodeError:
    print("not JSON")                     # -> not JSON

# %% [markdown]
# ### Building URLs with `+` breaks on special characters
# CS50P's `itunes.py` builds the URL with `+`, which works for simple words.
# An `&` in the search term splits it into two parameters. `params=` escapes it.

# %%
from urllib.parse import parse_qs, urlsplit
import requests

term = "rock & roll"
glued = requests.Request("GET", "https://itunes.apple.com/search?term=" + term).prepare().url
safe = requests.Request("GET", "https://itunes.apple.com/search", params={"term": term}).prepare().url

parse_qs(urlsplit(glued).query)           # -> {'term': ['rock ']}  # the server only sees "rock "
parse_qs(urlsplit(safe).query)            # -> {'term': ['rock & roll']}

# %% [markdown]
# ### No timeout means it can hang forever
# `requests` waits indefinitely by default. Always pass `timeout=`.

# %% [markdown]
# ### A printed dict isn't JSON
# `print(data)` shows Python syntax: single quotes, `True`, `None`.
# Use `json.dumps` when you need real JSON, for example to save it or send it.

# %%
import json

data = {"ok": True, "value": None}
str(data)                                 # -> "{'ok': True, 'value': None}"  # Python, NOT JSON
json.dumps(data)                          # -> '{"ok": true, "value": null}'

# %% [markdown]
# ### Everything in a URL is a string
# Parameters arrive as strings, and some APIs send numbers as strings too. Convert before doing math.

# %%
data = {"price": "19.99", "qty": "3"}
float(data["price"]) * int(data["qty"])   # -> 59.97

# %% [markdown]
# ### Keys are case-sensitive and must match exactly
# Copy key names from a pretty-printed response rather than guessing.
# `trackname` and `trackName` are different keys.

# %%
result = {"trackName": "Buddy Holly"}
result.get("trackname")                   # -> None
result.get("trackName")                   # -> 'Buddy Holly'
