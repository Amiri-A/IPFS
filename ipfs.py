import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIzMWY1OTc1OS1iY2Y1LTRiOTQtYWVhMy1lYmZkNGYxNzM2ZDQiLCJlbWFpbCI6ImFtaXJpYUBzZWFzLnVwZW5uLmVkdSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiJhOTUwNzhlYWUwM2U2ZmYzMTNjNSIsInNjb3BlZEtleVNlY3JldCI6ImNiNjFjYWUyNzcyYzk4NDMyOTkxZDI1OGU0OGMzNTJkOGM1ZDQ1ZTdhZjU0Nzk2MjQ5YTdkY2U4YmViMTM1YTAiLCJleHAiOjE3NzMyNTA5Mzd9.5nibkR6HtrxIuAgKowwMxhziptJFW0w_bqmKotcqe2U"  
	}
	response = requests.post(url, headers=headers, files={"file": json_data})  
	response_data = response.json()  
	cid = response_data['IpfsHash']

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://ipfs.infura.io:5001/api/v0/cat?arg={cid}"
	response = requests.get(url)
	data = response.json()
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
