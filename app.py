#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
from flask import request,Flask,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('BreastCancer.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    output=round(prediction[0])
    return render_template('index.html',prediction_text='Predicted Cancer is  {}'.format(output))


#@app.route("/predict_api",methods=['POST'])
#def predict_api():
 #   data = request.get_json(force=True)
 #   prediction = model.predict([np.array(list(data.values()))])
 

 #   output=prediction[0]
  #  return jsonify(output)



if __name__ == "__main__":
    app.run(port = 5000,debug=True)

