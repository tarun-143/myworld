import requests

def main():
	res=requests.get("http://data.fixer.io/api/latest?access_key=a3112cc1d4a2add5e2cfa9a9a1914484&symbols=INR,USD&format=1")
	if  res.status_code!=200:
		raise Exception("ERROR:API request unsuccessful")
	data=res.json()
	print(data)


if __name__ == '__main__':
	main()