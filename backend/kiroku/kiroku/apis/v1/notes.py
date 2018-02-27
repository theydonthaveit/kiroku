from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin, DBCreateMixin

from kiroku.models import db, Note
from .mappers import NoteMapper

notes_resource = Resource('notes', __name__, url_prefix='/notes')


class NotesIndexEndpoint(KimEndpoint, DBListMixin, DBCreateMixin):

    name = 'list'
    many = True
    mapper_class = NoteMapper
    model = Note

    def get_query(self):

        stmt = db.session.query(Note)
        return stmt

notes_resource.add_endpoint(NotesIndexEndpoint)