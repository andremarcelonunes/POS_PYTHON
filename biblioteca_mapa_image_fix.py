from tkinter import Tk, Label, Button, filedialog, Scale, Entry, Frame

from PIL import Image, ImageTk, ImageOps
import cv2


class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("TRATAMENTO DE IMAGEM")
        self.image_path = None

        self.image_label = Label(root)
        self.image_label.pack()

        # Sessão da tela para carregar a imagem
        load_frame = Frame(root)
        load_frame.pack(fill='x')
        self.load_button = Button(load_frame, text="Load Image", command=self.load_image)
        self.load_button.pack(side='left')

        # Sessão da tela para Rotação
        rotate_frame = Frame(root)
        rotate_frame.pack(fill='x')
        self.rotate_scale = Scale(rotate_frame, from_=0, to=360, label="Degrees", orient='horizontal')
        self.rotate_scale.pack(side='left')
        Button(rotate_frame, text="Rotate Image", command=self.rotate_image).pack(side='left')

        # Seção da tela para aplicar o Blurr
        blur_frame = Frame(root)
        blur_frame.pack(fill='x')
        self.blur_scale = Scale(blur_frame, from_=1, to=50, resolution=1, label="Strength", orient='horizontal')
        self.blur_scale.pack(side='left')
        Button(blur_frame, text="Apply Blur", command=self.apply_blur).pack(side='left')

        # Seção da tela para fazer resize
        resize_frame = Frame(root)
        resize_frame.pack(fill='x')
        self.width_entry = Entry(resize_frame)
        self.width_entry.pack(side='left')
        Label(resize_frame, text="Width").pack(side='left')
        self.height_entry = Entry(resize_frame)
        self.height_entry.pack(side='left')
        Label(resize_frame, text="Height").pack(side='left')
        Button(resize_frame, text="Resize Image", command=self.resize_image).pack(side='left')

        # Sessão da tela para converter em Escala de Cinza
        grayscale_frame = Frame(root)
        grayscale_frame.pack(fill='x')
        Button(grayscale_frame, text="Convert to Grayscale", command=self.to_grayscale).pack(side='left')

    #Daqui para baixo todos metodos.
    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            image = Image.open(self.image_path)
            self.display_image(image)

    def display_image(self, image):
        tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image

    def rotate_image(self):
        if self.image_path:
            image = Image.open(self.image_path)
            rotated = image.rotate(self.rotate_scale.get())
            self.display_image(rotated)

    def apply_blur(self):
        if self.image_path:
            image = cv2.imread(self.image_path)
            blur_strength = self.blur_scale.get()
            if blur_strength % 2 == 0:
                blur_strength += 1
            blurred = cv2.GaussianBlur(image, (blur_strength, blur_strength), 0)
            image = Image.fromarray(blurred)
            self.display_image(image)

    def resize_image(self):
        if self.image_path:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            image = Image.open(self.image_path)
            resized = image.resize((width, height))
            self.display_image(resized)

    def to_grayscale(self):
        if self.image_path:
            image = Image.open(self.image_path)
            grayscale = ImageOps.grayscale(image)
            self.display_image(grayscale).


if __name__ == "__main__":
    root = Tk()
    editor = ImageEditor(root)
    root.mainloop()
