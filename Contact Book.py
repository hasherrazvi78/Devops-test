import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Initialize the contact list
contacts = []

def add_contact():
    name = simpledialog.askstring("Input", "Enter contact name:")
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email address:")
    address = simpledialog.askstring("Input", "Enter address:")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    refresh_contact_list()

def view_contacts():
    contact_list_window = tk.Toplevel(window)
    contact_list_window.title("Contact List")
    contact_list_window.geometry("400x300")

    tk.Label(contact_list_window, text="Contact List", font=('Arial', 14, 'bold')).pack(pady=10)

    listbox = tk.Listbox(contact_list_window, width=50, height=15)
    listbox.pack(pady=10)

    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search_query = simpledialog.askstring("Search", "Enter name or phone number to search:")
    if not search_query:
        return

    search_results = [contact for contact in contacts if search_query.lower() in contact['name'].lower() or search_query in contact['phone']]
    
    if not search_results:
        messagebox.showinfo("Search Result", "No contact found.")
        return

    search_results_window = tk.Toplevel(window)
    search_results_window.title("Search Results")
    search_results_window.geometry("400x300")

    tk.Label(search_results_window, text="Search Results", font=('Arial', 14, 'bold')).pack(pady=10)

    listbox = tk.Listbox(search_results_window, width=50, height=15)
    listbox.pack(pady=10)

    for contact in search_results:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    selected_contact_index = tk.IntVar()

    def show_contact_details():
        selected_index = listbox.curselection()
        if selected_index:
            contact = search_results[selected_index[0]]
            details = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
            messagebox.showinfo("Contact Details", details)

    tk.Button(search_results_window, text="View Details", command=show_contact_details).pack(pady=10)

def update_contact():
    contact_name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
    if not contact_name:
        return

    contact = next((c for c in contacts if c['name'].lower() == contact_name.lower()), None)
    if not contact:
        messagebox.showinfo("Update", "Contact not found.")
        return

    new_name = simpledialog.askstring("Update", "Enter new contact name:", initialvalue=contact['name'])
    new_phone = simpledialog.askstring("Update", "Enter new phone number:", initialvalue=contact['phone'])
    new_email = simpledialog.askstring("Update", "Enter new email address:", initialvalue=contact['email'])
    new_address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contact['address'])

    contact.update({"name": new_name, "phone": new_phone, "email": new_email, "address": new_address})
    refresh_contact_list()

def delete_contact():
    contact_name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
    if not contact_name:
        return

    global contacts
    contacts = [c for c in contacts if c['name'].lower() != contact_name.lower()]
    refresh_contact_list()

def refresh_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Create the main window
window = tk.Tk()
window.title("Contact Management System")
window.geometry("500x400")
window.configure(bg="#e0f7fa")

# Title Label
tk.Label(window, text="Contact Management System", bg="#e0f7fa", font=('Arial', 18, 'bold')).pack(pady=10)

# Contact List Display
contact_list_frame = tk.Frame(window, bg="#e0f7fa")
contact_list_frame.pack(pady=10)

contact_list = tk.Listbox(contact_list_frame, width=60, height=10)
contact_list.pack(side=tk.LEFT, fill=tk.BOTH)

# Buttons
button_frame = tk.Frame(window, bg="#e0f7fa")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Contact", command=add_contact, font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="View Contacts", command=view_contacts, font=('Arial', 12, 'bold')).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Search Contact", command=search_contact, font=('Arial', 12, 'bold')).grid(row=0, column=2, padx=10)
tk.Button(button_frame, text="Update Contact", command=update_contact, font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=10)
tk.Button(button_frame, text="Delete Contact", command=delete_contact, font=('Arial', 12, 'bold')).grid(row=1, column=1, padx=10)

# Run the Tkinter event loop
window.mainloop()
