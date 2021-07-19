from flask import Flask,render_template,request
import pickle
# import xgboost
import numpy as np
# import x

model = pickle.load(open('stroke_model.pkl', 'rb'))
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/prediction_of_rain",methods=['GET','POST'])
def predict_rain():
    inputs=[]
    strokes=0
    if request.method=='POST':
        # print('NOt working')
        # print(gust_dir)
        gender=int(request.form.get('gender'))
        age=int(request.form.get('age'))
        hypertension=int(request.form.get('hypertension'))
        heart_disease=int(request.form.get('heart_disease'))
        married=int(request.form.get('married'))
        work=int(request.form.get('work'))
        recidence=int(request.form.get('recidence'))
        glucose=float(request.form.get('glucose'))
        bmi=float(request.form.get('bmi'))
        smokes=int(request.form.get('smokes'))
        inputs=[gender,age,hypertension,heart_disease,married,work,recidence,glucose,bmi,smokes]
        strokes=model.predict(inputs)
#         print(strokes)
    else:
        print('NOt working')
    return render_template('index.html',is_stroke=strokes)

if __name__=='__main__':
    app.run(debug=True)
