from marshmallow import Schema, fields, post_load
from dataclasses import dataclass

@dataclass
class Message:
	id: int
	from_id: int
	text: str
	date: int

class MessageSchema(Schema):
	id = fields.Integer()
	from_id = fields.Integer()
	text = fields.String()
	date = fields.Integer()

	@post_load
	def make_message(self, data, **kwargs):
	 return Message(**data)
