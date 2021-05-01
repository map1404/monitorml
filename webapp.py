from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('dumpfile.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template("uberwachen.html")

@app.route('/predict',methods=['POST','GET'])

def predict():
    input_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][0], 2)

    if output == str(1):
        return render_template('ubenwachen.html',
                               pred='Patient highly critical and needs immediate medical assistance\nSeriousness of the patient is {}'.format(output))
    elif (str(0.5) <=output<str(1)):
        return render_template('ubenwachen.html',
                               pred='Patient needs medical attention.\n Seriousness of the patient is {}'.format(output))
    
    elif (str(0.25)<=output<str(0.5)):
        return render_template('ubenwachen.html',
                               pred='Patient needs a medical checkup\n Seriousness of the patient is {}'.format( output))
    else:
        return render_template('ubenwachen.html',
                               pred='Patient Normal!.\n Seriousness of the patient is {}'.format(output))
if __name__ == '__main__':
    app.run(debug=True)
