from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
def validate_key_range(value):
	if value < 10000000 or value > 99999999:
		raise ValidationError("The key must be 8 number")
def validate_msg_length(value):
	if len(value) == 0:
		raise ValidationError("The message can not be empty")
	elif len(value) > 165:
		raise ValidationError("The message must be 165 long")
class msgserver(models.Model):
	Message = models.CharField(max_length=165)
	Key = models.IntegerField(validators=[validate_key_range],primary_key=True)
	def __str__(self):
		return str(self.Key) +": "+self.Message
class List(models.Model):
	def default(self, obj):
		if isinstance(obj, msgserver):
			return {'id': obj.Key, 'Message' : obj.Message}
		return json.JSONEncoder.default(self, obj)

	

