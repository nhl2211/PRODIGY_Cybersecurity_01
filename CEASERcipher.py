import string
from collections import Counter

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def brute_force_decrypt(text):
    # Try all possible shifts (1 to 25) and print the results
    print("Attempting brute-force decryption...")
    for shift in range(1, 26):
        decrypted_text = decrypt(text, shift)
        print(f"Shift {shift}: {decrypted_text}")
    print("Brute-force attack completed.")

def frequency_analysis_decrypt(text):
    # English letter frequency for comparison
    english_freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    # Count letter frequencies in the text
    counter = Counter([char.upper() for char in text if char.isalpha()])
    most_common = [item[0] for item in counter.most_common()]
    
    print("Performing frequency analysis decryption attempt...")
    for shift_guess in range(1, 26):
        decrypted_text = decrypt(text, shift_guess)
        decrypted_freq_order = ''.join(
            sorted(set(decrypted_text.upper()), key=decrypted_text.upper().count, reverse=True)
        )
        if decrypted_freq_order[:6] == english_freq_order[:6]:
            print(f"Frequency analysis suggests Shift {shift_guess}: {decrypted_text}")
            break
    print("Frequency analysis attempt completed.")

def main():
    print("Caesar Cipher Program - Advanced Version")
    message = input("Enter the message: ")
    shift = input("Enter shift value (leave blank if unknown): ")
    
    if shift.isdigit():
        shift = int(shift)
        encrypted_text = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_text}")
        decrypted_text = decrypt(encrypted_text, shift)
        print(f"Decrypted Message: {decrypted_text}")
    else:
        print("Shift unknown, attempting brute-force decryption and frequency analysis...")
        brute_force_decrypt(message)
        frequency_analysis_decrypt(message)

if __name__ == "__main__":
    main()

