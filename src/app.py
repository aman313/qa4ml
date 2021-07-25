from flask_sqlalchemy import SQLAlchemy
from sandman2 import get_app, db
import src
import src.models as models
import inspect
from flask_sqlalchemy.model import DefaultMeta
from src import __all__
print(__all__)
from src.constants import database_uri

def add_nonCrudServices(app):
    return app


def main():
    user_models = [x[1] for x in inspect.getmembers(models) if type(x[1]) == DefaultMeta]
    app = get_app(database_uri=database_uri,user_models=user_models)
    db.create_all(app=app)
    app = add_nonCrudServices(app)
    app.run(host='localhost',port=5000,debug=True)


if __name__ == '__main__':
    #engine = src.models.Models.engine()
    #Base.metadata.create_all(engine)
    main()