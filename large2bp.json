import json
import sys
data = json.load(file(sys.argv[1]))
docs = [x['doc'] for x in data['rows']]
for doc in docs:
	doc["comment"] = doc["comments"];
	del(doc["comments"])
	for comment in doc["comment"]:
		comment["what"] = comment.get("body","")
		comment["when"] = comment.get("created_at","")
	doc["description"] = doc.get("content","")
	doc["bugid"] = doc["number"]
	doc["openedDate"] = doc["created_at"]
json.dump(docs,sys.stdout)
