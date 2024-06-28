# %%
import json
import sqlite3

# define a function to query the NER annotation database
def query_nerdb( query,  params=(), dbpath = 'nerdb.db'):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
    return rows

#%%
# check db schema:
# query_nerdb ("select * from sqlite_master where type='table';")

# %%
# Fetch all dhlabids in the database
dhlabids = query_nerdb("select distinct dhlabid from ner_sequence;")

# %%
# Fetch all placenames from the database, in the order they appear in the text

query = "select word from ner_sequence where dhlabid=? and label like '%LOC' order by cast(paragraph as integer);"

placenames = {}
for docid in dhlabids:
    #print(docid)
    results = query_nerdb(query, docid)
    formatted = [x[0] for x in results]
    placenames[docid[0]] = formatted

# %%
# Save the placenames to a json file
with open("placenames.json", "w", encoding="utf-8") as fp:
    json.dump(placenames, fp)
