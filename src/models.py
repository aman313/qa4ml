import enum
import json
from typing import Dict, Any, Union, List

from sandman2.model import db, Model

from src.constants import max_text_len, max_name_len
from sqlalchemy import Text

class FreeModel():
    pass


class MLModel(db.Model, Model):
    id = db.Column(db.Integer,primary_key=True)
    train_dataset_id = db.Column(db.Integer,db.ForeignKey('dataset.id'))
    train_dataset = db.relationship('Dataset',back_populates='models')
    model_prediction_endpoint =  db.Column(db.String(max_name_len))


class FeatureTypes(enum.Enum):
    TEXT='text'
    IMAGE='image'
    TABULAR='tabular'
    CUSTOM='custom'

class Dataset(db.Model, Model):
    id = db.Column(db.Integer,primary_key=True)
    models = db.relationship('MLModel',back_populates='train_dataset')
    ml_problem_id = db.Column(db.Integer,db.ForeignKey('ml_problem.id'))
    ml_problem = db.relationship('MLProblem',back_populates='datasets')
    is_labelled = db.Column(db.Boolean)
    is_training = db.Column(db.Boolean)
    dataset_location = db.Column(db.String(max_name_len))
    dataset_feature_fields = db.Column(db.String(max_name_len))
    dataset_label_fields = db.Column(db.String(max_name_len))
    dataset_metadata_fields = db.Column(db.String(max_name_len))
    featurtype = db.Column(db.Enum(FeatureTypes))
    #prompts = db.relationship('Prompt',back_populates ='dataset_id')



class ModelTrainingEvent(db.Model,Model):
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, )
    pass

'''
class ModelBatchInferenceEvent(db.Model,Model):
    pass


class DatasetReport(db.Model,Model):
    pass


class PerformanceReport(db.Model,Model):
    pass
'''


class SupervisedProblemType(enum.Enum):
    CLASSIFICATION = 'classification'
    REGRESSION = 'regression'
    SEGMENT_CLASSIFiCATION = 'segmentation'  # This could be sequence tagging, segmentation, extraction etc.
    GENERATION = 'generation'

class MLProblem(db.Model, Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(max_name_len), nullable=False)
    description = db.Column(Text(max_text_len))
    datasets  = db.relationship('Dataset',back_populates='ml_problem')
    problem_cases = db.relationship('ProblemCase', back_populates = 'ml_problem')
    problem_type = db.Column(db.Enum(SupervisedProblemType))


class ProblemCase(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(max_name_len), nullable=False)
    description = db.Column(Text(max_text_len))
    detection_criterion = db.relationship('CaseDetectionCriterion',back_populates='problem_case')
    ml_problem_id = db.Column(db.Integer,db.ForeignKey('ml_problem.id'))
    ml_problem = db.relationship('MLProblem',back_populates='problem_cases')



class PerformanceCriterion(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(max_name_len),nullable=False)
    description = db.Column(db.Text(max_text_len))


class CaseDetectionCriterion(db.Model, Model):
    id = db.Column(db.Integer,primary_key=True)
    problem_case_id = db.Column(db.Integer,db.ForeignKey('problem_case.id'))
    problem_case = db.relationship('ProblemCase',back_populates='detection_criterion')

class FieldValueCaseDetectionCriterion(CaseDetectionCriterion):
    __mapper_args__ = {'polymorphic_identity': 'fieldvaluecasedetectioncriterion'}
    field_names = db.Column(db.String(max_name_len))
    field_values = db.Column(db.String(max_name_len))


class DataPoint(FreeModel):
    pass

class TextClassificationDataPoint(DataPoint):
    def __init__(self, text:str, metadata:Dict=None, label:Union[str,int]=None):
        super().__init__()
        self._text = text
        self._metadata = metadata
        self._label = label

    def __repr__(self):
        return self._text

class Subset(FreeModel):

    def __init__(self, name:str, data_points:List[DataPoint]):
        self._name = name
        self._data_points = data_points

class EDASummary(FreeModel):
    pass


class PromptType(enum.Enum):
    PREFIX='prefix'
    CLOZE='cloze'

class Prompt(FreeModel):

    def __init__(self, prompt_type:PromptType, prompt_text:str, problem_type:SupervisedProblemType=None, aug_suffix:str=''):
        self._prompt_type = prompt_type
        self._prompt_text = prompt_text
        self._problem_type = problem_type
        self._aug_suffix = aug_suffix

    @staticmethod
    def load_from_file(prompt_file_path:str):
        with open(prompt_file_path) as pfp:
            dct = json.load(pfp)
            return Prompt(**dct)

    def augment_text(self, data_point:TextClassificationDataPoint):
        return self._prompt_text + data_point._text + self._aug_suffix


class PromptBasedCaseDetectionCriterion(FreeModel):

    def __init__(self, prompt:Prompt):
        self._prompt = prompt

class FoundationModelAPIWrapper(FreeModel):

    def __init__(self, api_details:Dict):
        self._api_details = api_details


