#nick deChant
#6-4-2020
#This is a program that queries a MongoDB petsitters database in the 'vendors' collection,
#returns any matching cities and businesses, and prints each result in a .csv file.
#User must enter: a MongoDB connection string, the breed type, country, region, and filename to print to.

import argparse

#gather user input to search the query
parser = argparse.ArgumentParser()
parser.add_argument("connectionString", help="Please enter a MongoDB connection string")
parser.add_argument("breed", help="Breed to search")
parser.add_argument("country", help="Country to search")
parser.add_argument("region", help="Region to search")
parser.add_argument("filename", help="File to save")
args = parser.parse_args()

from pymongo import MongoClient

#login to your MongoDB connection
client = MongoClient(args.connectionString)

filter={
    'pet_breeds_handled': args.breed, 
    'address.country': args.country,
    'address.region': args.region    
}

#header for csv file
f = open(args.filename, "w")
f.write(f"Business name, City\n")

#results gathered into a "result" array
result = client['petsitters']['vendors'].find(
  filter=filter
)

#dummy variable for testing results
query_returned = False

#for all searches found, print out the business name and city
for item in result:
    query_returned = True #If true, we will skip the error message if statement below
    name = item['business_name']
    city = item['address']['city']
    f.write(f"{name},{city}\n")

if query_returned == False:
    print("Error! There were no matches for your input.")

f.close()   
