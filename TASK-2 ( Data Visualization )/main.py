import requests
import pandas as pd

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data from the API. Status code: {response.status_code}")
        return None

def create_dataframe(data):
    if data is not None:
        df = pd.DataFrame(data)
        return df
    else:
        return None

def save_to_csv(dataframe, file_name):
    if dataframe is not None:
        dataframe.to_csv(file_name, index=False)
        print(f"Data saved to {file_name}")
    else:
        print("No data to save")

def main():
    # API URL to fetch data
    api_url = 'https://api.slingacademy.com/v1/sample-data/files/student-scores.json'

    # Fetch data from the API
    data = fetch_data_from_api(api_url)

    # Process the data
    df = create_dataframe(data)

    # Save the processed data to a CSV file
    if df is not None:
        save_to_csv(df, 'dataset.csv')

if __name__ == "__main__":
    main()
