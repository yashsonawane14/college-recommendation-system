#from django.shortcuts import render

# import csv
# #from django.shortcuts import render

# def csv_view(request):
#     with open('C:/Users/Yash/Desktop/clgyasuyasu/college_data.csv', 'r') as file:
#         reader = csv.reader(file)
#         first_row = next(reader)  # Get the first row
    
#     return render(request, 'college/csv_template.html', {'first_row': first_row})


# def csv_view(request):
#     with open('C:/Users/Yash/Desktop/clgyasuyasu/college_data.csv', 'r') as file:
#         reader = csv.reader(file)
#         first_row = next(reader)  # Get the first row (header)
#         second_row = next(reader)  # Get the second row (first data row)

#     context = {
#         'first_row': first_row,
#         'second_row': second_row,
#     }
#     return render(request, 'college/csv_template.html', context)


#
#


# import csv
# from django.shortcuts import render,redirect
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.neighbors import KNeighborsClassifier
# from django.shortcuts import render
# from django.http import JsonResponse

# # Load and preprocess data only once (to optimize performance)
# dataframe = pd.read_csv("C:/Users/Yash/Desktop/clgyasuyasu/college_data.csv")

# # Replace values in 'fulfillment' column
# dataframe.replace(to_replace='^', value='Admitted to Institute', inplace=True)
# dataframe.replace(to_replace='~', value='No Change', inplace=True)
# dataframe.replace(to_replace='*', value='Betterment in Choice Code', inplace=True)
# dataframe.replace(to_replace='@', value='Betterment in Seat Type', inplace=True)
# dataframe.replace(to_replace='&', value='Newly Allotted', inplace=True)

# # Replace values in 'seat_type' column
# dataframe.replace(to_replace='GOPENS', value='General Open State Level', inplace=True)
# dataframe.replace(to_replace='LOPENS', value='Ladies Open State Level', inplace=True)

# # Encode categorical columns
# label_encoder = LabelEncoder()
# categorical_columns = [
#     'fulfillment', 'seat_type', 'primary_seat_type', 
#     'secondary_seat_type', 'branch', 'gender', 
#     'category', 'score_type', 'enrollment_no', 'branch_code'
# ]
# for col in categorical_columns:
#     dataframe[col] = label_encoder.fit_transform(dataframe[col])

# # Split the data
# x = dataframe.drop(['college_name'], axis=1)
# y = dataframe['college_name']

# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)

# # Train the KNN model
# knn = KNeighborsClassifier(n_neighbors=8)
# knn.fit(x_train, y_train)

# from django.http import HttpResponse
# def home(request):
#     return render(request, 'home.html')
#     return HttpResponse("Welcome to the College Recommendation System!")

# # Define the prediction view
# def predict_college(request):
#     if request.method == 'POST':
#         # Extract input data from request
#         input_data = {
#             'rank': request.POST.get('rank'),
#             'percentile': request.POST.get('percentile'),
#             'branch': request.POST.get('branch'),
#             'gender': request.POST.get('gender'),
#             'category': request.POST.get('category'),
#             'fulfillment': request.POST.get('fulfillment'),
#             'seat_type': request.POST.get('seat_type'),
#             'primary_seat_type': request.POST.get('primary_seat_type'),
#             'secondary_seat_type': request.POST.get('secondary_seat_type'),
#             'score_type': request.POST.get('score_type'),
#             'enrollment_no': request.POST.get('enrollment_no'),
#             'branch_code': request.POST.get('branch_code'),
#         }

#         # Convert input data to a DataFrame for prediction
#         input_df = pd.DataFrame([input_data])
#         for col in categorical_columns:
#             input_df[col] = label_encoder.transform(input_df[col])

#         # Perform prediction
#         predicted_college = knn.predict(input_df)
#         return JsonResponse({'predicted_college': predicted_college[0]})

#     return JsonResponse({'error': 'Invalid request method. Use POST.'})


#
#

import csv
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

# Load and preprocess data
dataframe = pd.read_csv("C:/Users/Yash/Desktop/clgyasuyasu/college_data.csv")

# Replace values in specific columns
dataframe.replace(to_replace='^', value='Admitted to Institute', inplace=True)
dataframe.replace(to_replace='~', value='No Change', inplace=True)
dataframe.replace(to_replace='*', value='Betterment in Choice Code', inplace=True)
dataframe.replace(to_replace='@', value='Betterment in Seat Type', inplace=True)
dataframe.replace(to_replace='&', value='Newly Allotted', inplace=True)
dataframe.replace(to_replace='GOPENS', value='General Open State Level', inplace=True)
dataframe.replace(to_replace='LOPENS', value='Ladies Open State Level', inplace=True)

# Encode categorical columns
label_encoder = LabelEncoder()
categorical_columns = [
    'fulfillment', 'seat_type', 'primary_seat_type', 
    'secondary_seat_type', 'branch', 'gender', 
    'category', 'score_type', 'enrollment_no', 'branch_code'
]
for col in categorical_columns:
    dataframe[col] = label_encoder.fit_transform(dataframe[col])

# Split the data
x = dataframe.drop(['college_name'], axis=1)
y = dataframe['college_name']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)

# Train the KNN model
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train, y_train)

# View for the homepage
def home(request):
    return render(request, 'home.html')

# View for handling predictions
def predict_college(request):
    if request.method == 'POST':
        
            # Extract input data from the form
            input_data = {
                'rank': request.POST.get('rank'),
                'percentile': request.POST.get('percentile'),
                'branch': request.POST.get('branch'),
                'gender': request.POST.get('gender'),
                'category': request.POST.get('category'),
                'fulfillment': request.POST.get('fulfillment'),
                'seat_type': request.POST.get('seat_type'),
                'primary_seat_type': request.POST.get('primary_seat_type'),
                'secondary_seat_type': request.POST.get('secondary_seat_type'),
                'score_type': request.POST.get('score_type'),
                'enrollment_no': request.POST.get('enrollment_no'),
                'branch_code': request.POST.get('branch_code'),
            }

            # Convert input data to a DataFrame
            input_df = pd.DataFrame([input_data])

            # Encode categorical columns for input data
            try:
                for col in categorical_columns:
                    if col in input_df.columns:
                        input_df[col] = input_df[col].apply(
                            lambda x: label_encoder.transform([x])[0] if x in label_encoder.classes_ else -1
                        )

                # Check for invalid (-1) values
                if input_df.isin([-1]).any().any():
                    return JsonResponse({'error': 'Invalid input values. Please ensure all fields are filled correctly.'})

                # Perform prediction
                predicted_college = knn.predict(input_df)
                return JsonResponse({'predicted_college': predicted_college[0]})

            except Exception as e:
                return JsonResponse({'error': f'Error during prediction: {str(e)}'})

    # Redirect to home page if not a POST request
    return redirect('home')
