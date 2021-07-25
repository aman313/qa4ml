import enum

from sandman2.model import db, Model

from src.constants import max_text_len, max_name_len
from sqlalchemy import Text


class MLModel(db.Model,Model):
    id = db.Column(db.Integer,primary_key=True)
    train_dataset_id = db.Column(db.Integer,db.ForeignKey('dataset.id'))
    train_dataset = db.relationship('Dataset',back_populates='models')
    model_prediction_endpoint =  db.Column(db.String(max_name_len))


class Dataset(db.Model,Model):
    id = db.Column(db.Integer,primary_key=True)
    models = db.relationship('MLModel',back_populates='train_dataset')
    ml_problem_id = db.Column(db.Integer,db.ForeignKey('ml_problem.id'))
    ml_problem = db.relationship('MLProblem',back_populates='datasets')
    is_labelled = db.Column(db.Boolean)
    is_training = db.Column(db.Boolean)
    dataset_location = db.Column(db.String(max_name_len))
    dataset_io_class_name = db.Column(db.String(max_name_len))


class ModelTrainingEvent(db.Model,Model):
    pass


class ModelBatchInferenceEvent(db,Model,Model):
    pass


class DatasetReport(db.Model,Model):
    pass


class PerformanceReport(db.Model,Model):
    pass


class MLProblem(db.Model,Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(max_name_len), nullable=False)
    description = db.Column(Text(max_text_len))
    datasets  = db.relationship('Dataset',back_populates='ml_problem')
    problem_cases = db.relationship('ProblemCase', back_populates = 'ml_problem')
    class SupervisedProblemType(enum.Enum):
        CLASSIFICATION = 'classification'
        REGRESSION = 'regression'
        SEGMENT_CLASSIFiCATION = 'segmentation'  # This could be sequence tagging, segmentation, extraction etc.
        GENERATION ='generation'

    problem_type = db.Column(db.Enum(SupervisedProblemType))


class ProblemCase(db.Model,Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(max_name_len), nullable=False)
    description = db.Column(Text(max_text_len))
    detection_criterion = db.relationship('CaseDetectionCriterion',back_populates='problem_case')
    ml_problem_id = db.Column(db.Integer,db.ForeignKey('ml_problem.id'))
    ml_problem = db.relationship('MLProblem',back_populates='problem_cases')



class PerformanceCriterion(db.Model,Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(db.String(max_name_len)),nullable=False)
    description = db.Column(db.Text(max_text_len))


class CaseDetectionCriterion(db.Model,Model):
    id = db.Column(db.Integer,primary_key=True)
    problem_case_id = db.Column(db.Integer,db.ForeignKey('problem_case.id'))
    problem_case = db.relationship('ProblemCase',back_populates='detection_criterion')
    function_name = db.Column(db.String(max_name_len))
