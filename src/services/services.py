class BaseService():
    pass

class ModelMonitoringRegistrationService(BaseService):
    pass

class FeatureReportService(BaseService):

    def __init__(self,report_location):
        self.report_location = report_location

    def create_report(self, dataset_id):
        pass


class ModelPerformanceReportService(BaseService):
    pass


class ModelMonitoringService(BaseService):


    def model_training_event_handler(self):
        '''
            Every time the model is trained, this event supplies the dataset on which the model is trained
            The handler creates the performance report for the problem cases.
            It also compares the problem cases in the new dataset with those in the previous dataset
        :return:
        '''
        pass

    def model_batch_inference_event_handler(self):
        '''
            Create report for data drift
            Create performance report if labelled data is available
        :return:
        '''
        pass

class DatasetCreationService(BaseService):
    pass

class ResampledDatasetCreationService(BaseService):
    pass

class AugmentedDatasetCreationService(BaseService):
    pass