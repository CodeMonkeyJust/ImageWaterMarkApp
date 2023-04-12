import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, messagebox
import os
from config_unit import get_config, set_config
from workspace import get_config_filename, init_file
from image_watermark import add_watermark
from date_unit import get_current_time

LOG_LINE_NUM = 0


class App:
    def __init__(self, root):
        # setting title
        root.title("图像水印工具 For Flyany V1.0.0")
        # setting window size
        width = 700
        height = 800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # 全局变量
        self.watermark_dir = ''
        self.watermark_path = ''
        self.image_dir = ''
        self.watermark_index = 0
        self.watermark_pos = 0
        self.watermark_offset_x = 0
        self.watermark_offset_y = 0
        self.watermark_zoom = 0
        self.watermark_transparency = 0
        # 水印9宫格位置
        self.v = tk.IntVar()
        self.v.set(7)

        GButton_ChooseWatermarkDir = tk.Button(root)
        GButton_ChooseWatermarkDir["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_ChooseWatermarkDir["font"] = ft
        GButton_ChooseWatermarkDir["fg"] = "#000000"
        GButton_ChooseWatermarkDir["justify"] = "center"
        GButton_ChooseWatermarkDir["text"] = "..."
        GButton_ChooseWatermarkDir.place(x=560, y=20, width=84, height=30)
        GButton_ChooseWatermarkDir["command"] = self.GButton_ChooseWatermarkDir_command

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

        self.GLineEdit_WatermarkDir = tk.Entry(root)
        self.GLineEdit_WatermarkDir["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_WatermarkDir["font"] = ft
        self.GLineEdit_WatermarkDir["fg"] = "#333333"
        self.GLineEdit_WatermarkDir["justify"] = "left"
        self.GLineEdit_WatermarkDir.place(x=130, y=20, width=400, height=30)

        self.GListBox_WatermarkImg = tk.Listbox(root)
        self.GListBox_WatermarkImg["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GListBox_WatermarkImg["font"] = ft
        self.GListBox_WatermarkImg["fg"] = "#333333"
        self.GListBox_WatermarkImg["justify"] = "left"
        # 失去焦点后仍然保持选择
        self.GListBox_WatermarkImg["exportselection"] = False
        # self.GListBox_WatermarkImg["selectmode"] = tk.BROWSE
        self.GListBox_WatermarkImg.place(x=130, y=80, width=512, height=170)

        GRadio_385 = tk.Radiobutton(root, variable=self.v, value=1)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_385["font"] = ft
        GRadio_385["fg"] = "#333333"
        GRadio_385["justify"] = "left"
        GRadio_385["text"] = "左上"
        GRadio_385.place(x=130, y=280, width=90, height=30)

        GRadio_873 = tk.Radiobutton(root, variable=self.v, value=3)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_873["font"] = ft
        GRadio_873["fg"] = "#333333"
        GRadio_873["justify"] = "right"
        GRadio_873["text"] = "右上"
        GRadio_873.place(x=550, y=280, width=90, height=30)

        GLabel_190 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_190["font"] = ft
        GLabel_190["fg"] = "#333333"
        GLabel_190["justify"] = "right"
        GLabel_190["text"] = "请选择水印："
        GLabel_190.place(x=20, y=80, width=90, height=30)

        GRadio_894 = tk.Radiobutton(root, variable=self.v, value=4)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_894["font"] = ft
        GRadio_894["fg"] = "#333333"
        GRadio_894["justify"] = "left"
        GRadio_894["text"] = "左中"
        GRadio_894.place(x=130, y=340, width=90, height=30)

        GRadio_92 = tk.Radiobutton(root, variable=self.v, value=2)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_92["font"] = ft
        GRadio_92["fg"] = "#333333"
        GRadio_92["justify"] = "center"
        GRadio_92["text"] = "中上"
        GRadio_92.place(x=340, y=280, width=90, height=30)

        GRadio_330 = tk.Radiobutton(root, variable=self.v, value=5)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_330["font"] = ft
        GRadio_330["fg"] = "#333333"
        GRadio_330["justify"] = "center"
        GRadio_330["text"] = "中中"
        GRadio_330.place(x=340, y=340, width=90, height=30)

        GRadio_923 = tk.Radiobutton(root, variable=self.v, value=6)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_923["font"] = ft
        GRadio_923["fg"] = "#333333"
        GRadio_923["justify"] = "right"
        GRadio_923["text"] = "右中"
        GRadio_923.place(x=550, y=340, width=90, height=30)

        GRadio_31 = tk.Radiobutton(root, variable=self.v, value=7)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_31["font"] = ft
        GRadio_31["fg"] = "#333333"
        GRadio_31["justify"] = "left"
        GRadio_31["text"] = "左下"
        GRadio_31.place(x=130, y=400, width=90, height=25)

        GRadio_639 = tk.Radiobutton(root, variable=self.v, value=8)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_639["font"] = ft
        GRadio_639["fg"] = "#333333"
        GRadio_639["justify"] = "center"
        GRadio_639["text"] = "中下"
        GRadio_639.place(x=340, y=400, width=90, height=30)

        GRadio_95 = tk.Radiobutton(root, variable=self.v, value=9)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_95["font"] = ft
        GRadio_95["fg"] = "#333333"
        GRadio_95["justify"] = "right"
        GRadio_95["text"] = "右下"
        GRadio_95.place(x=550, y=400, width=90, height=30)

        # 水印偏移X
        GLabel_offset_x = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_offset_x["font"] = ft
        GLabel_offset_x["fg"] = "#333333"
        GLabel_offset_x["justify"] = "right"
        GLabel_offset_x["text"] = "水印偏移X："
        GLabel_offset_x.place(x=20, y=460, width=90, height=30)

        self.GLineEdit_offset_x = tk.Entry(root)
        self.GLineEdit_offset_x["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_offset_x["font"] = ft
        self.GLineEdit_offset_x["fg"] = "#333333"
        self.GLineEdit_offset_x["justify"] = "center"
        self.GLineEdit_offset_x.place(x=130, y=460, width=150, height=30)

        # 水印偏移Y
        GLabel_offset_y = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_offset_y["font"] = ft
        GLabel_offset_y["fg"] = "#333333"
        GLabel_offset_y["justify"] = "right"
        GLabel_offset_y["text"] = "水印偏移Y："
        GLabel_offset_y.place(x=380, y=460, width=90, height=30)

        self.GLineEdit_offset_y = tk.Entry(root)
        self.GLineEdit_offset_y["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_offset_y["font"] = ft
        self.GLineEdit_offset_y["fg"] = "#333333"
        self.GLineEdit_offset_y["justify"] = "center"
        self.GLineEdit_offset_y.place(x=490, y=460, width=150, height=30)

        # 图像/水印大小
        GLabel_72 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_72["font"] = ft
        GLabel_72["fg"] = "#333333"
        GLabel_72["justify"] = "right"
        GLabel_72["text"] = "图片/水印："
        GLabel_72.place(x=20, y=520, width=90, height=30)

        self.GLineEdit_zoom = tk.Entry(root)
        self.GLineEdit_zoom["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_zoom["font"] = ft
        self.GLineEdit_zoom["fg"] = "#333333"
        self.GLineEdit_zoom["justify"] = "center"
        self.GLineEdit_zoom["text"] = "3"
        self.GLineEdit_zoom.place(x=130, y=520, width=150, height=30)

        GLabel_630 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_630["font"] = ft
        GLabel_630["fg"] = "#333333"
        GLabel_630["justify"] = "center"
        GLabel_630["text"] = "/1"
        GLabel_630.place(x=280, y=520, width=35, height=30)

        # 透明度
        GLabel_268 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_268["font"] = ft
        GLabel_268["fg"] = "#333333"
        GLabel_268["justify"] = "right"
        GLabel_268["text"] = "透明度："
        GLabel_268.place(x=380, y=520, width=90, height=30)

        self.GLineEdit_transparency = tk.Entry(root)
        self.GLineEdit_transparency["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_transparency["font"] = ft
        self.GLineEdit_transparency["fg"] = "#333333"
        self.GLineEdit_transparency["justify"] = "center"
        self.GLineEdit_transparency.place(x=490, y=520, width=150, height=30)

        # 图像文件目录
        GLabel_54 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_54["font"] = ft
        GLabel_54["fg"] = "#333333"
        GLabel_54["justify"] = "right"
        GLabel_54["text"] = "图片文件目录："
        GLabel_54.place(x=20, y=580, width=90, height=30)

        self.GLineEdit_image_dir = tk.Entry(root)
        self.GLineEdit_image_dir["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_image_dir["font"] = ft
        self.GLineEdit_image_dir["fg"] = "#333333"
        self.GLineEdit_image_dir["justify"] = "left"
        self.GLineEdit_image_dir.place(x=130, y=580, width=400, height=30)

        GButton_choose_image_dir = tk.Button(root)
        GButton_choose_image_dir["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_choose_image_dir["font"] = ft
        GButton_choose_image_dir["fg"] = "#000000"
        GButton_choose_image_dir["justify"] = "center"
        GButton_choose_image_dir["text"] = "..."
        GButton_choose_image_dir.place(x=560, y=580, width=84, height=30)
        GButton_choose_image_dir["command"] = self.GButton_choose_image_dir_command

        # 生成水印图片
        GButton_add_watermark = tk.Button(root)
        GButton_add_watermark["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_add_watermark["font"] = ft
        GButton_add_watermark["fg"] = "#000000"
        GButton_add_watermark["justify"] = "center"
        GButton_add_watermark["text"] = "生成水印图片"
        GButton_add_watermark.place(x=260, y=640, width=165, height=30)
        GButton_add_watermark["command"] = self.GButton_add_watermark_command

        self.Text_log = tk.Text(root)  # 日志框
        self.Text_log.place(x=20, y=700, width=660, height=80)
        self.load_default_config()

    # 选择水印文件夹
    def GButton_ChooseWatermarkDir_command(self):
        select_dir = tk.filedialog.askdirectory()
        if len(select_dir) > 0:
            self.set_watermark_dir(select_dir)

    def GButton_choose_image_dir_command(self):
        select_dir = tk.filedialog.askdirectory()
        if len(select_dir) > 0:
            self.set_image_dir(select_dir)

    def GButton_add_watermark_command(self):
        self.load_form_val()
        if len(self.image_dir) < 2:
            messagebox.showwarning('注意', '图片路径不能为空！')
            return
        selection = self.GListBox_WatermarkImg.curselection()
        print(selection)
        if not selection:
            messagebox.showwarning('注意', '请选择水印！')
            return
        self.watermark_path = os.path.join(self.watermark_dir,
                                           self.GListBox_WatermarkImg.get(selection[0]))
        self.add_watermark_dir(self.image_dir)

    # 读取水印文件
    def load_watermark(self, dir):
        i = 0
        for filename in os.listdir(dir):
            filepath = os.path.join(dir, filename)
            if os.path.isfile(filepath):
                watermakr_filepath = os.path.basename(filepath)
                ext = os.path.splitext(watermakr_filepath)[1].lower()
                if ext == '.png':
                    i = i + 1
                    self.GListBox_WatermarkImg.insert(i, watermakr_filepath)

    # 读取图像文件
    def load_image(self, dir):
        i = 0
        for filename in os.listdir(dir):
            filepath = os.path.join(dir, filename)
            if os.path.isfile(filepath):
                watermakr_filepath = os.path.basename(filepath)
                ext = os.path.splitext(watermakr_filepath)[1].lower()
                if ext == '.png' or ext == '.jpg':
                    i = i + 1
                    self.GListBox_WatermarkImg.insert(i, watermakr_filepath)

    def load_default_config(self):
        self.set_watermark_dir(get_config(get_config_filename(), 'watermark', 'dir'))
        self.set_watermark_index(get_config(get_config_filename(), 'watermark', 'index'))
        self.v.set(get_config(get_config_filename(), 'watermark', 'pos'))
        self.GLineEdit_offset_x.insert(0, get_config(get_config_filename(), 'watermark', 'offset_x'))
        self.GLineEdit_offset_y.insert(0, get_config(get_config_filename(), 'watermark', 'offset_y'))
        self.GLineEdit_zoom.delete(0, tk.END)
        self.GLineEdit_zoom.insert(0, get_config(get_config_filename(), 'watermark', 'zoom'))
        self.GLineEdit_transparency.delete(0, tk.END)
        self.GLineEdit_transparency.insert(0, get_config(get_config_filename(), 'watermark', 'transparency'))

    def save_default_config(self):
        set_config(get_config_filename(), 'watermark', 'dir', self.watermark_dir)
        set_config(get_config_filename(), 'watermark', 'index', self.watermark_index)
        set_config(get_config_filename(), 'watermark', 'pos', self.watermark_pos)
        set_config(get_config_filename(), 'watermark', 'offset_x', self.watermark_offset_x)
        set_config(get_config_filename(), 'watermark', 'offset_y', self.watermark_offset_y)
        set_config(get_config_filename(), 'watermark', 'zoom', self.watermark_zoom)
        set_config(get_config_filename(), 'watermark', 'transparency', self.watermark_transparency)

    def set_watermark_dir(self, watermark_dir):
        self.watermark_dir = watermark_dir
        self.GLineEdit_WatermarkDir.delete(0, tk.END)
        self.GLineEdit_WatermarkDir.insert(0, self.watermark_dir)
        self.GLineEdit_WatermarkDir["text"] = self.watermark_dir
        self.load_watermark(self.watermark_dir)

    def set_image_dir(self, image_dir):
        self.image_dir = image_dir
        self.GLineEdit_image_dir.delete(0, tk.END)
        self.GLineEdit_image_dir.insert(0, self.image_dir)

    def set_watermark_index(self, index):
        self.watermark_index = index
        self.GListBox_WatermarkImg.select_set(index)

    def load_form_val(self):
        self.watermark_pos = int(self.v.get())
        self.watermark_index = self.GListBox_WatermarkImg.curselection()[0]
        self.watermark_offset_x = int(self.GLineEdit_offset_x.get())
        self.watermark_offset_y = int(self.GLineEdit_offset_y.get())
        self.watermark_zoom = int(self.GLineEdit_zoom.get())
        self.watermark_transparency = int(self.GLineEdit_transparency.get())

    def add_watermark_dir(self, image_dir):
        i = 0;
        out_dir = image_dir + '_watermark'
        self.write_log_to_text('======开始添加水印======')
        for filename in os.listdir(image_dir):
            filepath = os.path.join(image_dir, filename)
            if os.path.isfile(filepath):
                base_filename = os.path.basename(filepath)
                ext = os.path.splitext(base_filename)[1].lower()
                if ext == '.png' or ext == '.jpg':
                    i = i + 1
                    out_path = os.path.join(out_dir, os.path.splitext(base_filename)[0] + '.png')
                    # print(out_path)
                    add_watermark(watermark_path=self.watermark_path, image_path=filepath, out_path=out_path,
                                  zoom=self.watermark_zoom, pos=self.watermark_pos, offset_x=self.watermark_offset_x,
                                  offset_y=self.watermark_offset_y,
                                  transparency=self.watermark_transparency)
                    self.write_log_to_text(str(i) + '-[' + filepath + ']')
        self.write_log_to_text('======添加水印完成，共添加' + str(i) + '个文件======')
        self.write_log_to_text('文件输出路径' + out_dir)
        self.save_default_config()
        messagebox.showinfo('信息', '添加水印完成，共添加' + str(i) + '个文件,水印文件输出路径'+out_dir)

    def write_log_to_text(self, logmsg):
        global LOG_LINE_NUM
        current_time = get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.Text_log.insert(tk.END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.Text_log.delete(1.0, 2.0)
            self.Text_log.insert(tk.END, logmsg_in)


def gui_start():
    init_file()
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    gui_start()
