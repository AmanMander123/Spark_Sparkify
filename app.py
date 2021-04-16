from flask import Flask
from flask import render_template, request
from pyspark.ml.pipeline import PipelineModel
from pyspark.sql import Row
from pyspark import SparkContext
from pyspark import SQLContext
sc = SparkContext()
sqlContext = SQLContext(sc)

persistedModel = PipelineModel.load('dtmodel')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# web page that handles user query and displays model results
@app.route('/go',methods=['POST'])
def predict():
    if request.method == 'POST':
        days_active = request.form['days_active']
        length = request.form['length']
        unique_songs = request.form['unique_songs']
        total_songs = request.form['total_songs']
        gender = request.form['gender']
        latest_level = request.form['latest_level']

        feature_vector = [(int(days_active), int(length), int(unique_songs), int(total_songs), gender, latest_level)]

        rdd = sc.parallelize(feature_vector)
        obs = rdd.map(lambda x: Row(days_active=x[0], length=x[1], unique_songs=x[2], total_songs=x[3], gender=x[4],
                                    latest_level=x[5]))
        test = sqlContext.createDataFrame(obs)
        predictionsDF = persistedModel.transform(test)
        result = predictionsDF.select('prediction').collect()
        row = result[0]
        prediction = row.asDict()['prediction']
        if prediction == 1:
            my_prediction = 'Risk of Churning'
        else:
            my_prediction = 'Not at Risk of Churning'



    # This will render the go.html Please see that file.
    return render_template(
        'go.html',
        classification_result=my_prediction
    )
