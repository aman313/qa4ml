from flask_sqlalchemy import SQLAlchemy
from sandman2 import get_app, db
import src
import src.models as models
import inspect
from flask_sqlalchemy.model import DefaultMeta
from src import __all__
print(__all__)
from src.constants import database_uri

def create_feature_report(dataset_id):
    return 'Report Created'

def add_nonCrudServices(app):
    app.add_url_rule('/feature_report/<int:dataset_id>','create_feature_report',create_feature_report)
    return app


def main():
    user_models = [x[1] for x in inspect.getmembers(models) if type(x[1]) == DefaultMeta]
    app = get_app(database_uri=database_uri,user_models=user_models)
    db.create_all(app=app)
    app = add_nonCrudServices(app)
    app.config['SECRET_KEY'] = '42'
    app.run(host='localhost',port=5000,debug=True)


if __name__ == '__main__':
    #engine = src.models.Models.engine()
    #Base.metadata.create_all(engine)
    main()