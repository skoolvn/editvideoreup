import tkinter as tk
from tkinter import ttk, filedialog, colorchooser

# Hàm chọn file video
def select_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
    if file_path:
        entry_video.delete(0, tk.END)
        entry_video.insert(0, file_path)

# Hàm chọn màu chữ hoặc khung
def choose_color():
    color_code = colorchooser.askcolor(title="Chọn màu")[1]
    return color_code

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Video Tools for Youtuber Pro - V1.0")
root.geometry("800x600")

# Tạo Notebook (tab container)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Tạo các tab
tab_edit = ttk.Frame(notebook)
tab_merge = ttk.Frame(notebook)
tab_livestream = ttk.Frame(notebook)
tab_info = ttk.Frame(notebook)

# Thêm tab vào Notebook
notebook.add(tab_edit, text="Edit Video")
notebook.add(tab_merge, text="Merge Video")
notebook.add(tab_livestream, text="Livestream")
notebook.add(tab_info, text="Thông tin")

# (1) Khu vực chọn video
frame_video = ttk.LabelFrame(tab_edit, text="Chọn Video")
frame_video.pack(pady=10, fill="x")

ttk.Label(frame_video, text="Video input:").pack(side="left", padx=5)
entry_video = ttk.Entry(frame_video, width=50)
entry_video.pack(side="left", padx=5)
ttk.Button(frame_video, text="Chọn Video", command=select_video).pack(side="left")

# (2) Thanh công cụ chỉnh sửa
frame_tools = ttk.LabelFrame(tab_edit, text="Công cụ chỉnh sửa")
frame_tools.pack(pady=10, fill="x")

# Cắt video
ttk.Label(frame_tools, text="Cắt video từ:").grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(frame_tools, width=10).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(frame_tools, text="đến").grid(row=0, column=2, padx=5, pady=5)
ttk.Entry(frame_tools, width=10).grid(row=0, column=3, padx=5, pady=5)

# Tốc độ phát
ttk.Label(frame_tools, text="Tốc độ video:").grid(row=1, column=0, padx=5, pady=5)
speed_scale = ttk.Scale(frame_tools, from_=0.5, to=2, orient="horizontal")
speed_scale.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

# Xoay & Lật video
ttk.Label(frame_tools, text="Xoay:").grid(row=1, column=2, padx=5, pady=5)
cmb_rotate = ttk.Combobox(frame_tools, values=["Không xoay", "90 độ", "180 độ", "270 độ"])
cmb_rotate.grid(row=1, column=3, padx=5, pady=5)
cmb_rotate.current(0)

ttk.Label(frame_tools, text="Lật:").grid(row=1, column=4, padx=5, pady=5)
cmb_flip = ttk.Combobox(frame_tools, values=["Không lật", "Lật ngang", "Lật dọc"])
cmb_flip.grid(row=1, column=5, padx=5, pady=5)
cmb_flip.current(0)

# Chỉnh sửa màu sắc
ttk.Label(frame_tools, text="Độ sáng:").grid(row=2, column=0, padx=5, pady=5)
ttk.Scale(frame_tools, from_=0, to=100, orient="horizontal").grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_tools, text="Bão hòa:").grid(row=2, column=2, padx=5, pady=5)
ttk.Scale(frame_tools, from_=0, to=100, orient="horizontal").grid(row=2, column=3, padx=5, pady=5)

# Thêm chữ
ttk.Label(frame_tools, text="Thêm chữ:").grid(row=3, column=0, padx=5, pady=5)
entry_text = ttk.Entry(frame_tools, width=30)
entry_text.grid(row=3, column=1, padx=5, pady=5)
ttk.Button(frame_tools, text="Chọn font").grid(row=3, column=2, padx=5, pady=5)
ttk.Label(frame_tools, text="Vị trí:").grid(row=3, column=3, padx=5, pady=5)
cmb_text = ttk.Combobox(frame_tools, values=["Trên Trái", "Trên Phải", "Dưới Trái", "Dưới Phải", "Trung Tâm"])
cmb_text.grid(row=3, column=4, padx=5, pady=5)
cmb_text.current(0)

# Thêm video
ttk.Label(frame_tools, text="Thêm video:").grid(row=4, column=0, padx=5, pady=5)

# Thêm khung
ttk.Label(frame_tools, text="Khung Size:").grid(row=5, column=0, padx=5, pady=5)
entry_border_width = ttk.Entry(frame_tools, width=5)
entry_border_width.grid(row=5, column=1, padx=5, pady=5)
ttk.Button(frame_tools, text="Chọn màu", command=choose_color).grid(row=5, column=2, padx=5, pady=5)
horizontal_frame = ttk.Scale(frame_tools, from_=0.5, to=2, orient="horizontal")
horizontal_frame.grid(row=5, column=3, columnspan=1, padx=5, pady=5)

#-------------------------------
frame_audio_effects = tk.Frame(tab_edit)
frame_audio_effects.pack(pady=5)
tk.Label(frame_audio_effects, text="Hiệu ứng Audio:").pack(side=tk.LEFT)
effect_noise = tk.BooleanVar()
effect_echo = tk.BooleanVar()
effect_reverb = tk.BooleanVar()
effect_loudnorm = tk.BooleanVar()
tk.Checkbutton(frame_audio_effects, text="Noise Reduction", variable=effect_noise).pack(side=tk.LEFT)
tk.Checkbutton(frame_audio_effects, text="Echo", variable=effect_echo).pack(side=tk.LEFT)
tk.Checkbutton(frame_audio_effects, text="Reverb", variable=effect_reverb).pack(side=tk.LEFT)
tk.Checkbutton(frame_audio_effects, text="Loudnorm", variable=effect_loudnorm).pack(side=tk.LEFT)
#-------------------------------

# (3) Khu vực cài đặt thông số
frame_settings = ttk.LabelFrame(tab_edit, text="Cài đặt xuất video")
frame_settings.pack(pady=10, fill="x")

# Chất lượng & Codec
ttk.Label(frame_settings, text="Codec:").grid(row=0, column=0, padx=5, pady=5)
cmb_codec = ttk.Combobox(frame_settings, values=["H.264", "H.265", "VP9"])
cmb_codec.grid(row=0, column=1, padx=5, pady=5)
cmb_codec.current(0)

ttk.Label(frame_settings, text="Bitrate:").grid(row=1, column=0, padx=5, pady=5)
ttk.Entry(frame_settings, width=10).grid(row=1, column=1, padx=5, pady=5)

# Tốc độ khung hình
ttk.Label(frame_settings, text="FPS:").grid(row=2, column=0, padx=5, pady=5)
cmb_fps = ttk.Combobox(frame_settings, values=["24", "30", "60"])
cmb_fps.grid(row=2, column=1, padx=5, pady=5)
cmb_fps.current(1)

# Nút lưu video
ttk.Button(frame_settings, text="Lưu Video").grid(row=3, column=0, columnspan=2, pady=10)

# Hiển thị cửa sổ
root.mainloop()
