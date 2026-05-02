# ─────────────────────────────────────────────────────────────────────────────
# TECH  — all reference content (migrated from the original JS TECH object)
# JOURNEY_STEPS — the beginner SOP flow
# ─────────────────────────────────────────────────────────────────────────────

TECH = {

# ═══════════════ PYTHON ═══════════════
"python": {
  "label": "Python", "emoji": "🐍", "color": "var(--py)", "bg": "var(--py-bg)",
  "intro": "The language that runs your server, processes your data, and talks to AI. Readable like English. Powerful like a pro.",
  "analogy": "🍳 Like a recipe: ingredients (data) + steps (logic) = dish (result). Python is the chef following your recipe.",
  "topics": [
    { "id": "py-datatypes", "emoji": "📦", "name": "Data Types", "sub": "9 containers for every kind of data",
      "sections": [
        {"t": "intro", "c": "A data type tells Python what kind of thing a variable holds — and what you can DO with it. A number and a word are different kinds of things; Python needs to know which."},
        {"t": "heading", "c": "The 9 Core Types"},
        {"t": "types", "items": [
          {"name": "int",   "eg": "age = 25",         "color": "#DBEAFE", "border": "#3B82F6", "when": "Whole numbers. Counting, IDs, indexes."},
          {"name": "float", "eg": "price = 9.99",      "color": "#EDE9FE", "border": "#8B5CF6", "when": "Decimal numbers. Money, percentages, measurements."},
          {"name": "str",   "eg": 'name = "Alice"',    "color": "#FEF3C7", "border": "#F59E0B", "when": "Text. Any sequence of characters."},
          {"name": "bool",  "eg": "is_active = True",  "color": "#DCFCE7", "border": "#22C55E", "when": "True or False only. Switches, flags, conditions."},
          {"name": "None",  "eg": "result = None",     "color": "#F3F4F6", "border": "#9CA3AF", "when": "Nothing / empty / not yet set. Like NULL in SQL."},
          {"name": "list",  "eg": "[1, 2, 3]",         "color": "#FEE2E2", "border": "#EF4444", "when": "Ordered collection. Can change. Items can repeat."},
          {"name": "dict",  "eg": '{"name":"Ali"}',    "color": "#FDF4FF", "border": "#D946EF", "when": "Key-value pairs. Like a labelled box for each thing."},
          {"name": "tuple", "eg": "(10, 20)",           "color": "#FFF7ED", "border": "#F97316", "when": "Ordered, CANNOT change. Use for fixed data (coordinates, RGB)."},
          {"name": "set",   "eg": "{1, 2, 3}",         "color": "#ECFDF5", "border": "#10B981", "when": "Unique values only. Duplicates auto-removed. Membership checks."},
        ]},
        {"t": "code", "c": """# Check any variable's type
type(42)          # <class 'int'>
type("hello")     # <class 'str'>
type([1,2,3])     # <class 'list'>

# Convert between types
int("42")         # → 42  (string to int)
str(42)           # → "42"  (int to string)
float("3.14")     # → 3.14
list((1,2,3))     # → [1, 2, 3]  (tuple to list)

# Mutable vs Immutable
# Mutable  (can change): list, dict, set
# Immutable (frozen):    int, float, str, bool, tuple"""},
        {"t": "rule", "q": "When should I use a list vs a tuple?", "a": "List = things that might change (cart items, search results). Tuple = things that never change (a coordinate pair, an RGB colour, database row returned from a query you don't want modified)."},
        {"t": "rule", "q": "When should I use a dict vs a list?", "a": "List = ordered sequence where position matters. Dict = labelled data where you access by NAME not position. User profile = dict. Leaderboard = list."},
        {"t": "ai", "items": [
          '"Create a Python dict called user with keys: name, email, age, is_active"',
          '"Convert this list of strings to integers using a list comprehension"',
          '"Add type hints to this function using Python\'s typing module"',
          '"Check if a key exists in a dict before accessing it"',
        ]},
      ]
    },

    { "id": "py-variables", "emoji": "🏷️", "name": "Variables", "sub": "Naming and storing values",
      "sections": [
        {"t": "intro", "c": "A variable is just a label you stick on a piece of data. Python figures out the type automatically — you just write the name, equals, and the value."},
        {"t": "heading", "c": "Naming Rules"},
        {"t": "p", "c": "Python uses snake_case (words separated by underscores). Be descriptive — code is read more than it's written."},
        {"t": "code", "c": """# ✓ Good names
user_name = "Alice"
total_price = 99.99
is_logged_in = True
MAX_FILE_SIZE = 10          # CAPS = constant (won't change)

# ✗ Bad names
x = "Alice"                 # too short
TotalPrice = 99.99          # that's JavaScript style
totalprice = 99.99          # hard to read

# Multiple assignment
a, b, c = 1, 2, 3          # a=1, b=2, c=3
x = y = 0                   # both start at 0

# Swap two values (Python magic)
a, b = b, a"""},
        {"t": "heading", "c": "Scope — Where a Variable Lives"},
        {"t": "p", "c": "Scope determines WHERE a variable can be seen. This is the #1 source of NameError bugs."},
        {"t": "code", "c": """count = 10              # Global — visible everywhere

def my_function():
    name = "Alice"      # Local — only inside this function
    print(count)        # ✓ Can READ globals
    # count = count + 1 # ✗ Can't MODIFY globals without 'global'

def fix_count():
    global count        # Declare you want the global one
    count = count + 1   # ✓ Now this works"""},
        {"t": "rule", "q": "When should I use a global variable?", "a": "Almost never. Global variables make code hard to debug because anything anywhere can change them. Pass values as function arguments instead. Reserve globals for TRUE constants (MAX_SIZE, APP_NAME)."},
        {"t": "ai", "items": [
          '"Refactor this function to accept parameters instead of using global variables"',
          '"What is the scope of variable X in this code block?"',
          '"Create constants for all magic numbers in this file"',
        ]},
      ]
    },

    { "id": "py-strings", "emoji": "📝", "name": "Strings", "sub": "Working with text",
      "sections": [
        {"t": "intro", "c": "Strings hold text. In Python, strings are immutable — you can't change a character in place, you create a new string. They have dozens of built-in methods."},
        {"t": "code", "c": r"""# Creating strings
name = "Alice"
message = 'She said "hello"'   # Single quotes if text has "
multiline = '''
Line one
Line two
'''

# f-strings — the best way to embed variables (Python 3.6+)
age = 30
price = 9.99
greeting = f"Hello, {name}! You are {age} years old."
price_str = f"Total: ${price:.2f}"   # :.2f = 2 decimal places

# Essential string methods
"  hello  ".strip()        # "hello"  (remove whitespace)
"hello".upper()            # "HELLO"
"HELLO".lower()            # "hello"
"hello world".split()      # ["hello", "world"]
" ".join(["a","b","c"])    # "a b c"
"hello".replace("l","r")   # "herro"
"hello world".startswith("hello")  # True
"hello".find("ll")         # 2  (index) or -1 if not found
len("hello")               # 5"""},
        {"t": "heading", "c": "String Slicing"},
        {"t": "code", "c": """text = "Hello World"
text[0]        # "H"   (first character)
text[-1]       # "d"   (last character)
text[0:5]      # "Hello"  (start:stop, stop not included)
text[6:]       # "World"  (from index 6 to end)
text[:5]       # "Hello"  (from start to index 5)
text[::-1]     # "dlroW olleH"  (reversed)"""},
        {"t": "ai", "items": [
          '"Format this list of prices as strings with 2 decimal places using f-strings"',
          '"Extract the domain from a list of email addresses using string split"',
          '"Clean a list of user inputs: strip whitespace, lowercase, remove special chars"',
        ]},
      ]
    },

    { "id": "py-lists", "emoji": "📋", "name": "Lists", "sub": "Ordered collections — your most-used type",
      "sections": [
        {"t": "intro", "c": "Lists are the workhorses of Python. An ordered sequence of anything — numbers, strings, dicts, even other lists. The most common data structure you'll use daily."},
        {"t": "code", "c": """# Create
fruits = ["apple", "banana", "cherry"]
mixed  = [1, "hello", True, None]   # can mix types
empty  = []

# Access by index (zero-based)
fruits[0]         # "apple"  (first)
fruits[-1]        # "cherry" (last)
fruits[1:3]       # ["banana","cherry"] (slice)

# Modify
fruits.append("date")          # add to end
fruits.insert(1, "avocado")    # insert at position
fruits.pop()                   # remove and return last
fruits.pop(0)                  # remove and return index 0
fruits.remove("banana")        # remove by value
fruits[0] = "mango"            # replace in place

# Query
len(fruits)                    # number of items
"apple" in fruits              # True or False
fruits.index("cherry")         # 2
fruits.count("apple")          # how many times

# Sort
fruits.sort()                  # sort in place A→Z
fruits.sort(reverse=True)      # Z→A
sorted(fruits)                 # returns NEW sorted list"""},
        {"t": "heading", "c": "List Comprehensions — The Python Superpower"},
        {"t": "p", "c": "A compact way to build a list from another list. Replaces a 3-line for loop with one line."},
        {"t": "code", "c": """numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Old way
squares = []
for n in numbers:
    squares.append(n * n)

# List comprehension (same result, one line)
squares = [n * n for n in numbers]

# With filter (only even numbers)
evens = [n for n in numbers if n % 2 == 0]

# Transform a list of dicts
names = [user["name"] for user in users]
prices_with_tax = [p * 1.2 for p in prices]"""},
        {"t": "ai", "items": [
          '"Convert this for-loop that builds a list into a list comprehension"',
          '"Filter this list of dicts to only include rows where status is active"',
          '"Flatten this list of lists into a single list"',
          '"Sort this list of dicts by the price key, descending"',
        ]},
      ]
    },

    { "id": "py-dicts", "emoji": "🗂️", "name": "Dictionaries", "sub": "Key-value pairs — like a labelled filing cabinet",
      "sections": [
        {"t": "intro", "c": "Dicts store data by name rather than position. Perfect for structured records — a user, a product, a config setting, an API response."},
        {"t": "code", "c": """# Create
user = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "is_active": True
}

# Access
user["name"]              # "Alice"  (KeyError if missing)
user.get("name")          # "Alice"  (None if missing — safer)
user.get("phone", "N/A")  # "N/A"   (default if missing)

# Modify
user["age"] = 31          # update
user["phone"] = "555-1234"  # add new key
del user["phone"]         # delete key

# Check
"email" in user           # True
"phone" in user           # False

# Loop
for key in user:                     # loop keys
    print(key, user[key])
for key, value in user.items():      # loop both
    print(f"{key}: {value}")
user.keys()    # all keys
user.values()  # all values

# Merge two dicts (Python 3.9+)
defaults = {"color": "blue", "size": "M"}
overrides = {"size": "L", "brand": "Nike"}
merged = defaults | overrides    # {"color":"blue","size":"L","brand":"Nike"}"""},
        {"t": "heading", "c": "Nested Dicts — Dicts inside Dicts"},
        {"t": "code", "c": """product = {
    "name": "Laptop",
    "price": 999.99,
    "specs": {
        "ram": "16GB",
        "storage": "512GB"
    },
    "tags": ["electronics", "computers"]
}

# Access nested
product["specs"]["ram"]    # "16GB"
product["tags"][0]         # "electronics\""""},
        {"t": "ai", "items": [
          '"Convert this list of tuples into a dict where first item is key, second is value"',
          '"Group this list of orders by customer_id using a dict"',
          '"Merge these two dicts, with the second taking priority on duplicate keys"',
          '"Extract just these 3 keys from a large dict"',
        ]},
      ]
    },

    { "id": "py-functions", "emoji": "⚙️", "name": "Functions", "sub": "Reusable blocks of logic",
      "sections": [
        {"t": "intro", "c": "A function is a named block of code you can run by calling its name. Write once, use anywhere. The fundamental unit of reusable code."},
        {"t": "code", "c": r"""# Basic function
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")    # "Hello, Alice!"

# Default parameters (used if caller doesn't provide)
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")             # "Hello, Alice!"
greet("Alice", "Hi")       # "Hi, Alice!" """},
        {"t": "heading", "c": "Types of Parameters"},
        {"t": "code", "c": r"""# Positional — order matters
def add(a, b):
    return a + b
add(3, 4)                  # 7

# Keyword — name matters, order doesn't
def create_user(name, age, email):
    return {"name": name, "age": age, "email": email}
create_user(age=30, email="a@b.com", name="Alice")  # order doesn't matter

# *args — accept any number of positional arguments
def total(*numbers):
    return sum(numbers)
total(1, 2, 3, 4, 5)      # 15

# **kwargs — accept any number of keyword arguments (becomes a dict)
def log_event(**details):
    for key, val in details.items():
        print(f"{key}: {val}")
log_event(user="Alice", action="login", ip="1.2.3.4")"""},
        {"t": "heading", "c": "Return Values"},
        {"t": "code", "c": r"""# Return nothing (returns None implicitly)
def log(message):
    print(message)

# Return one value
def square(n):
    return n * n

# Return multiple values (actually returns a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([3,1,4,1,5,9])   # lo=1, hi=9"""},
        {"t": "heading", "c": "Lambda — One-line throwaway functions"},
        {"t": "code", "c": r"""# Lambda: lambda parameters: expression
double = lambda x: x * 2
double(5)    # 10

# Most useful for sorting
users = [{"name":"Charlie","age":30},{"name":"Alice","age":25}]
users.sort(key=lambda u: u["age"])   # sort by age
users.sort(key=lambda u: u["name"])  # sort by name"""},
        {"t": "heading", "c": "Type Hints — Tell AI (and humans) what goes in/out"},
        {"t": "code", "c": r"""# Type hints make your code self-documenting
def get_user(user_id: int) -> dict:
    ...

def process_names(names: list[str]) -> list[str]:
    return [name.upper() for name in names]

def send_email(to: str, subject: str, body: str) -> bool:
    ..."""},
        {"t": "rule", "q": "When should I make something a function?", "a": "If you write the same code twice → make it a function. If a block of code has one clear job (one name you can give it) → make it a function. If a function is longer than 20-30 lines → split it into smaller functions."},
        {"t": "ai", "items": [
          '"Extract this repeated logic into a reusable function with type hints"',
          '"Add docstrings to all functions in this file"',
          '"Refactor this function: it does too many things, split it into 3 smaller functions"',
          '"Convert these **kwargs into explicit typed parameters"',
        ]},
      ]
    },

    { "id": "py-classes", "emoji": "🏗️", "name": "Classes", "sub": "Templates for creating objects",
      "sections": [
        {"t": "intro", "c": "A class is a blueprint. It defines what properties (data) and behaviours (methods) a thing has. An object is one instance built from that blueprint."},
        {"t": "p", "c": "Think of a class as a cookie cutter and objects as the cookies. The cutter defines the shape; each cookie is a separate thing with the same shape."},
        {"t": "code", "c": r"""class User:
    # __init__ runs when you create a new User
    def __init__(self, name: str, email: str, age: int):
        self.name = name      # self.X = instance variable
        self.email = email
        self.age = age
        self.is_active = True  # default value

    # Method: a function belonging to the class
    def greet(self) -> str:
        return f"Hi, I'm {self.name}"

    def deactivate(self):
        self.is_active = False

    # __repr__: what prints when you print(user)
    def __repr__(self) -> str:
        return f"User({self.name}, {self.email})"

# Create instances (objects)
alice = User("Alice", "alice@example.com", 30)
bob   = User("Bob",   "bob@example.com",   25)

alice.name          # "Alice"
alice.greet()       # "Hi, I'm Alice"
alice.deactivate()
alice.is_active     # False
bob.is_active       # True — bob is unaffected"""},
        {"t": "heading", "c": "Inheritance — Build on an existing class"},
        {"t": "code", "c": r"""class AdminUser(User):       # AdminUser inherits from User
    def __init__(self, name, email, age, permissions):
        super().__init__(name, email, age)   # call parent __init__
        self.permissions = permissions

    def grant_access(self, resource):
        print(f"{self.name} granted access to {resource}")

admin = AdminUser("Carol","carol@example.com",35,["delete","ban"])
admin.greet()         # ✓ inherited from User
admin.grant_access("database")  # ✓ new method"""},
        {"t": "rule", "q": "When do I use a class vs just a function?", "a": "Use a function when you have a single job to do. Use a class when you have DATA + BEHAVIOUR that belong together, and you'll create multiple instances of the same thing. A User with properties and methods = class. A function that formats a date = just a function."},
        {"t": "ai", "items": [
          '"Create a class called Product with these fields and methods: ..."',
          '"Add a class method that creates an instance from a dict"',
          '"Add a property decorator so price is always rounded to 2 decimals"',
          '"Convert these related functions into a class"',
        ]},
      ]
    },

    { "id": "py-errors", "emoji": "🛡️", "name": "Error Handling", "sub": "Catching things that go wrong",
      "sections": [
        {"t": "intro", "c": "Errors happen. A file is missing, a user sends bad data, the network drops. try/except lets your program handle errors gracefully instead of crashing."},
        {"t": "code", "c": """# Basic
try:
    result = 10 / 0
except ZeroDivisionError:
    result = 0

# Multiple except
try:
    data = json.loads(user_input)
    value = data["key"]
except json.JSONDecodeError:
    print("Invalid JSON")
except KeyError:
    print("Key not found")
except Exception as e:           # catch-all
    print(f"Unexpected error: {e}")
finally:
    print("This always runs")"""},
        {"t": "heading", "c": "Common Exception Types"},
        {"t": "table", "heads": ["Exception", "When it happens", "Example"],
          "rows": [
            ["ValueError", "Wrong type of value", 'int("abc")'],
            ["KeyError", "Dict key doesn't exist", 'd["missing"]'],
            ["IndexError", "List index out of range", "[1,2,3][9]"],
            ["TypeError", "Wrong type for operation", '"a" + 1'],
            ["AttributeError", "Object has no such attribute", "None.strip()"],
            ["FileNotFoundError", "File doesn't exist", 'open("x.txt")'],
            ["ZeroDivisionError", "Divide by zero", "10 / 0"],
            ["PermissionError", "No access to file/resource", 'open("/etc/shadow")'],
          ]
        },
        {"t": "tip", "c": "✓ Catch SPECIFIC exceptions, not just Exception. This way you handle each error differently and don't accidentally swallow bugs you didn't expect."},
        {"t": "ai", "items": [
          '"Wrap this function in try/except and return None on failure, log the error"',
          '"Add specific exception handling for FileNotFoundError and JSONDecodeError"',
          '"Create a custom exception class for invalid user input"',
        ]},
      ]
    },

    { "id": "py-flask", "emoji": "🌐", "name": "Flask Patterns", "sub": "The web framework your app runs on",
      "sections": [
        {"t": "intro", "c": "Flask turns your Python into a web server. You define routes (URLs) and what Python code to run when someone visits them. Your whole app.py is built on this."},
        {"t": "code", "c": """from flask import Flask, request, jsonify, session

app = Flask(__name__)

# GET route — return data
@app.route("/users")
def list_users():
    users = get_all_users()        # your function
    return jsonify({"users": users})

# POST route — receive data
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json            # body as dict
    name = data.get("name")
    if not name:
        return jsonify({"error": "name required"}), 400
    user = create(name)
    return jsonify({"user": user}), 201

# URL parameter
@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "not found"}), 404
    return jsonify(user)

# Query string  /search?q=alice&limit=10
@app.route("/search")
def search():
    q     = request.args.get("q", "")
    limit = int(request.args.get("limit", 10))
    ..."""},
        {"t": "heading", "c": "HTTP Status Codes You Must Know"},
        {"t": "table", "heads": ["Code", "Meaning", "When to use"],
          "rows": [
            ["200", "OK", "Successful GET or PUT"],
            ["201", "Created", "Successful POST (new resource created)"],
            ["400", "Bad Request", "Client sent invalid data"],
            ["401", "Unauthorized", "Not logged in"],
            ["403", "Forbidden", "Logged in but not allowed"],
            ["404", "Not Found", "Resource doesn't exist"],
            ["422", "Unprocessable", "Data format valid but content wrong"],
            ["500", "Server Error", "Something crashed on your end"],
          ]
        },
        {"t": "ai", "items": [
          '"Add a Flask route /api/products that accepts GET with optional ?category= filter"',
          '"Add input validation to this Flask POST route and return 400 if required fields missing"',
          '"Convert this Flask route to return paginated results with page and per_page query params"',
        ]},
      ]
    },

    { "id": "py-modules", "emoji": "📦", "name": "Modules & Imports", "sub": "Using and organising code across files",
      "sections": [
        {"t": "intro", "c": "A module is any Python file. An import lets you use code from another file or package. Python comes with a huge standard library — use it before installing anything."},
        {"t": "code", "c": """# Import whole module
import os
import json
import datetime

os.path.exists("file.txt")      # check if file exists
json.dumps({"key": "val"})      # dict → JSON string
json.loads('{"key":"val"}')     # JSON string → dict

# Import specific things
from datetime import datetime, timedelta
from pathlib import Path

now = datetime.now()
tomorrow = now + timedelta(days=1)
p = Path("uploads") / "file.csv"   # cross-platform paths"""},
        {"t": "heading", "c": "Standard Library — Use These Before pip install"},
        {"t": "table", "heads": ["Module", "What it does", "Common use"],
          "rows": [
            ["os", "Operating system interface", "File paths, env vars, directory listing"],
            ["json", "JSON encode/decode", "API responses, config files"],
            ["datetime", "Dates and times", "Timestamps, date arithmetic"],
            ["pathlib", "Modern file paths", "Building paths safely (cross-platform)"],
            ["re", "Regular expressions", "Pattern matching in strings"],
            ["collections", "Special data structures", "Counter, defaultdict, deque"],
            ["csv", "Read/write CSV files", "Data files without pandas"],
            ["uuid", "Generate unique IDs", "Creating unique identifiers"],
            ["hashlib", "Hashing (SHA256 etc)", "Password hashing, checksums"],
            ["logging", "Structured logging", "Replace print() in production"],
          ]
        },
        {"t": "ai", "items": [
          '"Replace os.path with pathlib.Path in this function"',
          '"Add logging to this module using Python\'s logging library at INFO level"',
          '"Read this CSV file into a list of dicts using the csv module"',
        ]},
      ]
    },
  ]
},

# ═══════════════ SQL ═══════════════
"sql": {
  "label": "SQL", "emoji": "🗄️", "color": "var(--sql)", "bg": "var(--sql-bg)",
  "intro": "The language that reads, writes, and shapes data in a database. Every real web app uses SQL.",
  "analogy": "📊 Like a very powerful spreadsheet with superpowers. You ask questions; the database returns answers.",
  "topics": [
    { "id": "sql-datatypes", "emoji": "📦", "name": "Data Types", "sub": "What type of data goes in each column",
      "sections": [
        {"t": "intro", "c": "When you create a table, every column needs a type. The database uses the type to store data efficiently and to stop you storing wrong data in the wrong place."},
        {"t": "table", "heads": ["Type", "What it stores", "Example"],
          "rows": [
            ["INTEGER", "Whole numbers", "id, age, quantity, count"],
            ["REAL / FLOAT", "Decimal numbers", "price (9.99), latitude"],
            ["TEXT / VARCHAR", "Text of any length", "name, email, address"],
            ["VARCHAR(n)", "Text up to n characters", "username VARCHAR(50)"],
            ["BOOLEAN", "True / False (0 or 1 in SQLite)", "is_active, is_verified"],
            ["DATE", "A calendar date", "birth_date (2000-01-15)"],
            ["DATETIME / TIMESTAMP", "Date + time", "created_at, updated_at"],
            ["JSON", "Flexible key-value blob", "settings, metadata, tags"],
            ["BLOB", "Binary data", "files, images (usually use file paths instead)"],
          ]
        },
        {"t": "rule", "q": "Should I store money as FLOAT or INTEGER?", "a": "NEVER float — floating point arithmetic has rounding errors. Store as INTEGER cents (999 = $9.99) or use NUMERIC/DECIMAL if your database supports it."},
        {"t": "ai", "items": [
          '"Design a table for storing blog posts with appropriate column types"',
          '"What data type should I use for storing a phone number in SQL?"',
          '"Add a created_at and updated_at column with automatic timestamps"',
        ]},
      ]
    },

    { "id": "sql-create", "emoji": "🏗️", "name": "CREATE TABLE", "sub": "Building the structure of your data",
      "sections": [
        {"t": "intro", "c": "Before you store anything, you need to define the shape of the data. CREATE TABLE is the blueprint of a database table."},
        {"t": "code", "c": """CREATE TABLE users (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    name      TEXT    NOT NULL,
    email     TEXT    NOT NULL UNIQUE,
    age       INTEGER,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    INTEGER NOT NULL,
    title      TEXT    NOT NULL,
    body       TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);"""},
        {"t": "heading", "c": "Constraints — Rules the Database Enforces"},
        {"t": "table", "heads": ["Constraint", "What it does"],
          "rows": [
            ["PRIMARY KEY", "Uniquely identifies each row. Auto-increments if AUTOINCREMENT added."],
            ["NOT NULL", "Column cannot be empty. Database rejects the row if missing."],
            ["UNIQUE", "No two rows can have the same value in this column."],
            ["DEFAULT value", "Used when you don't provide a value on insert."],
            ["FOREIGN KEY", "Links to a row in another table. Enforces relationships."],
            ["CHECK(...)", "Custom rule, e.g. CHECK(age >= 0)"],
          ]
        },
        {"t": "ai", "items": [
          '"Create a SQL table for storing orders with user reference, total, and status"',
          '"Add a CHECK constraint so status can only be pending, paid, or cancelled"',
          '"Write ALTER TABLE to add a phone column to an existing users table"',
        ]},
      ]
    },

    { "id": "sql-select", "emoji": "🔍", "name": "SELECT & Filtering", "sub": "Reading data — the most important query",
      "sections": [
        {"t": "intro", "c": "SELECT is how you ask the database a question. It returns rows. Every dashboard, every list, every search result starts with SELECT."},
        {"t": "code", "c": """-- All columns, all rows
SELECT * FROM users;

-- Specific columns
SELECT name, email FROM users;

-- Filter with WHERE
SELECT * FROM users WHERE is_active = TRUE;
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE name = 'Alice';

-- Multiple conditions
SELECT * FROM users WHERE age > 25 AND is_active = TRUE;
SELECT * FROM users WHERE city = 'London' OR city = 'Paris';
SELECT * FROM users WHERE city IN ('London', 'Paris', 'Berlin');
SELECT * FROM users WHERE email LIKE '%@gmail.com';  -- wildcard

-- Sort
SELECT * FROM users ORDER BY name ASC;       -- A → Z
SELECT * FROM users ORDER BY created_at DESC; -- newest first

-- Limit results (pagination)
SELECT * FROM users LIMIT 10;               -- first 10
SELECT * FROM users LIMIT 10 OFFSET 20;     -- rows 21-30

-- Unique values
SELECT DISTINCT city FROM users;"""},
        {"t": "heading", "c": "NULL — The Tricky One"},
        {"t": "code", "c": """-- NULL means "no value". Don't use = NULL, use IS NULL
SELECT * FROM users WHERE phone IS NULL;
SELECT * FROM users WHERE phone IS NOT NULL;

-- COALESCE returns first non-null value
SELECT name, COALESCE(phone, 'No phone') AS phone FROM users;"""},
        {"t": "ai", "items": [
          '"Write a SELECT query to find all orders placed in the last 30 days"',
          '"Add pagination to this query using LIMIT and OFFSET based on page number"',
          '"Write a query to search users by name using a case-insensitive LIKE"',
        ]},
      ]
    },

    { "id": "sql-write", "emoji": "✏️", "name": "INSERT / UPDATE / DELETE", "sub": "Writing and changing data",
      "sections": [
        {"t": "intro", "c": "Three operations that change data. INSERT adds rows. UPDATE changes existing rows. DELETE removes rows. Always use WHERE on UPDATE and DELETE."},
        {"t": "code", "c": """-- INSERT: add a new row
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@example.com', 30);

-- INSERT multiple rows
INSERT INTO users (name, email) VALUES
    ('Bob',   'bob@example.com'),
    ('Carol', 'carol@example.com');

-- UPDATE: change existing rows
UPDATE users
SET age = 31, updated_at = CURRENT_TIMESTAMP
WHERE id = 1;

UPDATE users
SET is_active = FALSE
WHERE last_login < '2024-01-01';

-- DELETE: remove rows
DELETE FROM users WHERE id = 5;
DELETE FROM users WHERE is_active = FALSE;"""},
        {"t": "warn", "c": "⚠️ ALWAYS include WHERE on UPDATE and DELETE — without it, you modify or delete EVERY ROW in the table. Test your WHERE clause with a SELECT first."},
        {"t": "code", "c": """-- UPSERT: insert if not exists, update if it does (SQLite)
INSERT INTO settings (key, value)
VALUES ('theme', 'dark')
ON CONFLICT(key) DO UPDATE SET value = excluded.value;"""},
        {"t": "ai", "items": [
          '"Write an upsert for this table where email is the unique key"',
          '"Write a soft-delete UPDATE that sets deleted_at instead of removing the row"',
          '"Write a parameterised INSERT in Python using sqlite3 or psycopg2"',
        ]},
      ]
    },

    { "id": "sql-joins", "emoji": "🔗", "name": "JOINs", "sub": "Combining data from multiple tables",
      "sections": [
        {"t": "intro", "c": "A JOIN combines rows from two tables based on a matching column. This is the relational part of \"relational database\" — data lives in separate tables and JOINs bring it together."},
        {"t": "code", "c": """-- INNER JOIN: only rows that match in BOTH tables
SELECT users.name, posts.title
FROM posts
INNER JOIN users ON posts.user_id = users.id;

-- LEFT JOIN: all rows from left table, matching from right (NULL if no match)
SELECT users.name, posts.title
FROM users
LEFT JOIN posts ON posts.user_id = users.id;
-- Returns ALL users, even those with no posts (posts.title will be NULL)

-- Aliases make it readable
SELECT u.name, p.title, p.created_at
FROM posts p
JOIN users u ON p.user_id = u.id
WHERE u.is_active = TRUE
ORDER BY p.created_at DESC;"""},
        {"t": "rule", "q": "INNER vs LEFT JOIN — which to use?", "a": "INNER JOIN = you only want rows where a match exists in BOTH tables. LEFT JOIN = you want ALL rows from the first table, whether or not there's a match. Use LEFT when the relationship is optional (user might have no posts)."},
        {"t": "ai", "items": [
          '"Write a query joining orders to customers and products to show order history"',
          '"Add a LEFT JOIN to include users who have never placed an order"',
          '"Rewrite this query with table aliases to make it shorter"',
        ]},
      ]
    },

    { "id": "sql-agg", "emoji": "📊", "name": "Aggregates & GROUP BY", "sub": "Counting, summing, averaging",
      "sections": [
        {"t": "intro", "c": "Aggregate functions crunch many rows into one number. COUNT, SUM, AVG, MIN, MAX. GROUP BY splits the data into groups before aggregating."},
        {"t": "code", "c": """-- Aggregate the whole table
SELECT COUNT(*) AS total_users FROM users;
SELECT AVG(age) AS avg_age FROM users;
SELECT MIN(price), MAX(price) FROM products;
SELECT SUM(amount) AS total_revenue FROM orders;

-- GROUP BY: aggregate PER GROUP
SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city
ORDER BY user_count DESC;

SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category;

-- HAVING: filter AFTER grouping (WHERE filters before)
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 5;    -- only users with more than 5 orders"""},
        {"t": "rule", "q": "WHERE vs HAVING — what's the difference?", "a": "WHERE filters rows BEFORE grouping. HAVING filters groups AFTER. You can't use WHERE on aggregate results (COUNT, SUM etc.) — use HAVING for that."},
        {"t": "ai", "items": [
          '"Write a query to show monthly revenue totals for the past year"',
          '"Count orders per status (pending, paid, cancelled) in one query"',
          '"Find the top 10 customers by total spend"',
        ]},
      ]
    },
  ]
},

# ═══════════════ HTML ═══════════════
"html": {
  "label": "HTML", "emoji": "🟧", "color": "var(--html)", "bg": "var(--html-bg)",
  "intro": "The skeleton of every web page. HTML defines what exists — structure, not appearance.",
  "analogy": "🏠 HTML is the walls, floors, and rooms of a house. CSS paints them. JS installs the lights and lifts.",
  "topics": [
    { "id": "html-structure", "emoji": "🦴", "name": "Document Structure", "sub": "The required skeleton every page needs",
      "sections": [
        {"t": "intro", "c": "Every HTML file must have this structure. The browser won't crash without it, but it will guess — and guess wrong."},
        {"t": "code", "c": """<!DOCTYPE html>          <!-- tells browser: this is HTML5 -->
<html lang="en">         <!-- root element, lang helps screen readers -->
  <head>                 <!-- metadata — not visible on page -->
    <meta charset="UTF-8">              <!-- handle all characters -->
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0"> <!-- mobile! -->
    <title>My App</title>              <!-- browser tab title -->
    <link rel="stylesheet" href="style.css">
  </head>
  <body>                 <!-- everything visible goes here -->
    <h1>Hello World</h1>
    <script src="app.js"></script>     <!-- JS at bottom of body -->
  </body>
</html>"""},
        {"t": "rule", "q": "Why does the script tag go at the bottom of body?", "a": "JavaScript runs as soon as the browser reads it. If it's in <head>, it runs before the HTML elements exist — so it can't find them. At the bottom of <body>, all elements are already created."},
      ]
    },

    { "id": "html-semantic", "emoji": "🏷️", "name": "Semantic Tags", "sub": "Using the right tag for the right thing",
      "sections": [
        {"t": "intro", "c": "Semantic tags tell the browser (and screen readers, and Google) WHAT a section is, not just how it looks. Always prefer semantic over generic <div>."},
        {"t": "table", "heads": ["Tag", "What it means", "Use for"],
          "rows": [
            ["&lt;header&gt;", "Top of page or section", "Logo, nav, site title"],
            ["&lt;nav&gt;", "Navigation links", "Menus, sidebars, breadcrumbs"],
            ["&lt;main&gt;", "Primary content", "The main content area (only one per page)"],
            ["&lt;section&gt;", "Thematic grouping", "A distinct topic or chapter"],
            ["&lt;article&gt;", "Self-contained content", "Blog post, card, comment"],
            ["&lt;aside&gt;", "Related side content", "Sidebar, related links, callout box"],
            ["&lt;footer&gt;", "Bottom of page or section", "Copyright, links, contact"],
            ["&lt;figure&gt;", "Media + caption", "Image with description"],
            ["&lt;time&gt;", "A date/time", "Timestamps, event dates"],
            ["&lt;button&gt;", "Clickable action", "Use for actions. Use &lt;a&gt; for navigation."],
          ]
        },
        {"t": "rule", "q": "<div> vs <span> — when do I use each?", "a": "<div> is a block element (takes full width, creates a new line). <span> is inline (stays in the flow of text). Use them as last resort when no semantic tag fits."},
        {"t": "ai", "items": [
          '"Replace all the &lt;div class=nav&gt; with a proper &lt;nav&gt; element"',
          '"Mark up this blog post layout using semantic HTML5 elements"',
          '"Add ARIA labels to these icon buttons so screen readers can understand them"',
        ]},
      ]
    },

    { "id": "html-forms", "emoji": "📝", "name": "Forms & Inputs", "sub": "Collecting data from users",
      "sections": [
        {"t": "intro", "c": "Forms are how users send data to your server. Every login, search bar, signup, and settings page is a form."},
        {"t": "code", "c": """<form action="/signup" method="POST">

  <!-- Text input -->
  <label for="name">Full Name</label>
  <input type="text" id="name" name="name" placeholder="Alice" required>

  <!-- Email (validates format automatically) -->
  <input type="email" name="email" required>

  <!-- Password (hides characters) -->
  <input type="password" name="password" minlength="8" required>

  <!-- Number -->
  <input type="number" name="age" min="0" max="120">

  <!-- Dropdown -->
  <select name="country">
    <option value="uk">United Kingdom</option>
    <option value="us">United States</option>
  </select>

  <!-- Checkbox -->
  <input type="checkbox" id="agree" name="agree" value="yes">
  <label for="agree">I agree to the terms</label>

  <!-- Textarea -->
  <textarea name="message" rows="4"></textarea>

  <!-- Submit button -->
  <button type="submit">Create Account</button>
</form>"""},
        {"t": "table", "heads": ["Input type", "Use for", "Browser bonus"],
          "rows": [
            ["text", "General text", "—"],
            ["email", "Email addresses", "Validates @ format on mobile"],
            ["password", "Passwords", "Hides characters"],
            ["number", "Quantities", "Up/down arrows, validates numbers"],
            ["tel", "Phone numbers", "Numeric keyboard on mobile"],
            ["date", "Date picker", "Native date picker UI"],
            ["file", "Upload files", "Opens file browser"],
            ["checkbox", "On/off toggle", "—"],
            ["radio", "One of many options", "—"],
            ["range", "Slider", "Visual slider UI"],
            ["search", "Search bars", "× clear button on mobile"],
          ]
        },
        {"t": "ai", "items": [
          '"Build a login form with email and password fields, proper labels and accessibility"',
          '"Add client-side validation attributes to this form (required, minlength, pattern)"',
          '"Convert this form to submit via JavaScript fetch() instead of page reload"',
        ]},
      ]
    },

    { "id": "html-attrs", "emoji": "🎯", "name": "Attributes", "sub": "id, class, data- and everything else",
      "sections": [
        {"t": "intro", "c": "Attributes add extra information to HTML elements. The most important ones are id, class, and data-* — you'll use these constantly."},
        {"t": "code", "c": """<!-- id: unique per page — use for JS targeting or anchor links -->
<div id="chat-window">...</div>
document.getElementById("chat-window")

<!-- class: reusable — use for CSS styling -->
<div class="card active large">...</div>
document.querySelectorAll(".card")

<!-- data-*: store custom data on elements -->
<button data-user-id="42" data-action="delete">Delete</button>

// In JavaScript:
btn.dataset.userId    // "42"
btn.dataset.action    // "delete"

<!-- href: where a link goes -->
<a href="/about">About</a>
<a href="https://example.com" target="_blank">External</a>

<!-- src: where an image/script comes from -->
<img src="/images/logo.png" alt="Company logo">

<!-- alt: text if image fails — required for accessibility -->
<!-- target="_blank": opens link in new tab -->"""},
        {"t": "rule", "q": "When to use id vs class?", "a": "id = one unique element (the chat box, the sidebar). class = a group of similar elements (all cards, all buttons). Never use the same id twice on one page. Classes can be reused everywhere."},
        {"t": "ai", "items": [
          '"Add data-attributes to these list items so JavaScript can read the record ID"',
          '"Add proper alt text to all images in this file"',
          '"Replace these id selectors in the CSS with class selectors"',
        ]},
      ]
    },
  ]
},

# ═══════════════ CSS ═══════════════
"css": {
  "label": "CSS", "emoji": "🎨", "color": "var(--css)", "bg": "var(--css-bg)",
  "intro": "CSS controls every visual decision — color, size, spacing, layout, animation. It reads like English and misbehaves like magic.",
  "analogy": "🎨 HTML is the pencil sketch. CSS is the paint, lighting, and frame around it.",
  "topics": [
    { "id": "css-selectors", "emoji": "🎯", "name": "Selectors", "sub": "How CSS targets elements",
      "sections": [
        {"t": "intro", "c": "A selector is the part that says \"apply this style to THESE elements\". Getting selectors right is 80% of CSS skill."},
        {"t": "code", "c": """/* Element — every <p> on the page */
p { color: #333; }

/* Class — every element with class="card" */
.card { border: 1px solid #ddd; }

/* ID — the one element with id="header" */
#header { background: navy; }

/* Descendant — <a> inside .nav (any depth) */
.nav a { text-decoration: none; }

/* Direct child — <li> DIRECT child of <ul> */
ul > li { margin-bottom: 8px; }

/* Multiple selectors — apply same style to both */
h1, h2, h3 { font-weight: 900; }

/* Pseudo-class — state-based */
a:hover { color: blue; }           /* mouse over */
button:disabled { opacity: 0.5; }  /* disabled state */
li:first-child { font-weight: bold; }
li:nth-child(2) { background: #f0f0f0; }

/* Pseudo-element — target part of element */
p::first-line { font-weight: bold; }
input::placeholder { color: #aaa; }"""},
        {"t": "rule", "q": "Why is my CSS not applying?", "a": "1) Specificity: more specific selector wins (id beats class beats element). 2) Order: last rule wins if specificity is equal. 3) Typo in selector or property. Check browser DevTools — it shows which rule is winning."},
        {"t": "ai", "items": [
          '"Add a hover state to these cards that lifts them with a shadow"',
          '"Style the first item in this list differently from the rest"',
          '"Add a focus ring to all form inputs for keyboard accessibility"',
        ]},
      ]
    },

    { "id": "css-boxmodel", "emoji": "📦", "name": "Box Model", "sub": "How every element is sized and spaced",
      "sections": [
        {"t": "intro", "c": "Every element in CSS is a rectangular box made of 4 layers. Understanding this stops 90% of layout confusion."},
        {"t": "code", "c": """/* From inside out: content → padding → border → margin */

.card {
  width: 300px;           /* content width */
  padding: 20px;          /* space INSIDE border */
  border: 2px solid #ddd; /* the border line */
  margin: 16px;           /* space OUTSIDE border (pushes other elements) */

  /* box-sizing: border-box — width includes padding+border (recommended) */
  box-sizing: border-box;
}

/* Shorthand: top right bottom left (clockwise from top) */
padding: 10px 20px 10px 20px;  /* all four */
padding: 10px 20px;            /* top+bottom | left+right */
padding: 10px;                 /* all four equal */

/* margin: auto centers a block element horizontally */
.container { max-width: 1200px; margin: 0 auto; }"""},
        {"t": "rule", "q": "padding vs margin — which to use?", "a": "padding = space inside the element (increases its size, background shows). margin = space outside (pushes other elements away, transparent). When in doubt: padding for internal breathing room, margin for distance between elements."},
        {"t": "ai", "items": [
          '"Add box-sizing: border-box to all elements globally"',
          '"Centre this div horizontally using margin: auto"',
          '"Why does my element have extra space below it? (answer: inline elements have line-height gap)"',
        ]},
      ]
    },

    { "id": "css-flexbox", "emoji": "↔️", "name": "Flexbox", "sub": "Line things up in a row or column",
      "sections": [
        {"t": "intro", "c": "Flexbox is for one-dimensional layouts — a row OR a column. Use it to align things, space them, center them."},
        {"t": "code", "c": """/* 1. Add display:flex to the PARENT (container) */
.nav {
  display: flex;
  flex-direction: row;          /* row (default) | column */
  justify-content: space-between; /* main axis: how to space items */
  align-items: center;          /* cross axis: how to align items */
  gap: 16px;                    /* space between items */
  flex-wrap: wrap;              /* allow wrapping to next line */
}

/* justify-content options:
   flex-start | flex-end | center | space-between | space-around | space-evenly */

/* align-items options:
   flex-start | flex-end | center | stretch | baseline */

/* 2. Control individual items (children) */
.nav-logo { flex: 0 0 auto; }   /* don't grow or shrink */
.nav-links { flex: 1; }         /* take up all remaining space */"""},
        {"t": "rule", "q": "Flexbox vs Grid — when to use each?", "a": "Flexbox = one direction at a time (a navbar, a row of buttons, a vertical stack). Grid = two directions at once (a card grid, a page layout with sidebar). Start with Flexbox; when you find yourself fighting it to make a 2D layout, switch to Grid."},
        {"t": "ai", "items": [
          '"Centre this div both vertically and horizontally using flexbox"',
          '"Make this navbar have logo on the left and links on the right"',
          '"Make this flex container wrap on mobile and stack in a column"',
        ]},
      ]
    },

    { "id": "css-grid", "emoji": "▦", "name": "Grid", "sub": "Two-dimensional layouts",
      "sections": [
        {"t": "intro", "c": "Grid lets you define rows AND columns. The most powerful layout tool in CSS. Use it for page layouts, card grids, and any 2D arrangement."},
        {"t": "code", "c": """/* Define the grid on the PARENT */
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);   /* 3 equal columns */
  grid-template-columns: 250px 1fr;        /* sidebar + content */
  grid-template-columns: repeat(auto-fill, minmax(250px,1fr)); /* responsive! */
  gap: 24px;                               /* space between cells */
}

/* Place items in specific cells */
.featured-card {
  grid-column: 1 / 3;   /* span from column 1 to 3 */
  grid-row: 1 / 2;
}

/* Named areas — most readable approach */
.page {
  display: grid;
  grid-template-areas:
    "header  header"
    "sidebar content"
    "footer  footer";
  grid-template-columns: 250px 1fr;
}
.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.content { grid-area: content; }"""},
        {"t": "ai", "items": [
          '"Create a responsive card grid that shows 1 column on mobile, 2 on tablet, 3 on desktop"',
          '"Make this 2-column layout using CSS Grid with named template areas"',
          '"Make the hero card span full width while the others are 3-up"',
        ]},
      ]
    },

    { "id": "css-responsive", "emoji": "📱", "name": "Responsive Design", "sub": "Making it work on every screen size",
      "sections": [
        {"t": "intro", "c": "Responsive design means your app looks good on phones, tablets, and desktops — automatically. You write CSS that changes based on screen width."},
        {"t": "code", "c": """/* Mobile-first: write base styles for small screens,
   then ADD styles for larger screens with min-width */

.grid { grid-template-columns: 1fr; }     /* mobile: 1 column */

@media (min-width: 640px) {              /* tablet+ */
  .grid { grid-template-columns: 1fr 1fr; }
}
@media (min-width: 1024px) {             /* desktop+ */
  .grid { grid-template-columns: repeat(3, 1fr); }
}

/* Common breakpoints (px) */
/* 640  = sm — large phones / small tablets  */
/* 768  = md — tablets                       */
/* 1024 = lg — small desktops               */
/* 1280 = xl — standard desktops            */

/* Useful responsive units */
width: 100%;          /* 100% of parent */
max-width: 1200px;    /* never wider than 1200px */
font-size: clamp(1rem, 2vw, 1.5rem);  /* scales between 1rem and 1.5rem */"""},
        {"t": "tip", "c": "✓ Always add the viewport meta tag in HTML: &lt;meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"&gt; — without it, mobile browsers zoom out and ignore your media queries."},
        {"t": "ai", "items": [
          '"Add responsive breakpoints to make this layout stack on mobile"',
          '"Make this font size scale fluidly between 1rem on mobile and 1.5rem on desktop using clamp()"',
          '"Add a hamburger menu that shows on mobile and hides on desktop"',
        ]},
      ]
    },

    { "id": "css-variables", "emoji": "🎨", "name": "CSS Variables", "sub": "Reusable values — your design system",
      "sections": [
        {"t": "intro", "c": "CSS variables let you store a colour, size, or any value once — then use it everywhere. Change it in one place, update everywhere."},
        {"t": "code", "c": """/* Define on :root (global) */
:root {
  --color-primary: #4F46E5;
  --color-text:    #111827;
  --color-bg:      #F9FAFB;
  --spacing-sm:    8px;
  --spacing-md:    16px;
  --spacing-lg:    32px;
  --radius:        12px;
  --shadow:        0 4px 24px rgba(0,0,0,0.10);
}

/* Use anywhere with var() */
.button {
  background: var(--color-primary);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

/* Dark mode with variables */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #F9FAFB;
    --color-bg:   #111827;
  }
}"""},
        {"t": "ai", "items": [
          '"Extract all hardcoded colours in this CSS file into CSS variables on :root"',
          '"Add a dark mode using CSS variables and prefers-color-scheme media query"',
          '"Create a consistent spacing scale using CSS variables (4px, 8px, 16px, 32px, 64px)"',
        ]},
      ]
    },
  ]
},

# ═══════════════ JAVASCRIPT ═══════════════
"js": {
  "label": "JavaScript", "emoji": "⚡", "color": "var(--js)", "bg": "var(--js-bg)",
  "intro": "The only language browsers can run. Makes pages interactive, talks to your server, updates the UI without reloading.",
  "analogy": "💡 HTML is the room. CSS is how it looks. JavaScript is the electricity — it makes things actually work.",
  "topics": [
    { "id": "js-vars", "emoji": "🏷️", "name": "Variables & Scope", "sub": "let, const, var — and where they live",
      "sections": [
        {"t": "intro", "c": "JavaScript has three ways to declare variables. In practice: use const for everything, use let when the value needs to change. Forget var exists."},
        {"t": "code", "c": """const name = "Alice";     // cannot be reassigned
let   count = 0;           // can be reassigned
// var  (don't use — confusing scope rules)

count = count + 1;  // ✓ let can change
// name = "Bob";    // ✗ TypeError: const cannot be reassigned

// const with objects/arrays: the variable can't be reassigned,
// but the CONTENTS can change
const user = { name: "Alice" };
user.name = "Bob";    // ✓ changing property is fine
// user = { name: "Bob" }; // ✗ can't reassign the variable

// Scope: where a variable can be seen
let x = 10;                    // module scope
function foo() {
  let y = 20;                  // function scope — invisible outside
  if (true) {
    let z = 30;                // block scope — invisible outside if
    console.log(x, y, z);     // ✓ all visible here
  }
  // z is undefined here
}"""},
        {"t": "ai", "items": [
          '"Replace all var declarations with const or let as appropriate"',
          '"Explain why this variable is undefined at this point in the code"',
        ]},
      ]
    },

    { "id": "js-types", "emoji": "📦", "name": "Data Types", "sub": "What JavaScript can hold",
      "sections": [
        {"t": "code", "c": """// Primitives (not objects)
let name    = "Alice";          // string
let age     = 30;               // number (int AND float — no distinction)
let price   = 9.99;             // number
let active  = true;             // boolean
let empty   = null;             // intentionally empty
let missing = undefined;        // not yet assigned

// Reference types (objects)
let user    = { name: "Alice", age: 30 };   // object
let items   = [1, 2, 3];                    // array (is an object)
let fn      = function() {};                // function (is an object)

// Type checking
typeof "hello"     // "string"
typeof 42          // "number"
typeof true        // "boolean"
typeof null        // "object"  ← famous JS bug, null is NOT an object
typeof undefined   // "undefined"
typeof []          // "object"  ← use Array.isArray([]) instead
Array.isArray([])  // true"""},
        {"t": "warn", "c": "⚠️ JavaScript has loose equality (==) that converts types, and strict equality (===) that does not. ALWAYS use === and !== — never == or !=. typeof null === \"object\" is a 25-year-old bug that will never be fixed."},
      ]
    },

    { "id": "js-functions", "emoji": "⚙️", "name": "Functions", "sub": "Three syntaxes for the same idea",
      "sections": [
        {"t": "intro", "c": "JavaScript has three ways to write functions. All do the same thing. Arrow functions are most common in modern code."},
        {"t": "code", "c": r"""// 1. Declaration (hoisted — can call before definition)
function greet(name) {
  return "Hello " + name;
}

// 2. Expression (not hoisted)
const greet = function(name) {
  return "Hello " + name;
};

// 3. Arrow function (most modern, most common)
const greet = (name) => "Hello " + name;  // implicit return

const add = (a, b) => a + b;       // one-liner implicit return
const square = n => n * n;          // one param, no parens needed
const doSomething = () => {         // multi-line: use braces + return
  const result = complexCalc();
  return result;
};

// Default parameters
const greet2 = (name = "stranger") => `Hello, ${name}!`;
greet2()           // "Hello, stranger!"
greet2("Alice")    // "Hello, Alice!" """},
        {"t": "heading", "c": "Callbacks — Functions Passed as Arguments"},
        {"t": "code", "c": """// A callback is a function you give to another function to call later
setTimeout(() => console.log("3 seconds passed"), 3000);

// Array methods use callbacks
const numbers = [1, 2, 3, 4, 5];
numbers.map(n => n * 2)        // [2, 4, 6, 8, 10]
numbers.filter(n => n > 2)     // [3, 4, 5]
numbers.find(n => n > 3)       // 4 (first match)
numbers.every(n => n > 0)      // true (all match)
numbers.some(n => n > 4)       // true (at least one matches)
numbers.reduce((sum, n) => sum + n, 0)  // 15 (total)"""},
        {"t": "ai", "items": [
          '"Rewrite this function declaration as an arrow function"',
          '"Extract this inline callback into a named function"',
          '"Use Array.map() and Array.filter() to replace this for loop"',
        ]},
      ]
    },

    { "id": "js-dom", "emoji": "🌳", "name": "DOM Manipulation", "sub": "Reading and changing the page",
      "sections": [
        {"t": "intro", "c": "The DOM (Document Object Model) is the live tree of HTML elements in the browser. JavaScript can read, create, change, and delete any element."},
        {"t": "code", "c": """// Find elements
document.getElementById("header")           // one element by id
document.querySelector(".card")             // FIRST element matching CSS selector
document.querySelectorAll(".card")          // ALL matching elements (NodeList)

// Read
element.textContent           // text inside (safe, no HTML)
element.innerHTML             // HTML inside (careful with user input!)
element.value                 // form input value
element.getAttribute("data-id")  // read attribute

// Change
element.textContent = "New text";
element.innerHTML   = "<strong>Bold</strong>";
element.style.color = "red";
element.classList.add("active");
element.classList.remove("hidden");
element.classList.toggle("open");
element.setAttribute("data-id", "42");

// Create and insert
const div = document.createElement("div");
div.className = "card";
div.textContent = "I am new";
parent.appendChild(div);            // add at end
parent.prepend(div);                // add at start
parent.insertBefore(div, sibling);  // before specific child

// Remove
element.remove();"""},
        {"t": "ai", "items": [
          '"Update the text content of #results with the API response"',
          '"Toggle the class open on this nav element when the hamburger is clicked"',
          '"Generate a list of <li> elements from this array and append to #list"',
        ]},
      ]
    },

    { "id": "js-events", "emoji": "👂", "name": "Events", "sub": "Reacting to what the user does",
      "sections": [
        {"t": "intro", "c": "Events are things that happen — click, type, scroll, submit. You attach a listener to an element and it fires a function when the event occurs."},
        {"t": "code", "c": """// The pattern: element.addEventListener("event", callback)
const btn = document.querySelector("#submit-btn");
btn.addEventListener("click", (event) => {
  console.log("Clicked!", event);
});

// Common events
element.addEventListener("click",    () => {});   // mouse click
element.addEventListener("dblclick", () => {});   // double click
element.addEventListener("mouseover",() => {});   // hover
element.addEventListener("keydown",  (e) => {     // key pressed
  if (e.key === "Enter") submitForm();
  if (e.key === "Escape") closeModal();
});
input.addEventListener("input",      (e) => {    // while typing
  console.log(e.target.value);
});
input.addEventListener("change",     (e) => {    // after typing done
  validate(e.target.value);
});
form.addEventListener("submit",      (e) => {    // form submit
  e.preventDefault();   // MUST stop page reload!
  handleSubmit();
});
window.addEventListener("scroll",    () => {});
document.addEventListener("DOMContentLoaded", () => {});  // page loaded"""},
        {"t": "tip", "c": "✓ e.preventDefault() stops the browser's default action. Use it on form submit (stops page reload), on anchor clicks (stops navigation), on drag events."},
        {"t": "ai", "items": [
          '"Add a click handler to all .delete-btn elements using event delegation"',
          '"Add keyboard shortcuts: Ctrl+Enter to submit, Escape to close"',
          '"Debounce this search input handler so it only fires 300ms after the user stops typing"',
        ]},
      ]
    },

    { "id": "js-fetch", "emoji": "📡", "name": "Fetch & APIs", "sub": "Talking to your Python backend",
      "sections": [
        {"t": "intro", "c": "fetch() sends HTTP requests from JavaScript to your server. This is how your frontend talks to Flask — sends data, gets data, updates the page without reloading."},
        {"t": "code", "c": """// GET — fetch data from server
const response = await fetch("/api/users");
const data = await response.json();
console.log(data);

// POST — send data to server
const response2 = await fetch("/api/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Alice", email: "a@b.com" })
});
const result = await response2.json();

// Full pattern with error handling
async function createUser(name, email) {
  try {
    const res = await fetch("/api/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email })
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.error || "Server error");
    }
    return await res.json();
  } catch (e) {
    console.error("Failed:", e.message);
    showError(e.message);
  }
}"""},
        {"t": "heading", "c": "Async / Await — The Right Way to Handle Waiting"},
        {"t": "code", "c": """// async: marks a function as asynchronous (always returns a Promise)
// await: pauses here until the Promise resolves — only inside async functions

async function loadData() {
  const res  = await fetch("/api/data");  // wait for network
  const data = await res.json();          // wait for JSON parsing
  displayData(data);                      // now we have the data
}

// Run on page load
document.addEventListener("DOMContentLoaded", async () => {
  await loadData();
});"""},
        {"t": "ai", "items": [
          '"Add a fetch() call to POST this form data to /api/orders and show success/error"',
          '"Add a loading spinner while the fetch is in progress"',
          '"Convert this .then().catch() chain to async/await"',
        ]},
      ]
    },
  ]
},

# ═══════════════ HOW THEY CONNECT ═══════════════
"connect": {
  "label": "How They Connect", "emoji": "🔗", "color": "var(--connect)", "bg": "var(--connect-bg)",
  "intro": "The 5 technologies aren't separate — they're a pipeline. Data flows through all of them every time a user does something.",
  "analogy": "🏭 Like a factory assembly line. Each station does one job and passes the result to the next.",
  "topics": [
    { "id": "con-request", "emoji": "🔄", "name": "A Request's Life", "sub": "What happens when you click Submit",
      "sections": [
        {"t": "intro", "c": "Follow one form submission from click to database and back. This is the entire web in one flow."},
        {"t": "code", "c": """/* Step 1 — HTML defines the form the user fills in */
<form id="add-user">
  <input name="name" type="text">
  <button type="submit">Add User</button>
</form>

/* Step 2 — JavaScript intercepts submit, sends fetch() to Python */
document.querySelector("#add-user").addEventListener("submit", async (e) => {
  e.preventDefault();                              // don't reload!
  const name = e.target.name.value;
  const res  = await fetch("/api/users", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({name})
  });
  const data = await res.json();
  displayUser(data.user);                          // update the page
});

# Step 3 — Python Flask receives, validates, calls SQL
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    name = data.get("name","").strip()
    if not name:
        return jsonify({"error":"Name required"}), 400

    # Step 4 — SQL stores the data
    conn = get_db()
    conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    user_id = conn.lastrowid

    # Step 5 — Python returns JSON to JavaScript
    return jsonify({"user":{"id":user_id,"name":name}}), 201

/* Step 6 — JavaScript updates the HTML with the response (Step 2 above) */"""},
        {"t": "rule", "q": "Where do I put validation?", "a": "Frontend (JS): instant feedback as user types. Backend (Python): the authoritative check. Database (SQL constraints): the final safety net. Validation should be in all three layers for different reasons — never trust only one."},
      ]
    },

    { "id": "con-files", "emoji": "📁", "name": "Who Owns What", "sub": "Which language controls which concern",
      "sections": [
        {"t": "table", "heads": ["Task", "Language", "Why"],
          "rows": [
            ["Page structure", "HTML", "Browsers only understand HTML as structure"],
            ["Visual styling", "CSS", "Separation of style from content"],
            ["User interactions", "JavaScript", "Only JS runs in browsers"],
            ["API calls to server", "JavaScript fetch()", "Browsers can't run Python"],
            ["Server routes (URLs)", "Python/Flask", "Runs on server, not browser"],
            ["Business logic", "Python", "Secure, can't be tampered with by users"],
            ["Read/write data", "SQL", "Databases speak SQL"],
            ["Validate user input", "Both JS+Python", "JS=speed, Python=security"],
            ["Store secrets/API keys", "Python (env vars)", "NEVER in JS — visible to everyone"],
          ]
        },
      ]
    },

    { "id": "con-debug", "emoji": "🐛", "name": "Debugging Map", "sub": "Which tool to open when something's wrong",
      "sections": [
        {"t": "table", "heads": ["Symptom", "Where to look", "Tool"],
          "rows": [
            ["Wrong layout / missing element", "HTML in browser", "Right-click → Inspect → Elements tab"],
            ["Wrong colour / size / position", "CSS rules", "DevTools → Styles panel (right side)"],
            ["Button does nothing", "JS event listener", "DevTools → Console for errors"],
            ["Data not sending/receiving", "fetch() call", "DevTools → Network tab → XHR/Fetch"],
            ["Server returns error", "Python route", "Terminal running Flask — read the traceback"],
            ["Wrong data returned", "SQL query", "Add print(query,params) in Flask, check terminal"],
            ["App crashes on startup", "config/imports", "Read the FULL error in terminal — bottom line is the problem"],
            ["Works locally not deployed", "env variables", "Check Railway Variables tab — is the env var set?"],
          ]
        },
        {"t": "tip", "c": "✓ Open browser DevTools with F12. The Console tab shows JS errors. The Network tab shows every HTTP request and the exact response from your server. These two tabs solve 80% of frontend problems."},
      ]
    },
  ]
},

}  # end TECH


# ─────────────────────────────────────────────────────────────────────────────
# JOURNEY STEPS — the beginner SOP flow (12 steps from idea to shipped)
# ─────────────────────────────────────────────────────────────────────────────

JOURNEY_STEPS = [
  {
    "step_id": "step-01-idea",
    "order": 1,
    "emoji": "💡",
    "title": "Have the Idea",
    "tagline": "It all starts with one idea.",
    "description": "Write your app idea in one sentence. What does it do? Who uses it? What problem does it solve? Don't code yet — just clarity.",
    "instructions": [
      "Write: 'My app lets [who] [do what] so that [outcome]'",
      "List the 3 most important things a user can do",
      "Sketch it on paper — boxes, arrows, labels",
    ],
    "linked_topics": [],
    "checkpoint": "You have a one-sentence description and a paper sketch.",
  },
  {
    "step_id": "step-02-html",
    "order": 2,
    "emoji": "🦴",
    "title": "Sketch the HTML",
    "tagline": "Build the skeleton before the skin.",
    "description": "Turn your paper sketch into HTML. No CSS yet — just structure. Use semantic tags. Get the bones right.",
    "instructions": [
      "Create index.html with DOCTYPE, head, body",
      "Add a header, main content area, and footer",
      "Use semantic tags for every section",
      "Add placeholder text — real words, not Lorem Ipsum",
    ],
    "linked_topics": ["html-structure", "html-semantic"],
    "checkpoint": "Open index.html in browser — ugly but structured.",
  },
  {
    "step_id": "step-03-forms",
    "order": 3,
    "emoji": "📝",
    "title": "Add Forms & Inputs",
    "tagline": "How will users talk to your app?",
    "description": "Every app needs at least one way for users to send data. Add your forms now, with proper labels and input types.",
    "instructions": [
      "Identify every place a user enters data",
      "Add <form> elements with correct method and action",
      "Use the right input type for each field (email, number, text)",
      "Add labels for every input — for accessibility",
    ],
    "linked_topics": ["html-forms", "html-attrs"],
    "checkpoint": "All forms present. Tab through them with keyboard — works?",
  },
  {
    "step_id": "step-04-css",
    "order": 4,
    "emoji": "🎨",
    "title": "Style with CSS",
    "tagline": "Make it look like you meant it.",
    "description": "Create a separate style.css file. Define your colours as CSS variables first. Layout with Flexbox/Grid. Mobile-first.",
    "instructions": [
      "Create static/style.css, link it in <head>",
      "Define your colour palette as CSS variables on :root",
      "Add box-sizing: border-box globally",
      "Layout the main sections with Flexbox or Grid",
      "Add a @media query for mobile (max-width: 768px)",
    ],
    "linked_topics": ["css-variables", "css-flexbox", "css-grid", "css-responsive"],
    "checkpoint": "Looks intentional. Resize browser window — mobile works.",
  },
  {
    "step_id": "step-05-js",
    "order": 5,
    "emoji": "⚡",
    "title": "Add Interactivity",
    "tagline": "Make it react to the user.",
    "description": "Create app.js. Add event listeners to make the UI respond. Intercept form submits so the page doesn't reload.",
    "instructions": [
      "Create static/app.js, add <script> at bottom of body",
      "Add DOMContentLoaded wrapper around all your code",
      "Intercept every form submit with e.preventDefault()",
      "Read form values with .value",
      "Update the DOM to show results",
    ],
    "linked_topics": ["js-events", "js-dom", "js-vars"],
    "checkpoint": "Form submit doesn't reload page. Console shows the data.",
  },
  {
    "step_id": "step-06-flask",
    "order": 6,
    "emoji": "🌐",
    "title": "Set Up Flask",
    "tagline": "Give your app a brain on the server.",
    "description": "Create a Python virtual environment. Install Flask. Write app.py with one route that renders your HTML template.",
    "instructions": [
      "python -m venv venv && venv/Scripts/activate",
      "pip install flask && pip freeze > requirements.txt",
      "Create app.py with Flask(__name__)",
      "Move index.html to templates/index.html",
      "Create a route: @app.route('/') that returns render_template('index.html')",
      "Run: python app.py → visit localhost:5000",
    ],
    "linked_topics": ["py-flask", "py-modules"],
    "checkpoint": "python app.py runs without errors. Browser shows your page.",
  },
  {
    "step_id": "step-07-api",
    "order": 7,
    "emoji": "🔌",
    "title": "Create API Routes",
    "tagline": "Let JS and Python talk to each other.",
    "description": "Turn your form submissions into POST routes. Have Flask receive JSON from fetch(), process it, and return JSON back.",
    "instructions": [
      "Add a POST route for each form: @app.route('/api/...', methods=['POST'])",
      "Read the body: data = request.json",
      "Validate required fields, return 400 if missing",
      "Return jsonify({'result': ...}), 201",
      "Update app.js fetch() calls to point to your new routes",
    ],
    "linked_topics": ["py-flask", "js-fetch", "con-request"],
    "checkpoint": "Submit form → Network tab shows 201 response with JSON.",
  },
  {
    "step_id": "step-08-sqlite",
    "order": 8,
    "emoji": "🗄️",
    "title": "Connect to SQLite",
    "tagline": "Give your app a memory.",
    "description": "Create a database.py file. Design your tables. Connect Flask to SQLite so data persists between requests.",
    "instructions": [
      "Create database.py with get_db() and init_db()",
      "Write CREATE TABLE statements for your data",
      "Call init_db() when app starts",
      "In your POST routes: get_db().execute('INSERT...', (params,))",
      "In your GET routes: get_db().execute('SELECT...').fetchall()",
    ],
    "linked_topics": ["sql-create", "sql-write", "sql-select", "py-flask"],
    "checkpoint": "Submit form → data appears in DB. Restart server → data still there.",
  },
  {
    "step_id": "step-09-display",
    "order": 9,
    "emoji": "📊",
    "title": "Display Dynamic Data",
    "tagline": "Show what's in the database.",
    "description": "Query the database and show results. Either pass data to Jinja2 templates (server-side) or fetch it with JavaScript (client-side).",
    "instructions": [
      "Add a GET route that queries the DB and returns JSON",
      "In app.js: fetch the data on DOMContentLoaded",
      "Loop through results and create DOM elements",
      "OR: pass data to render_template() and use {{ }} in HTML",
    ],
    "linked_topics": ["sql-select", "sql-joins", "js-fetch", "js-dom"],
    "checkpoint": "Page loads → shows real data from database.",
  },
  {
    "step_id": "step-10-errors",
    "order": 10,
    "emoji": "🛡️",
    "title": "Handle Errors",
    "tagline": "Expect the unexpected.",
    "description": "Add try/except in Python, check !res.ok in JavaScript, and add SQL constraints. A robust app handles failure gracefully.",
    "instructions": [
      "Wrap DB calls in try/except in Python",
      "Return proper HTTP status codes (400, 404, 500)",
      "In JS: check if (!res.ok) and show user-friendly error messages",
      "Add NOT NULL and UNIQUE constraints to your SQL tables",
      "Test: what happens if you submit empty form? Duplicate data?",
    ],
    "linked_topics": ["py-errors", "py-flask", "js-fetch", "sql-create"],
    "checkpoint": "Empty form submit shows error message, not a crash.",
  },
  {
    "step_id": "step-11-deploy",
    "order": 11,
    "emoji": "🚀",
    "title": "Deploy to Railway",
    "tagline": "Share it with the world.",
    "description": "Put your app on the internet using Railway — the simplest platform for Flask apps. Free tier included.",
    "instructions": [
      "Push code to GitHub (all files except venv/ and .env)",
      "Go to railway.app → New Project → Deploy from GitHub",
      "Set start command: python app.py",
      "Add environment variables if needed",
      "Railway gives you a public URL in 2 minutes",
    ],
    "linked_topics": ["con-debug"],
    "checkpoint": "Your app is live at a railway.app URL. Send it to someone.",
  },
  {
    "step_id": "step-12-reflect",
    "order": 12,
    "emoji": "🌟",
    "title": "Reflect & Build Next",
    "tagline": "Every app teaches you the next one.",
    "description": "You built a full-stack web app. What did you learn? What would you do differently? What's the next idea?",
    "instructions": [
      "Write down 3 things that surprised you",
      "Write down 2 things you'd improve",
      "Write down your next idea — it all starts with one idea",
      "Come back to the Reference tab — you'll read it differently now",
    ],
    "linked_topics": [],
    "checkpoint": "You're a web developer. Seriously.",
  },
]


# ─────────────────────────────────────────────────────────────────────────────
# Helpers used by ollama_client.py to build context strings
# ─────────────────────────────────────────────────────────────────────────────

def get_topic_index():
    """Return a compact string listing all topic IDs and names."""
    lines = []
    for tech_key, tech in TECH.items():
        for topic in tech["topics"]:
            lines.append(f"{topic['id']}: {tech['label']} › {topic['name']} — {topic['sub']}")
    return "\n".join(lines)


def get_topic_by_id(topic_id: str):
    """Return (tech, topic) tuple for a given topic_id, or (None, None)."""
    for tech_key, tech in TECH.items():
        for topic in tech["topics"]:
            if topic["id"] == topic_id:
                return tech, topic
    return None, None


def get_topic_text_summary(topic_id: str, max_chars: int = 600) -> str:
    """Return a plain-text summary of a topic's content for LLM context."""
    tech, topic = get_topic_by_id(topic_id)
    if not topic:
        return ""
    parts = [f"{topic['name']} ({tech['label']}): {topic['sub']}"]
    for sec in topic["sections"]:
        if sec["t"] == "intro":
            parts.append(sec["c"])
        elif sec["t"] == "code":
            parts.append(f"Code example:\n{sec['c'][:300]}")
        if sum(len(p) for p in parts) > max_chars:
            break
    return "\n".join(parts)[:max_chars]
