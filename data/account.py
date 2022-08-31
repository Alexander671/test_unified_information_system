import mongoengine
from mongoengine import Document, StringField, DateTimeField, ListField, EmbeddedDocumentField, EmbeddedDocument

class Action(EmbeddedDocument):
    type = mongoengine.StringField()
    created_at = mongoengine.DateTimeField()

class Session(EmbeddedDocument):
    created_at = DateTimeField()
    session_id = StringField()
    actions = ListField(EmbeddedDocumentField(Action))

class Account(Document):
    number = StringField()
    name = StringField()
    sessions = ListField(EmbeddedDocumentField(Session))

