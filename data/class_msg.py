from marshmallow import Schema, fields, post_load

class Message:
	def __init__(self, id, from_id, text, date):
		self.id = id
		self.from_id = from_id
		self.text = text
		self.date = date

class MessageSchema(Schema):
	id: fields.Integer()
	from_id: fields.Integer()
	text: fields.String()
	date: fields.Integer()

	@post_load
	def make_message(self, data, **kwargs):
	 return Message(**data)
