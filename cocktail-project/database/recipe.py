from tortoise import fields
from tortoise.models import Model

class Recipe(Model):
  id = fields.IntField(pk=True)
  name = fields.TextField(nullable=False)
  description = fields.TextField(nullable=False)
  created_at = fields.DatetimeField()
  rate_bottle_one = fields.FloatField(nullable=False)
  rate_bottle_two = fields.FloatField(nullable=False)
  rate_bottle_three = fields.FloatField(nullable=False)

  class Meta:
    table = 'recipes'