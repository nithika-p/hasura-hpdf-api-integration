class Response_object:
	"""docstring for Response"""
	def __init__(self, entity,value):
		self.entity = entity
		self.value = value
	def toJson(self):
		return {"Pair":{"entity":self.entity,"value":self.value}}

		