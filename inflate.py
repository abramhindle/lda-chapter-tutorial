import json
import sys
data = json.load(file(sys.argv[1]))
docs = [x['doc'] for x in data['rows']]
odocs = []
id = 0
for idoc in docs:
	for i in range(1,4):
		doc = idoc.copy()
		doc["comment"] = doc["comments"];
		del(doc["comments"])
		for comment in doc["comment"]:
			comment["what"] = comment.get("body","")
			comment["when"] = comment.get("created_at","")
		doc["description"] = doc.get("content","")
		doc["bugid"] = id #doc["number"]
		doc["_id"] = id #doc["number"]
		doc["openedDate"] = doc["created_at"]
	        id = id + 1
		odocs.append(doc)
	
json.dump(odocs,sys.stdout)
