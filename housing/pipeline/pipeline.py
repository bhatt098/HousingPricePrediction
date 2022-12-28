from housing.exception import HousingException
from housing.entity.config_entity import *
from housing.config.configuration import *
from housing.entity.artifact_entity import *


class Pipeline:
    def __init__(self,config:Configuration=Configuration()) -> None:
        try:
            self.config=config
        except Exception as e:
            raise HousingException(e,sys)

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            DataIngestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return DataIngestion.ingested_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys)

    def run_pipline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys)        