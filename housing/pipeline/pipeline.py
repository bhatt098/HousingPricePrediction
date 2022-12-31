from housing.exception import HousingException
from housing.entity.config_entity import*
from housing.config.configuration import*
from housing.entity.artifact_entity import*
from housing.component.data_ignestion import*
from housing.component.data_validation import*


import sys


class Pipeline:
    def __init__(self,config:Configuration=Configuration()) -> None:
        try:
            self.config=config
        except Exception as e:
            raise HousingException(e,sys)

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.ingested_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys)
    
    
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation=DataValidation(self.config.get_data_validation_config(),data_ingestion_artifact)
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise HousingException(e,sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_ingestion_validation=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)

        except Exception as e:
            raise HousingException(e,sys)        