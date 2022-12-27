from housing.constant import *
from housing.util.util import *
import sys,os
from housing.exception import *
from housing.entity.config_entity import*

class Configuration:
    def __init__(self,config_yaml_path,time_stamp):
        try:
            self.config_info=read_yaml_file(config_yaml_path)
            self.training_pipeline_config=self.get_training_pipeline_config()
            self.time_stamp=time_stamp
        except Exception as e:
            raise HousingException(e,sys)

    
    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        try:
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir=os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            # logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        
        except Exception as e:
            raise HousingException(e,sys)

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys)

    def get_data_validation_config(self) ->DataValidationConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys)

    def get_data_transformation_config(self) ->DataTransformationConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys)

    # def get_model_trainer_config(self)-> datatr

    # get_model_evaluation_config

    # get_model_pusher_config

    # get_training_pipeline_config
            