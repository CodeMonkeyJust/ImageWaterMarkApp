import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("图像水印工具 For Flyany V1.0.0")
        # setting window size
        width = 700
        height = 702
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_79 = tk.Button(root)
        GButton_79["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_79["font"] = ft
        GButton_79["fg"] = "#000000"
        GButton_79["justify"] = "center"
        GButton_79["text"] = "..."
        GButton_79.place(x=560, y=20, width=84, height=30)
        GButton_79["command"] = self.GButton_79_command

        GLabel_855 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_855["font"] = ft
        GLabel_855["fg"] = "#333333"
        GLabel_855["justify"] = "right"
        GLabel_855["text"] = "水印文件目录："
        GLabel_855.place(x=20, y=20, width=90, height=30)

        GLabel_669 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_669["font"] = ft
        GLabel_669["fg"] = "#333333"
        GLabel_669["justify"] = "right"
        GLabel_669["text"] = "水印位置："
        GLabel_669.place(x=20, y=280, width=90, height=30)

        GLabel_72 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_72["font"] = ft
        GLabel_72["fg"] = "#333333"
        GLabel_72["justify"] = "right"
        GLabel_72["text"] = "图像/水印大小："
        GLabel_72.place(x=20, y=460, width=90, height=30)

        GLineEdit_WatermarkDir = tk.Entry(root)
        GLineEdit_WatermarkDir["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_WatermarkDir["font"] = ft
        GLineEdit_WatermarkDir["fg"] = "#333333"
        GLineEdit_WatermarkDir["justify"] = "center"
        GLineEdit_WatermarkDir["text"] = ""
        GLineEdit_WatermarkDir.place(x=130, y=20, width=400, height=30)

        GListBox_903 = tk.Listbox(root)
        GListBox_903["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_903["font"] = ft
        GListBox_903["fg"] = "#333333"
        GListBox_903["justify"] = "center"
        GListBox_903.place(x=130, y=80, width=512, height=170)

        GLabel_268 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_268["font"] = ft
        GLabel_268["fg"] = "#333333"
        GLabel_268["justify"] = "right"
        GLabel_268["text"] = "透明度："
        GLabel_268.place(x=380, y=460, width=90, height=30)

        GLineEdit_518 = tk.Entry(root)
        GLineEdit_518["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_518["font"] = ft
        GLineEdit_518["fg"] = "#333333"
        GLineEdit_518["justify"] = "center"
        GLineEdit_518["text"] = "3"
        GLineEdit_518.place(x=120, y=460, width=150, height=30)

        GLabel_54 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_54["font"] = ft
        GLabel_54["fg"] = "#333333"
        GLabel_54["justify"] = "right"
        GLabel_54["text"] = "图像文件："
        GLabel_54.place(x=20, y=520, width=90, height=30)

        GLineEdit_962 = tk.Entry(root)
        GLineEdit_962["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_962["font"] = ft
        GLineEdit_962["fg"] = "#333333"
        GLineEdit_962["justify"] = "center"
        GLineEdit_962["text"] = ""
        GLineEdit_962.place(x=120, y=520, width=400, height=30)

        GButton_389 = tk.Button(root)
        GButton_389["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_389["font"] = ft
        GButton_389["fg"] = "#000000"
        GButton_389["justify"] = "center"
        GButton_389["text"] = "..."
        GButton_389.place(x=540, y=520, width=84, height=30)
        GButton_389["command"] = self.GButton_389_command

        GButton_522 = tk.Button(root)
        GButton_522["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_522["font"] = ft
        GButton_522["fg"] = "#000000"
        GButton_522["justify"] = "center"
        GButton_522["text"] = "生成水印图片"
        GButton_522.place(x=260, y=590, width=165, height=30)
        GButton_522["command"] = self.GButton_522_command

        GRadio_385 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_385["font"] = ft
        GRadio_385["fg"] = "#333333"
        GRadio_385["justify"] = "left"
        GRadio_385["text"] = "左上"
        GRadio_385.place(x=130, y=280, width=90, height=30)
        GRadio_385["command"] = self.GRadio_385_command

        GRadio_873 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_873["font"] = ft
        GRadio_873["fg"] = "#333333"
        GRadio_873["justify"] = "right"
        GRadio_873["text"] = "右上"
        GRadio_873.place(x=550, y=280, width=90, height=30)
        GRadio_873["command"] = self.GRadio_873_command

        GLabel_190 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_190["font"] = ft
        GLabel_190["fg"] = "#333333"
        GLabel_190["justify"] = "right"
        GLabel_190["text"] = "请选择水印："
        GLabel_190.place(x=20, y=80, width=90, height=30)

        GLineEdit_887 = tk.Entry(root)
        GLineEdit_887["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_887["font"] = ft
        GLineEdit_887["fg"] = "#333333"
        GLineEdit_887["justify"] = "center"
        GLineEdit_887["text"] = "0"
        GLineEdit_887.place(x=490, y=460, width=150, height=30)

        GRadio_894 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_894["font"] = ft
        GRadio_894["fg"] = "#333333"
        GRadio_894["justify"] = "left"
        GRadio_894["text"] = "左中"
        GRadio_894.place(x=130, y=340, width=90, height=30)
        GRadio_894["command"] = self.GRadio_894_command

        GRadio_92 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_92["font"] = ft
        GRadio_92["fg"] = "#333333"
        GRadio_92["justify"] = "center"
        GRadio_92["text"] = "中上"
        GRadio_92.place(x=340, y=280, width=90, height=30)
        GRadio_92["command"] = self.GRadio_92_command

        GRadio_330 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_330["font"] = ft
        GRadio_330["fg"] = "#333333"
        GRadio_330["justify"] = "center"
        GRadio_330["text"] = "中中"
        GRadio_330.place(x=340, y=340, width=90, height=30)
        GRadio_330["command"] = self.GRadio_330_command

        GRadio_923 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_923["font"] = ft
        GRadio_923["fg"] = "#333333"
        GRadio_923["justify"] = "right"
        GRadio_923["text"] = "右中"
        GRadio_923.place(x=550, y=340, width=90, height=30)
        GRadio_923["command"] = self.GRadio_923_command

        GRadio_31 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_31["font"] = ft
        GRadio_31["fg"] = "#333333"
        GRadio_31["justify"] = "left"
        GRadio_31["text"] = "左下"
        GRadio_31.place(x=130, y=400, width=90, height=25)
        GRadio_31["command"] = self.GRadio_31_command

        GRadio_639 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_639["font"] = ft
        GRadio_639["fg"] = "#333333"
        GRadio_639["justify"] = "center"
        GRadio_639["text"] = "中下"
        GRadio_639.place(x=340, y=400, width=90, height=30)
        GRadio_639["command"] = self.GRadio_639_command

        GRadio_95 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_95["font"] = ft
        GRadio_95["fg"] = "#333333"
        GRadio_95["justify"] = "right"
        GRadio_95["text"] = "右下"
        GRadio_95.place(x=550, y=400, width=90, height=30)
        GRadio_95["command"] = self.GRadio_95_command

        GLabel_630 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_630["font"] = ft
        GLabel_630["fg"] = "#333333"
        GLabel_630["justify"] = "center"
        GLabel_630["text"] = "/1"
        GLabel_630.place(x=280, y=460, width=35, height=30)

    def GButton_79_command(self):
        print("command")

    def GButton_389_command(self):
        print("command")

    def GButton_522_command(self):
        print("command")

    def GRadio_385_command(self):
        print("command")

    def GRadio_873_command(self):
        print("command")

    def GRadio_894_command(self):
        print("command")

    def GRadio_92_command(self):
        print("command")

    def GRadio_330_command(self):
        print("command")

    def GRadio_923_command(self):
        print("command")

    def GRadio_31_command(self):
        print("command")

    def GRadio_639_command(self):
        print("command")

    def GRadio_95_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
