import csv
import tkinter as tk
from tkinter import filedialog

def read_csv(file_path, columns):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Print out the column names for debugging
        print(f"Columns in {file_path}: {reader.fieldnames}")
        data = []
        for row in reader:
            print(f"Row: {row}")  # Debugging: print each row
            data.append({col: row[col].strip() for col in columns})
        return data

def save_csv(file_path, data, fieldnames):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Step 1: Get ADUsers files
    ad_file1 = filedialog.askopenfilename(title="Select the first ADUsers .csv file")
    ad_file2 = filedialog.askopenfilename(title="Select the second ADUsers .csv file")

    # Step 2: Combine ADUsers lists
    ad_users1 = read_csv(ad_file1, ['GivenName', 'Surname'])
    ad_users2 = read_csv(ad_file2, ['GivenName', 'Surname'])
    combined_ad_users = {f"{user['GivenName']} {user['Surname']}" for user in ad_users1 + ad_users2}
    combined_ad_users = [{'GivenName': name.split()[0], 'Surname': name.split()[1]} for name in combined_ad_users]

    save_path = filedialog.asksaveasfilename(title="Save the combined ADUsers file", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    save_csv(save_path, combined_ad_users, ['GivenName', 'Surname'])

    # Step 3: Get EntraID files
    entra_file1 = filedialog.askopenfilename(title="Select the first EntraID .csv file")
    entra_file2 = filedialog.askopenfilename(title="Select the second EntraID .csv file")

    # Step 4: Extract unique 'User' names from EntraID files
    entra_users1 = read_csv(entra_file1, ['User'])
    entra_users2 = read_csv(entra_file2, ['User'])
    unique_entra_users = {user['User'] for user in entra_users1 + entra_users2}

    # Step 5: Compare ADUsers with EntraID users
    ad_usernames = {f"{user['GivenName']} {user['Surname']}" for user in combined_ad_users}
    common_users = [{'GivenName': name.split()[0], 'Surname': name.split()[1]} for name in ad_usernames if name in unique_entra_users]

    save_path = filedialog.asksaveasfilename(title="Save the comparison result file", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    save_csv(save_path, common_users, ['GivenName', 'Surname'])

if __name__ == "__main__":
    main()
