import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model_reduced.pkl')

def get_user_input():
    pet_type = input("Enter Pet Type (Dog, Cat, Rabbit, Bird): ").strip().lower().title()
    breed = input("Enter Breed (Rabbit, Parakeet, Siamese, Persian, Labrador, Poodle, Golden Retriever): ").strip().lower().title()
    age_in_months = int(input("Enter Age in Months: "))
    vaccinated = int(input("Is the pet vaccinated(0 - Not vaccinated, 1 - Vaccinated:) "))
    health = int(input("Is the pet healthy (0 - Healthy, 1 - Medical condition:)"))
    weight = int(input("Enter the weight in Kg:" ))
    size = input("How big is the pet (Small, Medium, Large): ").strip().lower().title()
    days_in_shelter = int(input("How long has the pet been already in the shelter [days]: "))
        

    return {
        'Pet_Type': pet_type,
        'Breed': breed,
        'Age_in_Months': age_in_months,
        'Vaccinated': vaccinated,
        'Health_Condition': health,
        'Weight_in_Kg': weight,
        'Size': size,
        'Days_in_Shelter': days_in_shelter,
                
    }

def preprocess_input(data):
    # Convert input dictionary to a DataFrame
    input_df = pd.DataFrame([data])

    # Converte categorical data to dummies
    input_df_encoded = pd.get_dummies(input_df, columns=['Pet_Type', 'Breed', 'Size'])

    # Ensuring all columns expected by the model are present
    expected_columns = ['Age_in_Months','Weight_in_Kg',
    'Vaccinated', 'Health_Condition', 'Days_in_Shelter', 
    'Adoption_Fee','Pet_Type_Bird', 'Pet_Type_Cat', 'Pet_Type_Dog', 'Pet_Type_Rabbit',
    'Breed_Golden Retriever', 'Breed_Labrador', 'Breed_Parakeet', 
    'Breed_Persian', 'Breed_Poodle', 'Breed_Rabbit', 'Breed_Siamese', 
    'Size_Large', 'Size_Medium', 'Size_Small']

    for col in expected_columns:
        if col not in input_df_encoded.columns:
            input_df_encoded[col] = False
    
    # Reorder columns to match the expected structure
    input_df_encoded = input_df_encoded[expected_columns]
    
    return input_df_encoded

def predict(input_data):
    # Perform prediction using the loaded model
    # Convert DataFrame to NumPy array
    input_array = input_data.to_numpy()
    # Perform prediction using the loaded model
    prediction = model.predict(input_array)
    return prediction

def main():
    # Get user input
    user_input = get_user_input()

    # Preprocess input data
    input_data = preprocess_input(user_input)

    # Make prediction
    prediction = predict(input_data)

    # Display prediction result
    if prediction == 1:
        print("Prediction: The pet is likely to be adopted.")
    else:
        print("Prediction: The pet is unlikely to be adopted.")

if __name__ == "__main__":
    main()
