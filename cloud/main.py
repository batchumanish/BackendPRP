from pymongo import MongoClient

client=MongoClient('mongodb+srv://manishbatchu:Q7h5KtERcGZdfJ4E@manishcluster.71tedsw.mongodb.net/')

db=client.get_database('manishclouddb')

records=db.restdata

print(records.count_documents({}))
