# Movie Catalogue Program

## What is this?

This Python script is a simple command-line program that creates and manages a catalogue of movies and TV series. It's a great example for beginners to understand the core ideas of Object-Oriented Programming (OOP), like creating blueprints for objects (classes), reusing code (inheritance), and handling errors gracefully.

## How to Run?

To run this program, simply execute the python script from your terminal:

```bash
python "basic movie_catelogue.py"
```

You should see an output displaying a formatted list of movies and TV series that are hard-coded in the script.

## Detailed Code Walkthrough

This program is built around a few key "blueprints" called **classes**. Think of a class as a recipe for creating an object. We have recipes for a `Movie`, a `TVSeries`, and even for the `MediaCatalogue` itself.

### The `MediaError` Class
```python
class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj
```
Sometimes, a program runs into a problem that it can't recover from, so it "raises an exception" (an error). Python has many built-in exception types, like `ValueError` for bad input.

Here, we define our own special error, `MediaError`. It inherits from Python's basic `Exception` class. This lets us create a specific error for when someone tries to add something to our catalogue that isn't a movie or TV show. This is helpful because it allows us to "catch" this specific error later and handle it differently from other errors.

- The `__init__` method is a special method called a **constructor**. It runs every time a `MediaError` is created.
- It accepts an error `message` (a string) and `obj` (the item that caused the error).
- `super().__init__(message)` passes the message to the parent `Exception` class to handle.
- `self.obj = obj` stores the problematic object so we can inspect it when we catch the error.

---

### The `Movie` Class
This class is the main blueprint for any movie in our program.

```python
class Movie:
    """Parent class representing a movie."""
    
    def __init__(self, title, year, director, duration):
        # ... validation checks ...
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
```

#### The Constructor: `__init__`
When we create a new movie object like `Movie('The Matrix', 1999, ...)`, this method is automatically called. Its job is to set up the object. The `self` parameter refers to the specific object being created.

Inside the constructor, we perform several checks to make sure the data is valid before we even create the object. This is called **input validation**.

- `if not title.strip():`
  - `title.strip()` removes any accidental whitespace from the beginning and end of the title.
  - `if not ...` checks if the resulting string is empty.
  - If it is empty, we `raise ValueError(...)`, which stops the program and shows an error, because a movie must have a title.

- `if year < 1895:`
  - This checks if the year is before 1895 (the approximate start of cinema). If so, it's probably an error, so we raise a `ValueError`.

- `if duration <= 0:`
  - A movie's duration must be a positive number, so we check for that here and raise an error if it's not.

If all the checks pass, the method then assigns the provided `title`, `year`, `director`, and `duration` to the object itself using `self`. For example, `self.title = title` means "set this object's title to the value that was passed in."

#### The String Representation: `__str__`
```python
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'
```
This special method controls what happens when you try to print an object. If you have a `movie1` object and you write `print(movie1)`, Python will call this `__str__` method. It returns a nicely formatted string (an "f-string") that's easy for a human to read.

---

### The `TVSeries` Class
This class is a blueprint for a TV series.

```python
class TVSeries(Movie):
    # ...
```
The key part here is `(Movie)`. This tells Python that `TVSeries` is a **child** of the `Movie` class. This is called **inheritance**. It means that a `TVSeries` automatically gets all the methods and attributes of a `Movie` for free! A TV Series *is a* type of Movie, so it shares its core properties.

#### The Constructor: `__init__`
```python
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)

        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        self.seasons = seasons
        self.total_episodes = total_episodes
```
- A `TVSeries` needs all the `Movie` info, plus `seasons` and `total_episodes`.
- `super().__init__(title, year, director, duration)` is very important. It calls the `__init__` method of the parent class (`Movie`). This is how we reuse the validation logic from the `Movie` class without copying and pasting it.
- After the parent part is set up, we run validation checks for the new attributes (`seasons` and `total_episodes`) and then store them on the object using `self`.

#### Overriding `__str__`
```python
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'
```
Because a `TVSeries` has more information, we want to print it differently. We create a new `__str__` method here to **override** (replace) the one from the `Movie` class. Now, when you print a `TVSeries` object, this more detailed string will be returned.

---

### The `MediaCatalogue` Class
This class is a blueprint for the catalogue that holds our collection of media.

#### Methods
- `__init__(self)`: The constructor creates an empty list called `self.items`. This list will hold all the `Movie` and `TVSeries` objects we add.

- `add(self, media_item)`: This method adds a new item to the catalogue.
  - `if not isinstance(media_item, Movie):` This is a crucial check. `isinstance()` checks if `media_item` is a `Movie` object *or* an object of any class that inherits from `Movie` (like `TVSeries`).
  - If the item is not a `Movie` or `TVSeries`, we raise our custom `MediaError`.
  - If the check passes, `self.items.append(media_item)` adds the item to the end of the `items` list.

- `get_movies(self)` and `get_tv_series(self)`: These methods filter the list.
  - `return [item for item in self.items if type(item) is Movie]` is a **list comprehension**. It's a compact way of creating a new list. It reads: "Create a new list containing every `item` from `self.items` but only `if` the `type` of that `item` is exactly `Movie`."

- `__str__(self)`: This method creates the final, readable printout of the entire catalogue.
  - It first checks if the catalogue is empty.
  - It calls `self.get_movies()` and `self.get_tv_series()` to get separate lists for each type.
  - `if movies:` and `if series:` check if these lists are not empty before trying to print a header.
  - The script then uses a **for loop** to go through each item in the lists.
  - `for i, movie in enumerate(movies, 1):` is a special loop. `enumerate` gives us both the item (`movie`) and a counter (`i`). We start the counter at `1` instead of the default `0`.
  - Inside the loop, `result += f'{i}. {movie}\n'` builds up the final string line by line.

---

### The Script in Action
This is the final part of the script that is not inside a class. It's where we actually use the blueprints we defined.

```python
catalogue = MediaCatalogue()

try:
    # ... creating and adding movies/series ...
    print(catalogue)
except ValueError as e:
    # ... error handling ...
```
- `catalogue = MediaCatalogue()`: We create an instance of our catalogue.
- The `try...except` block is for error handling. Python will `try` to run the code inside the `try` block. If an error (an exception) occurs at any point, the program will immediately jump to the appropriate `except` block and run that code instead of crashing.
  - Inside `try`, we create instances of `Movie` and `TVSeries` and use `catalogue.add()` to put them in our catalogue.
  - `print(catalogue)` triggers the `__str__` method of our `MediaCatalogue` object, printing the whole formatted list.
- `except ValueError as e:`: If a `ValueError` was raised anywhere in the `try` block (like from an empty title), this block will run, printing a friendly error message.
- `except MediaError as e:`: If our custom `MediaError` was raised (from trying to add a non-media item), this block would run.