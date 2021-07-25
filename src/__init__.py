from sqlalchemy.ext.declarative import declarative_base
import src.models as models
import inspect
from flask_sqlalchemy.model import DefaultMeta

#Base = declarative_base()

__all__ = [x[0] for x in inspect.getmembers(models) if type(x[1]) == DefaultMeta]
#print(__all__)