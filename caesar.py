text="Hello zorld";
alphabet="abcdefghijklmnopqrstuvwxyz"
shift=3

def caesar(text,offset):
    enkripsi_text=''
    
    for char in text.lower():
     if char==' ':
        enkripsi_text+=char
     else:
        index=alphabet.find(char)
        enkripsi_text+=alphabet[(index+offset)%len(alphabet)]
        print(enkripsi_text)

caesar(text,shift)

