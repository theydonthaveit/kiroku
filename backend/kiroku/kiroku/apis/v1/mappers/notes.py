from kim import field

from .base import BaseMapper

from kiroku.models import Note


class NoteMapper(BaseMapper):

    __type__ = Note

    title = field.String()
    content = field.String()