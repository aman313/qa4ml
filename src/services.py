class ModelMonitoringRegistrationService():
    pass


class ModelMonitoringService():


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

class DatasetCreationService():
    pass

class ResampledDatasetCreationService():
    pass

class AugmentedDatasetCreationService():
    pass