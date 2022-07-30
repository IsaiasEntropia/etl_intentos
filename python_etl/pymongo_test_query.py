# Get the database using the method we defined in pymongo_test_insert file 
from pymongo_test_insert import get_database
dbname = get_database()

# Create a new collection
collection_name = dbname["listingsAndReviews"]

item_details = collection_name.find()
for item in item_details:
    # This does not give a very readable output
    print(item)