from Housing.logger import logging
from Housing.exception import HousingException
from Housing.entity.config_entity import DataValidationConfig
from Housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import sys,os
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset,TargetDriftPreset
import json
class DataValidation:
    
    def __init__(self, data_validation_config:DataValidationConfig,
                data_ingestion_artifact):
        try:
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
    def get_train_and_test_df(self):
        try:
            train_df=pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df=pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise HousingException(e,sys) from e        
    
    def is_train_test_file_exists(self):
        try:
            logging.info("Checking if train and test file is exists")
            is_train_file_exist=False
            is_test_file_exist=False
            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            is_train_file_exist=os.path.exists(train_file_path)
            is_test_file_exist=os.path.exists(test_file_path)

            is_available=is_test_file_exist and is_train_file_exist

            logging.info(f"Is train and test file exists?-> {is_available}")
            if not is_available:
                training_file=self.data_ingestion_artifact.train_file_path
                testing_file=self.data_ingestion_artifact.test_file_path
                message=f"Training file: {training_file} or Testing file: {testing_file} is not present"
                logging.info(message)
                raise Exception(message)
            return is_available

        except Exception as e:
            raise HousingException(e,sys) from e

    
    def validate_dataset_schema(self)->bool:
        try:
            validation_status=False

            validation_status=True
            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_save_data_drift_report(self):
        try:
            profile=Report(metrics=[DataDriftPreset(),TargetDriftPreset()])
            train_df,test_df=self.get_train_and_test_df()

            profile.run(reference_data=train_df,current_data=test_df)

            report=json.loads(profile.json())
            report_file_path=self.data_validation_config.report_file_path
            report_dir=os.path.dirname(report_file_path)
            os.makedirs(report_dir,exist_ok=True)


            with open(report_file_path,"w") as report_file:
                json.dump(report,report_file,indent=6)
            return report
        except Exception as e:
            raise HousingException(e,sys) from e
    def save_data_drift_report_page(self):
        try:
            dashboard=Report(metrics=[DataDriftPreset(),TargetDriftPreset()])
            train_df,test_df=self.get_train_and_test_df()
            dashboard.run(reference_data=train_df,current_data=test_df)

            report_page_file_path=self.data_validation_config.report_page_file_path
            report_page_dir=os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)

            dashboard.save_html(report_page_file_path)
        except Exception as e:
            raise HousingException(e,sys) from e

    def is_data_drift_found(self)->bool:
        try:
            report=self.get_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact=DataValidationArtifact(schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation perfomed sucessfully"
            )
            logging.info(f"Data Validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

        