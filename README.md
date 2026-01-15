# MovieDBREST

A simple REST API for managing a movie database using Flask and SQLAlchemy.

## Features

- Get all movies
- Get a specific movie by ID
- Create a new movie
- Update a movie
- Delete a movie

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. The API will be available at `http://localhost:5000`

## API Endpoints

- `GET /api/movies` - Get all movies
- `GET /api/movies/<id>` - Get a specific movie
- `POST /api/movies` - Create a new movie
- `PUT /api/movies/<id>` - Update a movie
- `DELETE /api/movies/<id>` - Delete a movie

## Database

The application uses SQLite for data storage. The database file `movies.db` will be created automatically on first run.
