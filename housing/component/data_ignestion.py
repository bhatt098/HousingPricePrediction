from housing.entity.config_entity import DataIngestionConfig
from housing.entity.artifact_entity import DataIngestionArtifact

from housing.exception import*
import tarfile
from six.moves import urllib
import pandas as pd
from sklearn.model_selection import train_test_split

import os,sys

class DataIngestion:

    def __init__(self, data_ingestion_config=DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config 
        except Exception as e:
            raise HousingException(e,sys)

   
    def download_housing_data(self):
        try:
            download_url=self.data_ingestion_config.dataset_download_url
            tgz_download_dir=self.data_ingestion_config.tgz_download_dir
            os.makedirs(tgz_download_dir,exist_ok=True)

            housing_file_name = os.path.basename(download_url)

            tgz_file_path = os.path.join(tgz_download_dir, housing_file_name)

            # logging.info(f"Downloading file from :[{download_url}] into :[{tgz_file_path}]")
            urllib.request.urlretrieve(download_url, tgz_file_path)
            # logging.info(f"File :[{tgz_file_path}] has been downloaded successfully.")
            return tgz_file_path

        except Exception as e:
            raise HousingException(e,sys)


    def extract_tgz_file(self,tgz_file_path):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)
            # logging.info(f"Extracting tgz file: [{tgz_file_path}] into dir: [{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(path=raw_data_dir)
            # logging.info(f"Extraction completed")


        except Exception as e:
            raise HousingException(e,sys)


    def split_data_as_train_test(self)->DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            file_name=os.listdir(raw_data_dir)[0]
            housing_file_path=os.path.join(raw_data_dir,file_name)
            df=pd.read_csv(housing_file_path)
            print(df)
            X=df.iloc[:,:-1]   #independent
            print(X)
            y=df.iloc[:,-1]    #dependent
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir, file_name)
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir, file_name)
            # if X_train in not None:
            os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
            X_train.to_csv(train_file_path,index=False)
    
            # if X_train in not None:
            os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
            X_test.to_csv(test_file_path,index=False)

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                    test_file_path=test_file_path,
                                    is_ingested=True,
                                    message=f"Data ingestion completed successfully."
                                    )
            return data_ingestion_artifact


        except Exception as e:
            raise HousingException(e,sys)


    def ingested_data_ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path =  self.download_housing_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise HousingException(e,sys) from e
        




    




