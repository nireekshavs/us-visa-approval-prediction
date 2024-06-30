import os
import sys
from pathlib import Path
from us_visa.exception import USvisaException
import shutil
from us_visa.logger import logging


class FileEstimator:
    def __init__(self,model_path):
        """
        param model_path: Location of your model
        """
        self.model_path = Path(f"{model_path}")

    def is_model_present(self,model_path):
        try:
            if self.model_path.exists():
                return True
        except USvisaException as e:
            print(e)
            return False
    def save_model(self,from_file,remove:bool=False)->None:
        """
        Save the model to the model_path
        """
        try:

            jj = os.path.join("usvisa-model2024")
            #jj = Path("C:\\Users\\Nireeksha\\Desktop\\projects\\model_list")
            os.makedirs(jj, exist_ok=True)
            logging.info("FFFFFFFFFFFFFFFFFFFFFFFFFFf")
            logging.info(jj)
            logging.info(from_file)
            shutil.copy(from_file,jj)
            logging.info("Done")
            
        except Exception as e:
            raise USvisaException(e, sys)
