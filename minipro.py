from apify_client import ApifyClient
import pandas as pd

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_Zik2KvK6vqgvCSh4uB2W1jT5LiyfXf3EU9C6")  # Replace with your actual API token

# Prepare the Actor input
run_input = {
    "position": "web developer",
    "country": "IN",
    "location": "BANGALORE",  # Corrected spelling
    "maxItems": 6,
    "parseCompanyDetails": True,
    "saveOnlyUniqueItems": True,
    "followApplyRedirects": True,
}

try:
    # Run the Actor and wait for it to finish
    run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)

    # Fetch and store Actor results from the run's dataset
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    # Check if items were found
    if not items:
        print("No items found.")
    else:
        # Convert items to a DataFrame
        df = pd.DataFrame(items)

        # Save the DataFrame to an Excel file
        file_name = 'job_listings.xlsx'
        df.to_excel(file_name, index=False)

        print(f"Data saved to {file_name}")

except Exception as e:
    print(f"An error occurred: {e}")
