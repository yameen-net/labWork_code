import requests
def black_box_recon(url):
    try:
        response = requests.head(url)
        print("Black Box Findings:")
        print(f"Server: {response.headers.get('Server', 'Unknown')}")
        print(f"Content-Type: {response.headers.get('Content-Type',
'Unknown')}")
    except Exception as e:
        print(f"Error: {e}")

url = "http://python.org"
known_info = {"server": "Apache 2.4", "vulns": "Check CVE-2021-1234"}
black_box_recon(url)