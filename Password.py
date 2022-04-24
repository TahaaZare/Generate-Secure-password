while True:
    print("Choose Your Option : \n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit")
    choice = input("Your Choice : ")
    if choice == "1":
        plainText = input("text : ")
        encryptedText = ""
        for character in plainText:
            x = ord(character) * 8 + 21
            encryptedText += chr(x)
        print(f"*"*21)
        print(f"encrypted text : {encryptedText}")
        print(f"*"*21)

    elif choice == "2":
        encryptedText = input("Encrypted Text : ")
        plainText = ""
        for character in encryptedText:
            x = (ord(character)-21)//8
            plainText += chr(x)
        print(f"*" * 21)
        print(f"decrypted text : {plainText}")
        print(f"*" * 21)

    elif choice == "3":
        break
    else:
        print(f"*"*21)
        print("Sorry Just Choose Number 1 to 3 !!!")
        print(f"*" * 21)
