message = (input()).lower()


reverse_letters = {"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"," ":" "}
secret_message = ""
for letters in message:
    secret_message += reverse_letters[letters]
print(secret_message)
    
