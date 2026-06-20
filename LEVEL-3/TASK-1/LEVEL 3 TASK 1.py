SHIFT = 3

print("Program Started")

while True:
    print("\n===== FILE ENCRYPTION / DECRYPTION =====")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":

        file_name = input("Enter file name to encrypt: ")

        try:
            file = open(file_name, "r")
            text = file.read()
            file.close()

            encrypted_text = ""

            for char in text:
                encrypted_text += chr(ord(char) + SHIFT)

            file = open("encrypted.txt", "w")
            file.write(encrypted_text)
            file.close()

            print("File encrypted successfully!")
            print("Saved as encrypted.txt")

        except FileNotFoundError:
            print("File not found.")

    elif choice == "2":

        file_name = input("Enter file name to decrypt: ")

        try:
            file = open(file_name, "r")
            text = file.read()
            file.close()

            decrypted_text = ""

            for char in text:
                decrypted_text += chr(ord(char) - SHIFT)

            file = open("decrypted.txt", "w")
            file.write(decrypted_text)
            file.close()

            print("File decrypted successfully!")
            print("Saved as decrypted.txt")

        except FileNotFoundError:
            print("File not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Please enter 1, 2, or 3.")