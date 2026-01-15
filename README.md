# MovieDB REST API

Prosty serwis REST API zbudowany w FastAPI w ramach laboratorium (Lab 2).  
Aplikacja umożliwia zarządzanie filmami oraz aktorami z wykorzystaniem bazy SQLite.

---

## Wymagania

- Python 3.x

---

## Instalacja

```bash
pip install -r requirements.txt

Uruchomienie
fastapi dev main.py

Aplikacja:
http://127.0.0.1:8000


Swagger UI:
http://127.0.0.1:8000/docs

------------------------------------------------

Endpointy:

Filmy
GET /movies — lista filmów
GET /movies/{id} — jeden film
POST /movies — dodanie filmu
PUT /movies/{id} — aktualizacja filmu
DELETE /movies/{id} — usunięcie filmu
DELETE /movies — usunięcie wszystkich filmów

Aktorzy
GET /actors
GET /actors/{id}
POST /actors
PUT /actors/{id}
DELETE /actors/{id}

Relacja film → aktorzy
GET /movies/{movie_id}/actors

Technologie
- FastAPI
- SQLite
- Python