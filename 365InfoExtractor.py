import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def select_file(file_type):
    file_path = filedialog.askopenfilename(filetypes=[(file_type.upper(), f"*.{file_type}")])
    return file_path

def save_file(content, file_type):
    file_path = filedialog.asksaveasfilename(defaultextension=file_type, filetypes=[(file_type.upper(), f"*.{file_type}")])
    if file_path:
        with open(file_path, 'w') as f:
            f.write(content)
        messagebox.showinfo("Success", f"File saved as {file_path}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Select the CSV files for the last two months
    messagebox.showinfo("Select File", "Select the log file for the first month")
    file_month1 = select_file('csv')
    messagebox.showinfo("Select File", "Select the log file for the second month")
    file_month2 = select_file('csv')

    # Read the CSV files
    df_month1 = pd.read_csv(file_month1)
    df_month2 = pd.read_csv(file_month2)

    # Extract unique user IDs from both months
    unique_users_month1 = set(df_month1['User ID'].unique())
    unique_users_month2 = set(df_month2['User ID'].unique())

    # Combine the unique user IDs from both months
    active_users = unique_users_month1.union(unique_users_month2)

    # Select the AD users xlsx file
    messagebox.showinfo("Select File", "Select the AD users file")
    ad_users_file = select_file('xlsx')
    
    # Read the list of all AD users
    ad_users = pd.read_excel(ad_users_file)
    all_ad_users = set(ad_users['User ID'].unique())

    # Identify inactive users
    inactive_users = all_ad_users - active_users

    # Convert inactive users to a string format for saving
    inactive_users_str = "\n".join(inactive_users)

    # Ask user to save the output as .txt or .csv
    file_type = messagebox.askquestion("Save As", "Save output as .txt or .csv?", icon='question', type='yesno')
    
    if file_type == 'yes':
        save_file(inactive_users_str, 'txt')
    else:
        inactive_users_df = pd.DataFrame(list(inactive_users), columns=['User ID'])
        save_file(inactive_users_df.to_csv(index=False), 'csv')

if __name__ == "__main__":
    main()
