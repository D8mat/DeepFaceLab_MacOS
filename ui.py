import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), 'scripts')


def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if not os.path.exists(script_path):
        messagebox.showerror('Error', f'Script not found: {script_path}')
        return
    try:
        subprocess.run(['bash', script_path], check=True)
        messagebox.showinfo('Success', f'{script_name} finished successfully.')
    except subprocess.CalledProcessError as err:
        messagebox.showerror('Error', f'Error while running {script_name}:\n{err}')


root = tk.Tk()
root.title('DeepFaceLab MacOS UI')
root.resizable(False, False)

# Image extraction section
extract_frame = ttk.LabelFrame(root, text='Image Extraction from Video')
extract_frame.pack(fill='x', padx=10, pady=5)

ttk.Button(extract_frame, text='Extract data_src', command=lambda: run_script('2_extract_images_from_video_data_src.sh')).pack(side='left', padx=5, pady=5)

ttk.Button(extract_frame, text='Extract data_dst', command=lambda: run_script('3_extract_images_from_video_data_dst.sh')).pack(side='left', padx=5, pady=5)

# Face extraction section
faces_frame = ttk.LabelFrame(root, text='Face Extraction from Images')
faces_frame.pack(fill='x', padx=10, pady=5)

ttk.Button(faces_frame, text='Data_src faces (S3FD)', command=lambda: run_script('4.1_data_src_extract_faces_S3FD.sh')).pack(side='left', padx=5, pady=5)

ttk.Button(faces_frame, text='Data_dst faces (S3FD)', command=lambda: run_script('5.1_data_dst_extract_faces_S3FD.sh')).pack(side='left', padx=5, pady=5)

# Training section
train_frame = ttk.LabelFrame(root, text='Training')
train_frame.pack(fill='x', padx=10, pady=5)

ttk.Button(train_frame, text='Train Quick96', command=lambda: run_script('6_train_Quick96.sh')).pack(side='left', padx=5, pady=5)

ttk.Button(train_frame, text='Train SAEHD', command=lambda: run_script('6_train_SAEHD.sh')).pack(side='left', padx=5, pady=5)

# Merging section
merge_frame = ttk.LabelFrame(root, text='Merging')
merge_frame.pack(fill='x', padx=10, pady=5)

ttk.Button(merge_frame, text='Merge Quick96', command=lambda: run_script('7_merge_Quick96.sh')).pack(side='left', padx=5, pady=5)

ttk.Button(merge_frame, text='Merge SAEHD', command=lambda: run_script('7_merge_SAEHD.sh')).pack(side='left', padx=5, pady=5)

root.mainloop()
