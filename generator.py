#python
import requests
import time

def follow_instagram(username):
    # Make a request to follow the Instagram account
    url = f"https://instagram.com/{username}/follow"
    response = requests.post(url)
    
    if response.status_code == 200:
        print(f"Successfully followed {username} on Instagram!")
    else:
        print(f"Failed to follow {username} on Instagram!")

def main():
    username = input("Please insert the username without the @ symbol: ")
    
    while True:
        follow_instagram(username)
        time.sleep(0.3)

if __name__ == "__main__":
    main()
