from Housing.pipeline.pipeline import Pipeline
from Housing.exception import HousingException
from Housing.logger import logging
from Housing.config.configuration import Configuration
from Housing.component.data_transformation import DataTransformation
def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
        #data_validation_config=Configuration().get_data_transformation_config()
        #print(data_validation_config)
        #schema_file_path=r"C:\Users\cscrs\OneDrive\Documents\Machine Learning\Machine-Learning-Project\config\schema.yaml"
        #file_path=r"C:\Users\cscrs\OneDrive\Documents\Machine Learning\Machine-Learning-Project\Housing\artifact\data_ingestion\2023-06-19-14-41-13\ingested_data\train\housing.csv"
        #df=DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()