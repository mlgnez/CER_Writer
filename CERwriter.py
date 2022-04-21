import requests

#------------------------------------

claim = input("Claim: " + "")

evidence = input("Evidence: " + "")

reasoning = input("Reasoning: " + "")

#------------------------------------

r = requests.post("https://api.deepai.org/api/text-generator", data={'text':claim}, headers={'api-key': 'PUT API KEY HERE'})

r2 = requests.post("https://api.deepai.org/api/text-generator", data={'text':evidence}, headers={'api-key': 'PUT API KEY HERE'})

r3 = requests.post("https://api.deepai.org/api/text-generator", data={'text':reasoning}, headers={'api-key': 'PUT API KEY HERE'})


fp = open('CER.txt', 'x')
fp.write("Claim: \n")
fp.write(r.text + "\n")
fp.write("Evidence: \n")
fp.write(r2.text + "\n")
fp.write("Reasoning: \n")
fp.write(r3.text + "\n")
fp.close()
