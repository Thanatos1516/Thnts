import requests

def get_geolocation(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data["status"] == "success":
            print(f"\n Information about geolocation: {ip}")
            print(f"Country: {data['country']}")
            print(f"City: {data['city']}")
            print(f"Region: {data['regionName']}")
            print(f"ISP: {data['isp']}")
            print(f"Longitude: {data['lat']}")
            print(f"Server time belt: {data['timezone']}")
            print(f"AS: {data['as']}")
        else:
            print(f"There is not information about this IP: {ip}")
    except Exception as e:
        print(f" Error getting IP address: {e}")

ip_address = input("IP address: ")
get_geolocation(ip_address)
