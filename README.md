Steps followed to Download data from github, preprocess it, ingest it into postgres server then migrate the data to cloud.
Step 1: Download 3 csv files from the git hub using he python code which is available in github repository as download_files.py
Step 2: create 3 new tables for storing booking_data, customer_data and destination_data in postgressql.
Step 3: Preprocess the raw data by removing nulls, formatting the data and structuring the data.
Step 4: Bulk insert the preprocessed data in postgressql using the python code.
Step 5: Schedule the ingesting process daily to upload the daily booking data.
Step 6: Batch transfer the data in postgressql to cloud
Step 7: Encrypt the PII information using MD5 encryption technique.
