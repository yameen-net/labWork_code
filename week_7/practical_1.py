import socket
import requests
def get_domain_info(domain):
    try:
        # Get IP address (active but low-risk)
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")

        # Get public WHOIS-like info (passive, using a free API)
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        if response.status_code == 200:
            data = response.json()
            print(f"Organization: {data.get('org', 'Unknown')}")
            print(f"City: {data.get('city', 'Unknown')}")
            print(f"Country: {data.get('country_name', 'Unknown')}")
        else:
            print("Could not fetch WHOIS data.")
    except Exception as e:
        print(f"Error: {e}")
# Example: Use a public domain (
get_domain_info("142.251.30.190")