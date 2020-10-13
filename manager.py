from flask import Flask
import os
from config import db,app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.category import Category
from models.items import Items


migrate = Migrate(app, db)
app.app_context().push()
db.init_app(app)
db.create_all(app=app)
db.session.commit()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
   manager.run()
