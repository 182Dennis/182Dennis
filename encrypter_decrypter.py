alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 5

def crypt(original_text, shift_amount, option):
    output_text = ""
    if option == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            output_text += alphabet[shifted_position]

    print(f"Here is the {option}d message: {output_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))

    crypt(original_text=text, shift_amount=shift, option=direction)

    restart = input("Type 'yes' if you want to input a new message. Otherwise, simply type 'no'.\n ").lower()
    if restart == "no":
        should_continue = False
        print("Bye bye!")