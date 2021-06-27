import sys
import imghdr
import tkinter
from tkinter import filedialog, messagebox
from PIL import Image
from init import OUTPUT_FOLDER

root = tkinter.Tk(className='python-images-to-pdf')
files = filedialog.askopenfilenames(parent=root, title='Choose files')

#not choose any file exit program
if len(files) == 0:
    messagebox.showerror(title='Error', message='Not choose files')
    sys.exit(1)
images = []
for file in files:
    #check file is image
    if imghdr.what(file) is None:
        messagebox.showerror(title='Error', message='Choose error files')
        sys.exit(1)
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