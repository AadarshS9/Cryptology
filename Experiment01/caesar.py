#CAESAR CIPHER
print("Caesar Cipher Menu")

while(1):
    print("1.Encryption \t 2.Decryption \t3.Exit")
    menuch = int(input("Kindly input your choice of action: "))
    result = ""
    key = 3
    if(menuch==1):
        plaintext = input("\tKindly enter plain text: ")
        for i in plaintext:
            base = ord('a') if i.islower() else ord('A')
            c = chr((ord(i)+key-base)%26+base)
            result += c
        print("\tCipher Text: ",result,"\n")

    if(menuch==2):
        plaintext = input("\tKindly enter cipher text: ")
        for i in plaintext:
            base = ord('a') if i.islower() else ord('A')
            c = chr((ord(i)-key-base)%26+base)
            result += c
        print("\tPlain Text: ",result,"\n")

    if(menuch==3):
        print("\tGoodbye\n")
        break
