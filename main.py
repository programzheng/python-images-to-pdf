import tkinter
from tkinter import filedialog
from PIL import Image
from init import OUTPUT_FOLDER

root = tkinter.Tk()
files = filedialog.askopenfilenames(parent=root, title='Choose a file')

images = []
for file in files:
    image = Image.open(r''+file)
    im = image.convert('RGB')
    images.append(im)
text = tkinter.Label(root, text='output pdf file name:').pack(side=tkinter.LEFT)
input = tkinter.StringVar()
inputEntry = tkinter.Entry(root, textvariable=input, bd=5).pack(side=tkinter.LEFT)
sendButton = tkinter.Button(root, height=1, width=10, text="send", command=root.quit)
sendButton.pack()
root.mainloop()
images[0].save(OUTPUT_FOLDER+'/'+input.get()+'.pdf', save_all=True, append_images=images[1:])