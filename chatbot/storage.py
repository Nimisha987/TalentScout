import json
FILE_PATH="data/candidates.json"
def save_candidate(data):
    try:
        with open(FILE_PATH,"r") as f:
            existing=json.load(f)
    except:
        existing=[]
    existing.append(data)
    with open(FILE_PATH,"w") as f:
        json.dump(existing,f,indent=4)