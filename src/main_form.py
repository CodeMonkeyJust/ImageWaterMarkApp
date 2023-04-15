# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2023-04-12
# Description:图像水印添加主界面
# ------------------------------------------------------------------
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, messagebox
import os
from config_unit import get_config, set_config
from workspace import get_config_filename, init_file
from image_watermark import add_watermark
from date_unit import get_current_time

LOG_LINE_NUM = 0


class WindowsMain(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__()
        init_file()
        # 全局变量
        self.VER = 'V1.1.1'
        self.watermark_dir = ''
        self.watermark_path = ''
        self.image_dir = ''
        self.watermark_index = 0
        self.watermark_pos = 5
        self.watermark_offset_x = 0
        self.watermark_offset_y = 0
        self.watermark_zoom = 3
        self.watermark_opacity = 0.65
        self.output_ext_type = 1
        # 水印9宫格位置
        self.gv_watermark_pos = tk.IntVar()
        self.gv_watermark_pos.set(7)
        self.gv_output_ext_type = tk.IntVar()
        self.gv_output_ext_type.set(1)
        self.init_from()
        self.after(100, self.refresh_from)
        self.load_default_config()
        self.mainloop()

    # 初始化界面
    def init_from(self):
        # setting title
        self.title("图像批量加水印工具")
        # setting window size
        width = 700
        height = 800
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        # 菜单，MacOS下根菜单不显示，所以不使用根菜单
        menu_main = tk.Menu(self)
        menu_file = tk.Menu(menu_main, tearoff=False)
        menu_file.add_command(label='选择水印', command=self.button_choose_watermark_dir_command)
        menu_file.add_command(label='选择图像', command=self.button_choose_image_dir_command)
        # 添加一条分割线
        menu_file.add_separator()
        menu_file.add_command(label="退出", command=self.destroy)
        menu_main.add_cascade(label='文件', menu=menu_file)
        menu_help = tk.Menu(menu_main, tearoff=False)
        menu_help.add_command(label='关于', command=self.show_about_author)
        menu_main.add_cascade(label='帮助', menu=menu_help)
        self.config(menu=menu_main)

        label_190 = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_190["font"] = ft
        label_190["fg"] = "#333333"
        label_190["justify"] = "right"
        label_190["text"] = "请选择水印："
        label_190.place(x=20, y=80, width=90, height=30)

        button_choose_watermark_dir = tk.Button(self)
        button_choose_watermark_dir["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button_choose_watermark_dir["font"] = ft
        button_choose_watermark_dir["fg"] = "#000000"
        button_choose_watermark_dir["justify"] = "center"
        button_choose_watermark_dir["text"] = "..."
        button_choose_watermark_dir.place(x=560, y=20, width=84, height=30)
        button_choose_watermark_dir["command"] = self.button_choose_watermark_dir_command

        label_855 = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_855["font"] = ft
        label_855["fg"] = "#333333"
        label_855["justify"] = "right"
        label_855["text"] = "水印文件目录："
        label_855.place(x=20, y=20, width=90, height=30)

        self.entry_watermark_dir = tk.Entry(self)
        self.entry_watermark_dir["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.entry_watermark_dir["font"] = ft
        self.entry_watermark_dir["fg"] = "#333333"
        self.entry_watermark_dir["justify"] = "left"
        self.entry_watermark_dir.place(x=130, y=20, width=400, height=30)

        self.listbox_watermark_img = tk.Listbox(self)
        self.listbox_watermark_img["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.listbox_watermark_img["font"] = ft
        self.listbox_watermark_img["fg"] = "#333333"
        self.listbox_watermark_img["justify"] = "left"
        # 失去焦点后仍然保持选择
        self.listbox_watermark_img["exportselection"] = False
        # self.listbox_watermark_img["selectmode"] = tk.BROWSE
        self.listbox_watermark_img.place(x=130, y=80, width=512, height=170)

        label_669 = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_669["font"] = ft
        label_669["fg"] = "#333333"
        label_669["justify"] = "right"
        label_669["text"] = "水印位置："
        label_669.place(x=20, y=280, width=90, height=30)

        radiobutton_pos_lt = tk.Radiobutton(self, variable=self.gv_watermark_pos, value=1)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_pos_lt["font"] = ft
        radiobutton_pos_lt["fg"] = "#333333"
        radiobutton_pos_lt["justify"] = "left"
        radiobutton_pos_lt["text"] = "左上"
        radiobutton_pos_lt.place(x=130, y=280, width=90, height=30)

        radiobutton_pos_mt = tk.Radiobutton(self, variable=self.gv_watermark_pos, value=2)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_pos_mt["font"] = ft
        radiobutton_pos_mt["fg"] = "#333333"
        radiobutton_pos_mt["justify"] = "center"
        radiobutton_pos_mt["text"] = "中上"
        radiobutton_pos_mt.place(x=340, y=280, width=90, height=30)

        radiobutton_pos_rt = tk.Radiobutton(self, variable=self.gv_watermark_pos, value=3)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_pos_rt["font"] = ft
        radiobutton_pos_rt["fg"] = "#333333"
        radiobutton_pos_rt["justify"] = "right"
        radiobutton_pos_rt["text"] = "右上"
        radiobutton_pos_rt.place(x=550, y=280, width=90, height=30)

        radiobutton_pos_lm = tk.Radiobutton(self, variable=self.gv_watermark_pos, value=4)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_pos_lm["font"] = ft
        radiobutton_pos_lm["fg"] = "#333333"
        radiobutton_pos_lm["justify"] = "left"
        radiobutton_pos_lm["text"] = "左中"
        radiobutton_pos_lm.place(x=130, y=320, width=90, height=30)

        radiobutton_pos_mm = tk.Radiobutton(self, variable=self.gv_watermark_pos, value=5)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_pos_mm["font"] = ft
        radiobutton_pos_mm["fg"] = "#333333"
        radiobutton_pos_mm["justify"] = "center"
        radiobutton_pos_mm["text"] = "中中"
        radiobutton_pos_mm.place(x=340, y=320, width=90, height=30)

        radiobutton_pos_rm = tk.Radiobutton(self, variable=self.gv_watermark_pos, value=6)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_pos_rm["font"] = ft
        radiobutton_pos_rm["fg"] = "#333333"
        radiobutton_pos_rm["justify"] = "right"
        radiobutton_pos_rm["text"] = "右中"
        radiobutton_pos_rm.place(x=550, y=320, width=90, height=30)

        radiobutton_pos_ld = tk.Radiobutton(self, variable=self.gv_watermark_pos, value=7)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_pos_ld["font"] = ft
        radiobutton_pos_ld["fg"] = "#333333"
        radiobutton_pos_ld["justify"] = "left"
        radiobutton_pos_ld["text"] = "左下"
        radiobutton_pos_ld.place(x=130, y=360, width=90, height=25)

        radiobutton_pos_md = tk.Radiobutton(self, variable=self.gv_watermark_pos, value=8)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_pos_md["font"] = ft
        radiobutton_pos_md["fg"] = "#333333"
        radiobutton_pos_md["justify"] = "center"
        radiobutton_pos_md["text"] = "中下"
        radiobutton_pos_md.place(x=340, y=360, width=90, height=30)

        radiobutton_pos_rd = tk.Radiobutton(self, variable=self.gv_watermark_pos, value=9)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_pos_rd["font"] = ft
        radiobutton_pos_rd["fg"] = "#333333"
        radiobutton_pos_rd["justify"] = "right"
        radiobutton_pos_rd["text"] = "右下"
        radiobutton_pos_rd.place(x=550, y=360, width=90, height=30)

        # 水印偏移X
        label_offset_x = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_offset_x["font"] = ft
        label_offset_x["fg"] = "#333333"
        label_offset_x["justify"] = "right"
        label_offset_x["text"] = "水印偏移X："
        label_offset_x.place(x=20, y=420, width=90, height=30)

        self.entry_offset_x = tk.Entry(self)
        self.entry_offset_x["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.entry_offset_x["font"] = ft
        self.entry_offset_x["fg"] = "#333333"
        self.entry_offset_x["justify"] = "center"
        self.entry_offset_x.place(x=130, y=420, width=150, height=30)

        # 水印偏移Y
        label_offset_y = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_offset_y["font"] = ft
        label_offset_y["fg"] = "#333333"
        label_offset_y["justify"] = "right"
        label_offset_y["text"] = "水印偏移Y："
        label_offset_y.place(x=380, y=420, width=90, height=30)

        self.entry_offset_y = tk.Entry(self)
        self.entry_offset_y["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.entry_offset_y["font"] = ft
        self.entry_offset_y["fg"] = "#333333"
        self.entry_offset_y["justify"] = "center"
        self.entry_offset_y.place(x=490, y=420, width=150, height=30)

        # 图像/水印大小
        label_72 = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_72["font"] = ft
        label_72["fg"] = "#333333"
        label_72["justify"] = "right"
        label_72["text"] = "图片/水印："
        label_72.place(x=20, y=480, width=90, height=30)

        self.entry_zoom = tk.Entry(self)
        self.entry_zoom["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.entry_zoom["font"] = ft
        self.entry_zoom["fg"] = "#333333"
        self.entry_zoom["justify"] = "center"
        self.entry_zoom["text"] = "3"
        self.entry_zoom.place(x=130, y=480, width=150, height=30)

        label_630 = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_630["font"] = ft
        label_630["fg"] = "#333333"
        label_630["justify"] = "center"
        label_630["text"] = "/1"
        label_630.place(x=280, y=480, width=35, height=30)

        # 不透明度
        label_268 = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_268["font"] = ft
        label_268["fg"] = "#333333"
        label_268["justify"] = "right"
        label_268["text"] = "不透明度："
        label_268.place(x=380, y=480, width=90, height=30)

        self.entry_opacity = tk.Entry(self)
        self.entry_opacity["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.entry_opacity["font"] = ft
        self.entry_opacity["fg"] = "#333333"
        self.entry_opacity["justify"] = "center"
        self.entry_opacity.place(x=490, y=480, width=150, height=30)

        # 输出格式
        label_output_ext = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_output_ext["font"] = ft
        label_output_ext["fg"] = "#333333"
        label_output_ext["justify"] = "right"
        label_output_ext["text"] = "输出图像格式："
        label_output_ext.place(x=20, y=540, width=90, height=30)

        radiobutton_output_source = tk.Radiobutton(self, variable=self.gv_output_ext_type, value=1)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_output_source["font"] = ft
        radiobutton_output_source["fg"] = "#333333"
        radiobutton_output_source["justify"] = "left"
        radiobutton_output_source["text"] = "同源格式"
        radiobutton_output_source.place(x=130, y=540, width=90, height=30)

        radiobutton_output_png = tk.Radiobutton(self, variable=self.gv_output_ext_type, value=2)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_output_png["font"] = ft
        radiobutton_output_png["fg"] = "#333333"
        radiobutton_output_png["justify"] = "center"
        radiobutton_output_png["text"] = "PNG"
        radiobutton_output_png.place(x=340, y=540, width=90, height=30)

        radiobutton_output_jpg = tk.Radiobutton(self, variable=self.gv_output_ext_type, value=3)
        ft = tkFont.Font(family='Times', size=10)
        radiobutton_output_jpg["font"] = ft
        radiobutton_output_jpg["fg"] = "#333333"
        radiobutton_output_jpg["justify"] = "right"
        radiobutton_output_jpg["text"] = "JPG"
        radiobutton_output_jpg.place(x=550, y=540, width=90, height=30)

        # 图像文件目录
        label_54 = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        label_54["font"] = ft
        label_54["fg"] = "#333333"
        label_54["justify"] = "right"
        label_54["text"] = "图片文件目录："
        label_54.place(x=20, y=600, width=90, height=30)

        self.entry_image_dir = tk.Entry(self)
        self.entry_image_dir["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.entry_image_dir["font"] = ft
        self.entry_image_dir["fg"] = "#333333"
        self.entry_image_dir["justify"] = "left"
        self.entry_image_dir.place(x=130, y=600, width=400, height=30)

        button_choose_image_dir = tk.Button(self)
        button_choose_image_dir["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button_choose_image_dir["font"] = ft
        button_choose_image_dir["fg"] = "#000000"
        button_choose_image_dir["justify"] = "center"
        button_choose_image_dir["text"] = "..."
        button_choose_image_dir.place(x=560, y=600, width=84, height=30)
        button_choose_image_dir["command"] = self.button_choose_image_dir_command

        # 生成水印图片
        button_add_watermark = tk.Button(self)
        button_add_watermark["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button_add_watermark["font"] = ft
        button_add_watermark["fg"] = "#000000"
        button_add_watermark["justify"] = "center"
        button_add_watermark["text"] = "生成水印图片"
        button_add_watermark.place(x=260, y=660, width=165, height=30)
        button_add_watermark["command"] = self.button_add_watermark_command

        self.text_log = tk.Text(self)  # 日志框
        self.text_log.place(x=20, y=700, width=660, height=80)

    # 选择水印文件夹
    def button_choose_watermark_dir_command(self):
        select_dir = tk.filedialog.askopenfilename(title='水印文件', filetypes=[('png', '*.png')])
        select_dir = os.path.dirname(select_dir)
        if len(select_dir) > 0:
            self.set_watermark_dir(select_dir)
            self.set_watermark_index(0)

    def button_choose_image_dir_command(self):
        select_dir = tk.filedialog.askopenfilename(title='图像文件',
                                                   filetypes=[('jpg', '*.jpg'), ('png', '*.png'), ('all', '*.*')])
        select_dir = os.path.dirname(select_dir)
        if len(select_dir) > 0:
            self.set_image_dir(select_dir)

    def button_add_watermark_command(self):
        self.load_form_val()
        if len(self.image_dir) < 2:
            messagebox.showwarning('注意', '图片路径不能为空！')
            return
        selection = self.listbox_watermark_img.curselection()
        if not selection:
            messagebox.showwarning('注意', '请选择水印！')
            return
        if self.watermark_opacity > 1 or self.watermark_opacity < 0:
            messagebox.showwarning('注意', '不透明度应该介于0到1之间！')
            return
        self.watermark_path = os.path.join(self.watermark_dir,
                                           self.listbox_watermark_img.get(selection[0]))
        self.add_watermark_dir(self.image_dir)

    # 读取水印文件
    def load_watermark(self, dir):
        # 清空
        self.listbox_watermark_img.delete(0, tk.END)
        if not os.path.isdir(dir):
            return
        i = 0
        for filename in os.listdir(dir):
            filepath = os.path.join(dir, filename)
            if os.path.isfile(filepath):
                watermakr_filepath = os.path.basename(filepath)
                ext = os.path.splitext(watermakr_filepath)[1].lower()
                if ext == '.png':
                    i = i + 1
                    self.listbox_watermark_img.insert(i, watermakr_filepath)

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
                    self.listbox_watermark_img.insert(i, watermakr_filepath)

    def load_default_config(self):
        self.set_watermark_dir(get_config(get_config_filename(), 'watermark', 'dir'))
        self.set_watermark_index(get_config(get_config_filename(), 'watermark', 'index'))
        # pos
        pos = get_config(get_config_filename(), 'watermark', 'pos')
        if len(pos) == 0:
            pos = self.watermark_pos
        self.gv_watermark_pos.set(pos)
        # offset_x
        offset_x = get_config(get_config_filename(), 'watermark', 'offset_x')
        if len(offset_x) == 0:
            offset_x = self.watermark_offset_x
        self.entry_offset_x.insert(0, offset_x)
        # offset_y
        offset_y = get_config(get_config_filename(), 'watermark', 'offset_y')
        if len(offset_y) == 0:
            offset_y = self.watermark_offset_y
        self.entry_offset_y.insert(0, offset_y)
        #  zoom
        zoom = get_config(get_config_filename(), 'watermark', 'zoom')
        if len(zoom) == 0:
            zoom = self.watermark_zoom
        self.entry_zoom.delete(0, tk.END)
        self.entry_zoom.insert(0, zoom)
        #  opacity
        opacity = get_config(get_config_filename(), 'watermark', 'opacity')
        if len(opacity) == 0:
            opacity = self.watermark_opacity
        self.entry_opacity.delete(0, tk.END)
        self.entry_opacity.insert(0, opacity)
        # ext_type
        ext_type = get_config(get_config_filename(), 'output', 'ext_type')
        if len(ext_type) == 0:
            ext_type = self.output_ext_type
        self.gv_output_ext_type.set(ext_type)

    def save_default_config(self):
        set_config(get_config_filename(), 'watermark', 'dir', self.watermark_dir)
        set_config(get_config_filename(), 'watermark', 'index', self.watermark_index)
        set_config(get_config_filename(), 'watermark', 'pos', self.watermark_pos)
        set_config(get_config_filename(), 'watermark', 'offset_x', self.watermark_offset_x)
        set_config(get_config_filename(), 'watermark', 'offset_y', self.watermark_offset_y)
        set_config(get_config_filename(), 'watermark', 'zoom', self.watermark_zoom)
        set_config(get_config_filename(), 'watermark', 'opacity', self.watermark_opacity)
        set_config(get_config_filename(), 'output', 'ext_type', self.output_ext_type)

    def set_watermark_dir(self, watermark_dir):
        self.watermark_dir = watermark_dir
        self.entry_watermark_dir.delete(0, tk.END)
        self.entry_watermark_dir.insert(0, self.watermark_dir)
        self.entry_watermark_dir["text"] = self.watermark_dir
        self.load_watermark(self.watermark_dir)

    def set_image_dir(self, image_dir):
        self.image_dir = image_dir
        self.entry_image_dir.delete(0, tk.END)
        self.entry_image_dir.insert(0, self.image_dir)

    def set_watermark_index(self, index=0):
        if self.listbox_watermark_img.size() == 0:
            return
        if len(index) == 0:
            index = 0
        self.watermark_index = index
        self.listbox_watermark_img.select_set(index)

    def load_form_val(self):
        self.watermark_pos = int(self.gv_watermark_pos.get())
        self.watermark_index = self.listbox_watermark_img.curselection()[0]
        self.watermark_offset_x = int(self.entry_offset_x.get())
        self.watermark_offset_y = int(self.entry_offset_y.get())
        self.watermark_zoom = int(self.entry_zoom.get())
        self.watermark_opacity = float(self.entry_opacity.get())
        self.output_ext_type = int(self.gv_output_ext_type.get())

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
                    if self.output_ext_type == 1:
                        out_ext = ext
                    elif self.output_ext_type == 2:
                        out_ext = '.png'
                    elif self.output_ext_type == 2:
                        out_ext = '.jpg'
                    out_path = os.path.join(out_dir, os.path.splitext(base_filename)[0] + out_ext)
                    # print(out_path)
                    add_watermark(watermark_path=self.watermark_path, image_path=filepath, out_path=out_path,
                                  zoom=self.watermark_zoom, pos=self.watermark_pos, offset_x=self.watermark_offset_x,
                                  offset_y=self.watermark_offset_y,
                                  opacity=self.watermark_opacity, out_ext=out_ext)
                    self.write_log_to_text(str(i) + '-[' + filepath + ']')
                    self.refresh_from()
        self.write_log_to_text('======添加水印完成，共添加' + str(i) + '个文件======')
        self.write_log_to_text('文件输出路径' + out_dir)
        self.save_default_config()
        messagebox.showinfo('信息', '添加水印完成，共添加' + str(i) + '个文件,水印文件输出路径' + out_dir)

    def refresh_from(self):
        # print('refresh_from')
        # self.text_log.insert(tk.END, '1')
        self.after(1000, self.refresh_from)  # 这里的100单位为毫秒

    def write_log_to_text(self, logmsg):
        global LOG_LINE_NUM
        current_time = get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 5:
            self.text_log.insert(tk.END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.text_log.delete(1.0, 2.0)
            self.text_log.insert(tk.END, logmsg_in)

    def show_about_author(self):
        messagebox.showinfo('关于', 'This program is developed for Flyany.\n\rzlj20@163.com\n\r' + self.VER)


def gui_start():
    gwindowsMain = WindowsMain()


if __name__ == "__main__":
    gui_start()
