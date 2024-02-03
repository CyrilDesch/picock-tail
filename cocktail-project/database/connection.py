from tortoise import Tortoise
from config import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT

async def initDatabase():
  await Tortoise.init(config={
    'connections': {
      'default': {
        'engine': 'tortoise.backends.mysql',
        'credentials': {
          'host': DB_HOST,
          'port': DB_PORT,
          'user': DB_USER,
          'password': DB_PASSWORD,
          'database': DB_NAME,
        }
      },
    },
    "apps": {
      "models": {
        "models": ["database.order", "database.recipe", "database.user"],
        'default_connection': 'default',
      }
    }
  })
