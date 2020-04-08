from app import create_app, db
import os
from flask_migrate import Migrate
from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db)


# cmd 启动示例
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
