import requests
import json
from datetime import datetime

def send_whatsapp_message(recipient, message):
    # API endpoint
    url = "http://localhost:8082/api/send"

    # Message data
    data = {
        "recipient": recipient,
        "message": message
    }

    try:
        # Send the request
        response = requests.post(url, json=data)
        
        # Print the response
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        return response.json()
    except Exception as e:
        print(f"Error sending message: {str(e)}")
        return None

def search_contacts(query):
    url = "http://localhost:8082/api/search_contacts"
    data = {"query": query}
    
    try:
        response = requests.post(url, json=data)
        print(f"\nSearch Results:")
        if response.status_code == 200:
            result = response.json()
            contacts = result.get('contacts', [])
            for idx, contact in enumerate(contacts):
                print(f"{idx+1}. {contact}")
            return contacts
        else:
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            return []
    except Exception as e:
        print(f"Error searching contacts: {str(e)}")
        return []

def get_latest_reply(jid):
    url = "http://localhost:8082/api/get_latest_reply"
    data = {"jid": jid}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            result = response.json()
            print(f"\nLatest reply from contact:")
            print(result.get('reply', 'No reply found.'))
        else:
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error fetching latest reply: {str(e)}")

def main():
    while True:
        print("\n=== WhatsApp MCP Message Sender ===")
        print("1. Search, Select & Send Message")
        print("2. Get Latest Reply from Contact (by JID)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            query = input("Enter contact name or number to search: ")
            contacts = search_contacts(query)
            if not contacts:
                print("No contacts found.")
                continue
            idx = input(f"Select contact (1-{len(contacts)}): ")
            try:
                idx = int(idx) - 1
                contact = contacts[idx]
                # Expecting format: 'Name - JID'
                if ' - ' in contact:
                    name, jid = contact.split(' - ', 1)
                else:
                    name, jid = contact, contact
                print(f"Selected: {name} (JID: {jid})")
                message = input("Enter your message: ")
                result = send_whatsapp_message(jid, message)
                if result and result.get('success'):
                    print("\n✅ Message sent successfully!")
                else:
                    print("\n❌ Failed to send message.")
            except Exception as e:
                print(f"Invalid selection: {e}")
                
        elif choice == "2":
            jid = input("Enter JID of contact to get latest reply: ")
            get_latest_reply(jid)
            
        elif choice == "3":
            print("\nGoodbye! 👋")
            break
            
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()