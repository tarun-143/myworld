import requests

def main():
	other=input("entr the other currency:")
	res=requests.get("http://data.fixer.io/api/latest?access_key=a3112cc1d4a2add5e2cfa9a9a1914484",params={"symbols":other})
	if  res.status_code!=200:
		raise Exception("ERROR:API request unsuccessful")
	data=res.json()
	rate=data["rates"][other]
	print(f"1 EUR is equal to {rate} {other}")


if __name__ == '__main__':
	main()