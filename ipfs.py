import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
	url = "https://ipfs.infura.io:5001/api/v0/add"
	headers = {
        "Authorization": "Bearer ac471cb75f1d42a7b75d168fefbd13b5"  
	}
	response = requests.post(url, headers=headers, files={"file": json_data})  
	response_data = response.json()  
	cid = response_data['Hash']

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://ipfs.infura.io:5001/api/v0/cat?arg={cid}"
	response = requests.get(url)
	data = response.json()
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
