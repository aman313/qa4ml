import json
from typing import List

from src.models import Dataset, DataPoint, EDASummary, Prompt, FoundationModelAPIWrapper
from src.operations import Sampler, Summarizer, DatasetReader, SubsetCreator, RandomSampler, \
    PromptBasedSubsetCreatorFromCriteriaCreator, PromptBasedCaseDetectionCriteriaCreator, DisasterTweetDatasetReader, \
    SubsetCountSummarizer
from src.services.services import BaseService


class EDAService(BaseService):

    def run_eda(self, dataset:Dataset):
        raise NotImplementedError

class SubsetSummaryEDAService(EDAService):

    def __init__(self, sampler:Sampler, subset_creator:SubsetCreator,
                 summarizer:Summarizer, dataset_reader:DatasetReader):
        self._sampler = sampler
        self._subset_creator = subset_creator
        self._summarizer = summarizer
        self._dataset_reader = dataset_reader


    def run_eda(self, dataset_location:str)->EDASummary:
        return self._summarizer(self._subset_creator(self._sampler(self._dataset_reader(dataset_location))))


if __name__ == '__main__':
    dataset_location = '/media/aman/8a3ffbda-8a36-45f9-b426-d146a65d9ece/data1/qa4ml/demo_data/disaster_dataset/train.csv'
    prompt_file_location = '/media/aman/8a3ffbda-8a36-45f9-b426-d146a65d9ece/data1/qa4ml/src/prompt.json'
    openai_api_file_location = '/media/aman/8a3ffbda-8a36-45f9-b426-d146a65d9ece/data1/qa4ml/src/opeai_param.json'
    sampler = RandomSampler(0.01,seed=42)
    reader = DisasterTweetDatasetReader()
    prompt = Prompt.load_from_file(prompt_file_location)
    subset_criteria_creator = PromptBasedCaseDetectionCriteriaCreator(prompt)
    api_wrapper = FoundationModelAPIWrapper(json.load(open(openai_api_file_location)))
    subset_creator = PromptBasedSubsetCreatorFromCriteriaCreator(subset_criteria_creator,api_wrapper)
    summarizer = SubsetCountSummarizer(verbose=True)
    service = SubsetSummaryEDAService(sampler,subset_creator,summarizer,reader)
    summary = service.run_eda(dataset_location)
    print(summary)