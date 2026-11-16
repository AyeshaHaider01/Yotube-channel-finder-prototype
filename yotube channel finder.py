import os
import webbrowser

os.system("cls")

print("==============================")
print("     YOUTUBE CHANNEL FINDER")
print("==============================")

channel = input("Enter channel name: ")

if channel:
    link = "https://www.youtube.com/@" + channel
    print("\nOpening channel...")
    webbrowser.open(link)

else:
    print("Please enter a channel name!")
