from msal import ConfidentialClientApplication
import requests
import json
import os

# SharePoint Credentials
client_id = "79c0491f-f179-457a-827e-249a552019ae"
cert_thumbprint= "77AB3CF024B410ACAC615617DA20B9928D47B378"
tenant_id = "fbf7e02f-e94a-4df2-a0a9-9e30f4d5cd65"

authority= f"https://login.microsoftonline.com/{tenant_id}"
private_key = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCkApQfLMu+Y/KD
0+4l9SWjRJt4F/o4luN7Q2YHTS9JvPsd+fEDFxRU/7P5dvHkkS9WElTJdjIpUoyN
PApsyF5s47zQoUIVUkJWPRpfD/CTRqeKtt6zNem1eAUsuY0VxBI9TKKZj7L+DQx3
a4bkCO1vxrHu8mjK82N+KJOxd5nU+i1U8yswzgNZZ6UpaARRo5hFW2Gard4ZjOlk
T37+SAkvsRx/MjEviEn5GCXmZplgRJwgG9ISsh04EZyTybgHwb1DTb2idwNYIAqz
BgkDFf/YX9zAykJyuBOJW8P721JuY/0dELk5WWEEPWxMkvZfO3epiRhWAtoRIDRS
YnN0BHtnAgMBAAECggEAEL6epswpBQgpQ2JIxyFPNWsUwF8aUdq94ODRst8je9DK
hpX1EE6z6bWth0OokKBuB8iZVXQ2zNc7uFOv8MlIMq/RoC9GkuyyDyHv5lK3SiIF
ivj+padUdA2L4bQT/mvlPNLtKuZr7NoiMrMMs41hyG6tzep73nSY7NFxusWuM/so
+78g5cOdUmfVSN7lmOgc9ydZNfZ2t7Ge6/GKnmpwt+jRmbK+NQ3xRKFTSPLZUIaP
YIahJfR+eSt0FHfPAcenabwRXNVYukLoGmSLqikq7PFfScAHV69qQc5UmwgjdSOM
MtQ93ZG+1UvRlAu+cGW04gEXI52/r/ml53g+7j7FoQKBgQDPXi8KorkI5XF09b25
OpIK4hpsjGyeOCx+xBajhg0ORTPUCiDf22RkoveP9GeQL2u5hzovJtqfZuRGyAfE
OWg0KkwbrohCzCP49pcf6kqMZEnbb+PA+Y18cqmCR7drUkaR9xjvR9wbyKdbok5c
j6DVIIYzQFzhjVNFcwX8hqx/0QKBgQDKeU5gHAvoR05QUEbpzTLrkxExw1C4DNPT
DhaN9LBlYZLEDoRLLS959Ltj7bS5Z1WxsnoxYWQojDJMp5sZlbL7GUF8RSukImZr
SsZysTr6AskhmmLsxCp6RSkAQ726mjiIQAGiKOe7zMwrh3BQWH527fFxUemkRq+X
jtFCEh+NtwKBgBlGbY1qUAtZi/6phTpyfSJ+dKIOa57NUf8Rf4Dm8ehvXuXVZjRi
1VW+11XggE7+uK6gYOMmZTdQnzpRX0D3jk/tZ+Fn4Ivjve62f60QLY33G1l3xdbb
k/c7MpYCj8Sw/pEEATIJHDb2ug9dNRfrGbtgf3r3uVp0k1W/s1cYQyZBAoGAHxk2
sohcQ9b/7lIGMk70LT6ve2c2dK5zso0NZcxZc5jjA/3+z9Um36J5TcXq5jc68Eor
fn4o9hlieGed6PYXQX4FkuLE6zblaEFZ7a/PEStwXRrratZOd+07ePDuqUSavkKm
fZOu1CeGjIEG/TA6bGXrma4tJrA8tBiZh35lHk0CgYEAu/mqt3Y4FqjVQlIIV0uu
Mh55mOdGGZ1WiHMAzb80HgxKhbd1DaDi/Gd2MHf2aSmdJmwk/KuGFO38ehv4zdo3
w5OtNZ2d5R7CH5z7tmIELkFBq0ezGeEjTGZeqHGar04FqzvSacnoHEAqgH7l1NDr
NkXlZwSo3PLI0yDWL6RTRn8=
-----END PRIVATE KEY-----
"""

# Authentication
cert = {
    "private_key": private_key,
    "thumbprint": cert_thumbprint
}

msal_app = ConfidentialClientApplication(
    client_id=client_id,
    authority=authority,
    client_credential=cert
)

scopes_sharepoint_online = ["https://data03.sharepoint.com/.default"]
result = msal_app.acquire_token_for_client(scopes_sharepoint_online)

if "access_token" in result:
    access_token = result["access_token"]
else:
    raise Exception("Failed to authenticate to SharePoint")

headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json;odata=verbose"
}

sharepoint_base_url = "https://data03.sharepoint.com/sites/WorkforceProjectReporting"
document_library = "PowerBI_Equans_Data"  # Change to the correct document library name
upload_folder = "Live_Logs"  # Target folder in SharePoint
#file_path = "requirements.txt"  # Local path to the CSV file

# Upload function
def upload_file_to_sharepoint(file_path, document_library, upload_folder):
    file_name = os.path.basename(file_path)
    upload_url = f"{sharepoint_base_url}/_api/web/getfolderbyserverrelativeurl('{document_library}/{upload_folder}')/files/add(url='{file_name}',overwrite=true)"
    
    with open(file_path, "rb") as file_content:
        response = requests.post(upload_url, headers=headers, data=file_content)
    
    if response.status_code == 200 or response.status_code == 201:
        print(f"File '{file_name}' uploaded successfully to {document_library}/{upload_folder}.")
    else:
        print(f"Failed to upload file: {response.status_code}")
        print(response.text)
# Upload the file
#upload_file_to_sharepoint(file_path, document_library, upload_folder)
