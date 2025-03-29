import requests

social_media_sites = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "TikTok": "https://www.tiktok.com/@{}"
}

def check_username(username):
    found_profiles = {}

    for platform, url in social_media_sites.items():
        profile_url = url.format(username)
        response = requests.get(profile_url)

        if response.status_code == 200:  
            found_profiles[platform] = profile_url

    return found_profiles

username = input("Enter username: ")
profiles = check_username(username)

if profiles:
    print("Username accounts found:")
    for platform, url in profiles.items():
        print(f"{platform}: {url}")
else:
    print("Username not found on social accounts.")
