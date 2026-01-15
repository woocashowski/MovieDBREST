from fastapi import FastAPI
# Punkt 4
import requests 
# Punkt 5
from db import get_connection 
# Punkt 6
from typing import Any
# Punkt 7
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Punkt 3
@app.get("/sum")
def sum(x: int = 0, y: int = 10):
    return x+y

# Punkt 4
@app.get("/geocode")
def geocode(lat: float, lon: float):
    url = (
        "https://nominatim.openstreetmap.org/reverse"
        f"?lat={lat}&lon={lon}&format=json"
    )

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    return response.json()


# Punkt 5
# @app.get("/movies")
# def get_movies():
#     conn = get_connection()
#     cur = conn.cursor()

#     cur.execute("SELECT * FROM movies")
#     rows = cur.fetchall()

#     result = []
#     for row in rows:
#         result.append(dict(row))

#     conn.close()
#     return result

# Punkt 6. Dodawanie filmu
# @app.post("/movies")
# def add_movie(params: dict[str, Any]):
#     conn = get_connection()
#     cur = conn.cursor()

#     cur.execute("""
#         INSERT INTO movies (title, year, actors)
#         VALUES (?, ?, ?)
#     """, (
#         params.get("title"),
#         params.get("year"),
#         params.get("actors")
#     ))

#     conn.commit()
#     movie_id = cur.lastrowid
#     conn.close()

#     return {"message": "Movie added successfully", "id": movie_id}

# Testować:
# Invoke-RestMethod `
#   -Uri http://127.0.0.1:8000/movies `
#   -Method POST `
#   -ContentType "application/json" `
#   -Body '{"title":"The Matrix","year":1999,"actors":"Keanu Reeves"}'

# Punkt 7. Usuwanie filmu, aktualizacja filmu
@app.delete("/movies")
def delete_all_movies():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM movies")
    conn.commit()

    deleted = cur.rowcount
    conn.close()

    if deleted == 0:
        raise HTTPException(status_code=404, detail="No movies to delete")

    return {"message": f"Deleted {deleted} movies"}

# Do testowania:
# http://127.0.0.1:8000/docs
# POST /movies
# Wpisujemy tam:
# {
#   "title": "Matrix",
#   "year": 1999,
#   "director": "Wachowski",
#   "description": "Sci-fi"
# }


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()

    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Movie not found")

    conn.close()
    return {"message": "Movie deleted"}
# Test:
# DELETE /movies/1

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, params: dict[str, Any]):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE movies
        SET title = ?, year = ?, director = ?, description = ?
        WHERE id = ?
    """, (
        params.get("title"),
        params.get("year"),
        params.get("director"),
        params.get("description"),
        movie_id
    ))

    conn.commit()

    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Movie not found")

    conn.close()
    return {"message": "Movie updated"}
# Do testowania:
# http://127.0.0.1:8000/docs
# PUT /movies/4
# {
#   "title": "Matrix Reloaded",
#   "year": 2003,
#   "director": "Wachowski",
#   "description": "Sequel"
# }

# Punkt 8
@app.post("/movies")
def add_movie(params: dict[str, Any]):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO movies (title, year, director, description)
        VALUES (?, ?, ?, ?)
    """, (
        params.get("title"),
        params.get("year"),
        params.get("director"),
        params.get("description")
    ))

    conn.commit()
    movie_id = cur.lastrowid
    conn.close()

    return {"message": "Movie added successfully", "id": movie_id}
# TEST:
# POST /movies
# {
#   "title": "Matrix",
#   "year": 1999,
#   "director": "Wachowski",
#   "description": "Sci-fi"
# }

@app.get("/movies")
def get_movies():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()
    conn.close()

    return [dict(row) for row in rows]
# TEST:
# Przeglądarka:
# http://127.0.0.1:8000/movies

@app.get("/actors")
def get_actors():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM actors")
    rows = cur.fetchall()
    conn.close()

    return [dict(r) for r in rows]
# TEST:
# http://127.0.0.1:8000/actors

@app.get("/actors/{actor_id}")
def get_actor(actor_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM actors WHERE id=?", (actor_id,))
    row = cur.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Actor not found")

    return dict(row)
# TEST:
# http://127.0.0.1:8000/actors/1

@app.post("/actors")
def add_actor(params: dict[str, Any]):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO actors (name) VALUES (?)", (params.get("name"),))
    conn.commit()
    actor_id = cur.lastrowid
    conn.close()

    return {"message": "Actor added", "id": actor_id}
# TEST:
# POST /actors
# {
#   "name": "Keanu Reeves"
# }

@app.delete("/actors/{actor_id}")
def delete_actor(actor_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM actors WHERE id=?", (actor_id,))
    conn.commit()

    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Actor not found")

    conn.close()
    return {"message": "Actor deleted"}
# TEST:
# DELETE /actors/1

@app.put("/actors/{actor_id}")
def update_actor(actor_id: int, params: dict[str, Any]):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE actors SET name=? WHERE id=?",
        (params.get("name"), actor_id)
    )

    conn.commit()

    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Actor not found")

    conn.close()
    return {"message": "Actor updated"}
# TEST:
# PUT /actors/1
# {
#   "name": "Keanu Charles Reeves"
# }

@app.get("/movies/{movie_id}/actors")
def get_movie_actors(movie_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT a.id, a.name
        FROM actors a
        JOIN movie_actors ma ON a.id = ma.actor_id
        WHERE ma.movie_id = ?
    """, (movie_id,))

    rows = cur.fetchall()
    conn.close()

    return [dict(r) for r in rows]

# TEST:
# 1 Dodaj film (POST /movies)
# 2 Dodaj aktora (POST /actors)
# 3 Powiąż ręcznie w konsoli:
# import sqlite3
# conn = sqlite3.connect("movies.db")
# cur = conn.cursor()
# cur.execute("INSERT INTO movie_actors VALUES (4,1)")
# conn.commit()
# conn.close()
# 4 Sprawdź:
# http://127.0.0.1:8000/movies/4/actors