import tkinter as tk
from tkinter import messagebox

class CaesarCipher:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")

        # Create input fields
        self.text_label = tk.Label(root, text="Text:")
        self.text_label.pack()
        self.text_entry = tk.Text(root, height=10, width=40)
        self.text_entry.pack()

        self.shift_label = tk.Label(root, text="Shift:")
        self.shift_label.pack()
        self.shift_entry = tk.Entry(root, width=40)
        self.shift_entry.pack()

        # Create buttons
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack()

        # Create output field
        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=10, width=40)
        self.output_text.pack()

    def encrypt(self):
        text = self.text_entry.get("1.0", "end-1c")
        shift = int(self.shift_entry.get())

        encrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                encrypted_text += char

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", encrypted_text)

    def decrypt(self):
        text = self.text_entry.get("1.0", "end-1c")
        shift = int(self.shift_entry.get())

        decrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                decrypted_text += char

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", decrypted_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipher(root)
    root.mainloop()