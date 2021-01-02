import requests
import json
#url="http://oauth.dicom.org.tw/fhir/Patient"
url='http://192.168.50.3:10610/gateway/fhir/Patient'
token='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL29hdXRoLmRpY29tLm9yZy50dyIsInN1YiI6IlRDU0jlnJjpmooiLCJhdWQiOiIxNTAuMTE3LjEyMS42NyIsImlhdCI6MTYwMzA4ODQzMywiZXhwIjoxNjA2NjY1NjAwLCJqdGkiOiIwMWNhZWVmOC1hYTk1LTQzYzQtODI4My01ODE0NmE5MGFmM2IifQ.cyJOd_1r5UvNHzm0h7k2IaCQBZyP2InOq644GOjtP-0d3M53kLJtjfdtHqsgD8fQrMI8D8t5WkoGQ2VPx-uDzzgknUWx5L70tfZadsPxJvnGFoZfIXfim4GasaBndB6fMyXq22BUudslwZPuBHOgLQaU-g6kZ6sxh4_dmmrbQNe0S9L1Z7NtzsqOS_48cWZuVOZBKLkLO5zfFcxn76Ntw81QRX85-wJp8L3kNozsqMc8JCmC79sFq6kI34h3ZIx-jV5D9w8F1T6qCdCn4MuDwco9oGxeAgelnAtXGkqlbHEBoz_E2aTssHE_y-edeXe2C9kxQJA6plJsM3IG75kMnw'
f = open("patientTest.json","r",encoding="utf-8").read()
f = f.replace("\n","")
dicts = json.loads(f)

r = requests.post(url,headers={'Authorization':token},json=dicts)
print(r.json())
