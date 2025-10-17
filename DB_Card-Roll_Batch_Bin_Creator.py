#!/usr/bin/env python
# DaVinci Resolve Script: Batch Bin Creator by Daniel Bañuelos
# Creates a series of numbered bins (folders) in the currently selected Media Pool folder.

import sys
from sys import platform

# This code checks your OS and adds the correct path for the DaVinci Resolve API
if platform == "darwin": # Mac OS X
    resolve_loc = '/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules'
elif platform == "win32": # Windows
    resolve_loc = r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules'
elif platform.startswith("linux"): # Linux
    resolve_loc = '/opt/resolve/Developer/Scripting/Modules'
else:
    print("Unsupported platform.")
    sys.exit()

sys.path.insert(1, resolve_loc)

import DaVinciResolveScript as dvr_script
import tkinter as tk
from tkinter import messagebox

def get_user_input_from_dialog():
    """
    Creates a single, custom tkinter dialog to get all user settings at once.
    """
    dialog = tk.Tk()
    dialog.title("Batch Bin Creator Settings")
    dialog.attributes('-topmost', True) # Keep the window on top of Resolve

    # This dictionary will hold the results
    results = {}

    def on_create():
        # Retrieve values from the widgets and store them
        try:
            results['num_bins'] = int(num_bins_var.get())
            results['start_index'] = int(start_index_var.get())
            results['cam_letter'] = cam_letter_var.get().strip().upper()
            results['num_digits'] = int(num_digits_var.get())

            # Validate camera letter
            if len(results['cam_letter']) != 1 or not results['cam_letter'].isalpha():
                messagebox.showerror("Invalid Input", "Camera Letter must be a single alphabet character.", parent=dialog)
                return
            
            dialog.destroy() # Close the dialog
        except ValueError:
            messagebox.showerror("Invalid Input", "Please ensure all number fields contain valid numbers.", parent=dialog)

    def on_cancel():
        dialog.destroy() # Close without saving results

    main_frame = tk.Frame(dialog, padx=15, pady=15)
    main_frame.pack()

    # --- Input Fields ---
    # Number of Bins
    tk.Label(main_frame, text="Folders to Create:").grid(row=0, column=0, sticky="w", pady=5)
    num_bins_var = tk.StringVar(value='10')
    tk.Spinbox(main_frame, from_=1, to=999, textvariable=num_bins_var, width=10).grid(row=0, column=1, sticky="w")

    # Starting Index
    tk.Label(main_frame, text="Starting Index:").grid(row=1, column=0, sticky="w", pady=5)
    start_index_var = tk.StringVar(value='1')
    tk.Spinbox(main_frame, from_=0, to=99999, textvariable=start_index_var, width=10).grid(row=1, column=1, sticky="w")

    # Camera Letter
    tk.Label(main_frame, text="Camera Letter:").grid(row=2, column=0, sticky="w", pady=5)
    cam_letter_var = tk.StringVar(value='A')
    tk.Entry(main_frame, textvariable=cam_letter_var, width=12).grid(row=2, column=1, sticky="w")
    
    # Number of Digits
    tk.Label(main_frame, text="Number of Digits:").grid(row=3, column=0, sticky="w", pady=5)
    num_digits_var = tk.StringVar(value='3')
    tk.Spinbox(main_frame, from_=2, to=5, textvariable=num_digits_var, width=10).grid(row=3, column=1, sticky="w")

    # --- Buttons ---
    button_frame = tk.Frame(main_frame, pady=10)
    button_frame.grid(row=4, column=0, columnspan=2)
    tk.Button(button_frame, text="Create", command=on_create, width=10).pack(side="left", padx=5)
    tk.Button(button_frame, text="Cancel", command=on_cancel, width=10).pack(side="left", padx=5)

    dialog.mainloop()
    return results

def create_roll_bins():
    """
    Main function to connect to Resolve and create bins based on user input.
    """
    try:
        resolve = dvr_script.scriptapp("Resolve")
        projectManager = resolve.GetProjectManager()
        project = projectManager.GetCurrentProject()
        mediaPool = project.GetMediaPool()
    except Exception:
        messagebox.showerror("Connection Error", "Could not connect to DaVinci Resolve. Please ensure the application is running.")
        return

    if not project:
        messagebox.showerror("Error", "No project is currently open.")
        return

    # Get all inputs from the single dialog window
    user_inputs = get_user_input_from_dialog()

    # Proceed only if the user clicked "Create" and provided valid inputs
    if not user_inputs:
        print("Operation cancelled by the user.")
        return

    # --- Process Input and Create Bins ---
    num_bins = user_inputs['num_bins']
    start_index = user_inputs['start_index']
    cam_letter = user_inputs['cam_letter']
    num_digits = user_inputs['num_digits']

    parent_folder = mediaPool.GetCurrentFolder()
    if not parent_folder:
        messagebox.showerror("Error", "Please select a folder in the Media Pool first.")
        return
    
    print(f"Target folder: '{parent_folder.GetName()}'")
    print("--- Starting Bin Creation ---")
    created_count = 0

    for i in range(num_bins):
        current_index = start_index + i
        padded_number = str(current_index).zfill(num_digits)
        bin_name = f"{cam_letter}{padded_number}"
        
        new_bin = mediaPool.AddSubFolder(parent_folder, bin_name)
        if new_bin:
            print(f"Successfully created bin: {bin_name}")
            created_count += 1
        else:
            print(f"Warning: Could not create bin '{bin_name}'. It might already exist.")

    print("--- Script finished! ---")
    if created_count > 0:
        messagebox.showinfo("Success", f"Successfully created {created_count} of {num_bins} bins.")

if __name__ == "__main__":
    create_roll_bins()
