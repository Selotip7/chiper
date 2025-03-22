text="kayzla"
custom_key="rumah"
alphabet="abcdefghijklmnopqrstuvwxyz"


def vigenere(message,key):
    index=0
    final_message=''
    for char in message.lower():
        key_value=key[index % len(key)]
        index+=1
        key_alpha=alphabet.find(key_value)
        print(key_alpha)
        char_alpha=alphabet.find(char)
        print(char_alpha)
        # print(char_alpha)
        lokasi=(key_alpha+char_alpha)%26
        print(lokasi)
        print("\n")
        final_message+=alphabet[lokasi]
    print("\n"+final_message)

vigenere(text,custom_key)