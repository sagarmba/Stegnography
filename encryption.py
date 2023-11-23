import cv2
import os

def encrypt_message(img, secret_message):
    d = {}
    for i in range(255):
        d[chr(i)] = i

    m, n, z = 0, 0, 0

    for char in secret_message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    return img

def decrypt_message(img, password):
    c = {}
    for i in range(255):
        c[i] = chr(i)

    message = ""
    n, m, z = 0, 0, 0

    for _ in range(len(password)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    return message

def save_encrypted_image(img, output_path):
    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")

if _name_ == "_main_":
    image_path = "mypic.jpg"
    img = cv2.imread(image_path)

    secret_msg = input("Enter secret message: ")
    password = input("Enter password: ")

    # Encryption
    encrypted_img = encrypt_message(img.copy(), secret_msg)
    save_encrypted_image(encrypted_img, "Encryptedmsg.jpg")

    message_input = input("Enter passcode for Decryption: ")
    if password == message_input:
        decrypted_message = decrypt_message(encrypted_img, password)
        print("Decryption message:", decrypted_message)
    else:
        print("Not a valid key")