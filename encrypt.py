def caesar_encrypt(String,length):
    result = ""
    for i in range(len(String)):
        c = String[i]
        if(c.isupper()):
              result += chr((ord(String[i]) + length - 65) % 26 + 65)
        elif(c.islower()):
              result += chr((ord(String[i]) + length - 97) % 26 + 97)
        else:
              result +=String[i] 
    return result
    
def caesar_decrypt(String,length):
    result = caesar_encrypt(String, 26 - length%26)
    return result;


text = "ASSrqotLSD FaaUNN//"
length = 35
result1 = caesar_encrypt(text,length);
print(result1)
result2 = caesar_decrypt(result1,length);
print(result2)