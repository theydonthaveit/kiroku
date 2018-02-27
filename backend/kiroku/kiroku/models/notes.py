from .base import db, BaseMixin

__all__ = ['Note']


class Note(BaseMixin, db.Model):

    __tablename__ = 'note'

    title = db.Column(db.Unicode(255), nullable=False)
    content = db.Column(db.Unicode(10000), nullable=False)