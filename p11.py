s=input("enter something: ")
if "weather" in s:
    print("weather API")
elif "news" in s:
    print("NEWS API")
else:
    print("general response")