from src.models import SupervisedProblemType


class ProductionDemoConfig():

    def __init__(self, config_dict):
        self.config_dict = config_dict


def create_request(resource_name, json_body):
    pass


def problemCreationDemo():
    def validate_type(typ):
        if typ in set([SupervisedProblemType.CLASSIFICATION, SupervisedProblemType.GENERATION, SupervisedProblemType.REGRESSION, SupervisedProblemType.SEGMENT_CLASSIFiCATION]):
            return
        raise Exception('Invalid type passed ' + typ)

    print('Enter Problem Name:')
    name = input()
    print('Select Problem type: (classification/regression/segmentation/generation)')
    typ = input()
    validate_type(typ)
    print('Enter a description for the problem: ')
    description = input()
    problem_create_json = {''}





def datasetCreationDemo():
    pass

def problemCaseAndCaseIdentifierCreationDemo():
    pass

def datasetReportDemo():
    pass

def modelCreationDemo():
    pass

def runProductionMonitoringDemo(production_demo_config:ProductionDemoConfig):
    #setup

    #create ML Problem


    #create Supervised Dataset1

    #Create input Scenarios and identifier criterion


    #Display dataset report


    #Create Performance criterion for input scenarios

    #Register model for monitoring

    #Start monitor for registered models

    #start simulator for ingestion of new labelled training and test data

    #teardown
    pass


def runExperimentMonitoringDemo():
    pass
