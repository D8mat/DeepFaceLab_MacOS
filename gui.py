#!/usr/bin/env python3
import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

ROOT = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(ROOT, 'scripts')


def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if not os.path.exists(script_path):
        messagebox.showerror("Error", f"Script not found: {script_name}")
        return
    try:
        subprocess.run(['bash', script_path], check=True)
    except subprocess.CalledProcessError as exc:
        messagebox.showerror("Error", f"Failed to run {script_name}\n{exc}")


root = tk.Tk()
root.title('DeepFaceLab MacOS GUI')

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Section: Extract images from video
frame_extract_images = ttk.Frame(notebook)
notebook.add(frame_extract_images, text='Extract Images')

ttk.Label(frame_extract_images, text='Extract frames from videos').pack(pady=5)
btn_src_vid = ttk.Button(frame_extract_images, text='Extract data_src video',
                         command=lambda: run_script('2_extract_images_from_video_data_src.sh'))
btn_dst_vid = ttk.Button(frame_extract_images, text='Extract data_dst video',
                         command=lambda: run_script('3_extract_images_from_video_data_dst.sh'))
btn_src_vid.pack(pady=2)
btn_dst_vid.pack(pady=2)

# Section: Face extraction
frame_extract_faces = ttk.Frame(notebook)
notebook.add(frame_extract_faces, text='Extract Faces')

ttk.Label(frame_extract_faces, text='Extract faces from images').pack(pady=5)
btn_src_face = ttk.Button(frame_extract_faces, text='Extract faces from data_src',
                          command=lambda: run_script('4.1_data_src_extract_faces_S3FD.sh'))
btn_dst_face = ttk.Button(frame_extract_faces, text='Extract faces from data_dst',
                          command=lambda: run_script('5.1_data_dst_extract_faces_S3FD.sh'))
btn_src_face.pack(pady=2)
btn_dst_face.pack(pady=2)

# Section: Training
frame_train = ttk.Frame(notebook)
notebook.add(frame_train, text='Training')

ttk.Label(frame_train, text='Train models').pack(pady=5)
btn_quick = ttk.Button(frame_train, text='Train Quick96',
                       command=lambda: run_script('6_train_Quick96.sh'))
btn_saehd = ttk.Button(frame_train, text='Train SAEHD',
                       command=lambda: run_script('6_train_SAEHD.sh'))
btn_quick.pack(pady=2)
btn_saehd.pack(pady=2)

# Section: Merge
frame_merge = ttk.Frame(notebook)
notebook.add(frame_merge, text='Merge')

ttk.Label(frame_merge, text='Merge faces to video').pack(pady=5)
btn_merge_quick = ttk.Button(frame_merge, text='Merge Quick96',
                             command=lambda: run_script('7_merge_Quick96.sh'))
btn_merge_saehd = ttk.Button(frame_merge, text='Merge SAEHD',
                             command=lambda: run_script('7_merge_SAEHD.sh'))
btn_merge_quick.pack(pady=2)
btn_merge_saehd.pack(pady=2)

root.mainloop()
