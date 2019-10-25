from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from project.models import db
from project import create_app

app = create_app('test_config.py')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
