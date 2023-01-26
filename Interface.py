import APIcall as call

url = "https://api.apilayer.com/currency_data/"
header = {"apikey": "2m3OOqOry0I8PDCRG5OiKpB8li6X2RJx"}
action = call.menu()
if action == 1:
    print(call.convert(url, header))
elif action == 2:
    print(call.historical(url, header))
elif action == 3:
    print(call.live(url, header))
else:
    fileObject = open("extractTrial.json", "w")
    content, day = call.timeframe(url, header)
    fileObject.write(content)
    fileObject.close()
    print(call.predict("extractTrial.json", day))
