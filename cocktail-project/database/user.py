from tortoise import fields
from tortoise.models import Model

class User(Model):
  id = fields.IntField(pk=True)
  cardUID = fields.CharField(unique=True, max_length=255, nullable=False)
  username = fields.TextField(max_length=50)
  created_at = fields.DatetimeField(auto_now_add=True)

  class Meta:
    table = 'users'
