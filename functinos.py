# Mapping: {'France': 0, 'Germany': 1, 'Spain': 2} 
# Mapping: {'Female': 0, 'Male': 1}
# functions
import joblib 

geography_dic = {'France': 0, 
            'Germany': 1, 
            'Spain': 2
            }

gender_dic = {'Female': 0, 
              'Male': 1
              }

scaler = joblib.load("Models\scaler.pkl") 
model = joblib.load(r"Models\rf_churn_prediction86_v1.pkl")

def encode_geography(geography) : 
    return geography_dic[geography] 

def encode_gender(gender) : 
    return gender_dic[gender] 


def scaling(x) : 
    x_scaled = scaler.transform([x])
    return x_scaled 

def model_predict(x) :  
    predicted_value = model.predict(x)
    return predicted_value[0]

sc = scaling([619.0	,0,0,42,2,0.00 ,1 ,1 ,1,101348.88])
print(model_predict(sc))