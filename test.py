import pandas as pd
import requests
import os

df = pd.read_excel('C:/Users/Vishw/OneDrive/Desktop/testing-pandas/test.xlsx')

output_folder = 'images'
os.makedirs(output_folder, exist_ok=True)

for index, row in df.iterrows():
    image_url = row['URL']  # Replace 'URL' with the actual column name containing the URLs in your Excel file
    
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an exception if the image download fails
        
        # Extract the image file name from the URL
        image_name = image_url.split('/')[-1]

        new_image_name = image_name.split('?')[0]  # Remove the query parameters from the image file name
        
        # Save the image to the local folder
        with open(os.path.join(output_folder, new_image_name), 'wb') as f:
            f.write(response.content)
            
        print(f"Downloaded image {index + 1}/{len(df)}")
    except Exception as e:
        print(f"Error downloading image {index + 1}/{len(df)}: {str(e)}")