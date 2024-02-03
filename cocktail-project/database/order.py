from tortoise import fields
from tortoise.models import Model
from database.user import User
from database.recipe import Recipe

class Order(Model):
  id = fields.IntField(pk=True)
  quantity = fields.SmallIntField(default=1, nullable=False)
  created_at = fields.DatetimeField(auto_now_add=True)
  user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField('models.User', related_name='orders')
  recipe: fields.ForeignKeyRelation[Recipe] = fields.ForeignKeyField('models.Recipe', related_name='orders')

  class Meta:
    table = 'orders'