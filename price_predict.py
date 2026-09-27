import pandas as pd
import joblib

model = joblib.load('house_price_model.pkl')

print("Model loaded successfully.")

area = pd.DataFrame({"Area": [1000, 1500, 2000]})
print(model.predict(area))

while True:
    try:
        save_choice = input("Do you want to save the model? (yes/no): ").strip().lower()

        if save_choice == "yes":
            import joblib
            joblib.dump(model, "house_price_model.pkl")
            print(" Model saved as house_price_model.pkl")
            break
        elif save_choice == "no":
            print(" Model not saved.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
    except Exception as e:
        print("Error:", e)