import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        self.image = None

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt Image", command=self.encrypt_image, state=tk.DISABLED)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt Image", command=self.decrypt_image, state=tk.DISABLED)
        self.decrypt_button.pack()

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack()

        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)
            self.encrypt_button.config(state=tk.NORMAL)
            self.decrypt_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.NORMAL)

    def display_image(self, image):
        image.thumbnail((500, 500))
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def encrypt_image(self):
        if self.image:
            self.image = self.apply_encryption(self.image)
            self.display_image(self.image)
            messagebox.showinfo("Success", "Image encrypted successfully!")

    def decrypt_image(self):
        if self.image:
            self.image = self.apply_decryption(self.image)
            self.display_image(self.image)
            messagebox.showinfo("Success", "Image decrypted successfully!")

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.image.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully!")

    def apply_encryption(self, image):
        pixels = image.load()
        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (255 - r, 255 - g, 255 - b)
        return image

    def apply_decryption(self, image):
        return self.apply_encryption(image)  # Encryption and decryption are symmetric in this simple example

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()

