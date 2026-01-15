from db import db

class Movie(db.Model):
    """Movie model"""
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255))
    year = db.Column(db.Integer)
    
    def to_dict(self):
        """Convert movie to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
            'year': self.year
        }
    
    def __repr__(self):
        return f'<Movie {self.title}>'
