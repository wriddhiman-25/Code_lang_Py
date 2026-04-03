import random
import string

class Message:
    def __init__(self, msg):
        self.msg = msg

    # 🔐 ENCODE FUNCTION
    def Encode(self):
        words = self.msg.split()
        result = []

        for word in words:
            if len(word) >= 3:
                # Step 1: move first letter to end
                new_word = word[1:] + word[0]

                # Step 2: generate random 3 letters
                rand_start = ''.join(random.choices(string.ascii_lowercase, k=3))
                rand_end = ''.join(random.choices(string.ascii_lowercase, k=3))

                # Step 3: add them
                new_word = rand_start + new_word + rand_end
                result.append(new_word)
            else:
                # reverse small words
                result.append(word[::-1])

        print("🔐 Encoded Message:", " ".join(result))

    # 🔓 DECODE FUNCTION
    def Decode(self):
        words = self.msg.split()
        result = []

        for word in words:
            if len(word) >= 3:
                # Step 1: remove first 3 and last 3 characters
                trimmed = word[3:-3]

                # Step 2: move last letter to front
                original = trimmed[-1] + trimmed[:-1]

                result.append(original)
            else:
                # reverse small words
                result.append(word[::-1])

        print("🔓 Decoded Message:", " ".join(result))

    # 🎮 USER CHOICE
    def ask(self):
        choice = input("☠️: Press 'E' to Encode and Press 'D' to Decode: ")

        if choice.upper() == 'E':
            self.Encode()
        elif choice.upper() == 'D':
            self.Decode()
        else:
            print("Invalid Choice...!")


# 🚀 MAIN PROGRAM
m1 = Message(input("☠️: Enter The Message -> "))
m1.ask()