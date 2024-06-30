from flask import Flask, request, jsonify
from us_visa.pipline.training_pipeline import TrainPipeline
from us_visa.pipline.prediction_pipeline import USvisaData, USvisaClassifier
app = Flask(__name__)

@app.route("/train",methods=['GET'])
def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return ("Training successful !!")

    except Exception as e:
        return (f"Error Occurred! {e}")
    
@app.route('/predict', methods=['POST'])
def predictRouteClient():
    try:
        content = request.json
        usvisa_data = USvisaData(
                                    continent= content['continent'],
                                    education_of_employee = content['education_of_employee'],
                                    has_job_experience = content['has_job_experience'],
                                    requires_job_training = content['requires_job_training'],
                                    no_of_employees= content['no_of_employees'],
                                    company_age= content['company_age'],
                                    region_of_employment = content['region_of_employment'],
                                    prevailing_wage= content['prevailing_wage'],
                                    unit_of_wage= content['unit_of_wage'],
                                    full_time_position= content['full_time_position'],
                                    )
        usvisa_df = usvisa_data.get_usvisa_input_data_frame()

        model_predictor = USvisaClassifier()

        value = model_predictor.predict(dataframe=usvisa_df)[0]

        status = None
        if value == 0:
            status = "Visa-approved"
        else:
            status = "Visa Not-Approved"

        return status
    except Exception as e:
        return {"status": False, "error": f"{e}"}

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)