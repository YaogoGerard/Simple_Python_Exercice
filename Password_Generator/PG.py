#  https://github.com/YaogoGerard
"""
This program is a password generator with a graphical user interface
"""

import secrets
import string

import customtkinter as ctk

# definition of the appareance of the window
ctk.set_appearance_mode("dark")


# this class is an heritage of ctk.CTk class
class PasswordGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()
        # all self.XXX are the attributes of the class PasswordGenerator
        # window title and size
        self.title("Password Generator")
        self.geometry("400x300")

        # label and entry for password length
        self.length_label = ctk.CTkLabel(self, text="Password Length(8 characters min):")
        self.length_label.pack(pady=10)
        self.length_entry = ctk.CTkEntry(self)
        self.length_entry.pack(pady=5)

        # button for password generation
        self.generate_button = ctk.CTkButton(self, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Create a label to display the generated password
        self.password_label = ctk.CTkLabel(self, text="",text_color="orange")
        self.password_label.pack(pady=10)
        
        self.copy_button = ctk.CTkButton(self, text="Copier", fg_color="green",command=self.clipboard)
        self.copy_button.pack(pady=20)
        

    # this fonc is a method of the clas PasswordGenerator, it generate the random password based on their lenght
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                length=8
            characters = string.ascii_letters + string.digits + string.punctuation
            self.password = "".join(secrets.choice(characters) for i in range(length))
            self.password_label.configure(text=self.password)
        except ValueError as e:
            self.password_label.config(text=str(e))

    def clipboard(self):
        # allow to copy the generated password to the clipboard
        self.clipboard_clear()
        self.clipboard_append(self.password)
        self.copy_button.configure(text="Copié !", fg_color="green")
        self.after(2000, self.reset)
        self.update()

    def reset(self):
        # reset the copy after 2 seconds
        self.copy_button.configure(text="Copier")
        self.update()


# this the entry point of our exercice
if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
