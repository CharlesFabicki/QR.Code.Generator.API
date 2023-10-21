import requests
import tkinter as tk
from tkinter import filedialog


def generate_qr_code(data, filename):
    api_url = f"https://api.qrserver.com/v1/create-qr-code/?data={data}&size=300x300"
    response = requests.get(api_url)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        result_label.config(text=f"A QR code has been generated and saved as an image file: {filename}")
    else:
        result_label.config(text="Failed to generate QR code.")


def update_fields_visibility():
    selected_type = data_type_var.get()

    name_entry.pack_forget()
    email_entry.pack_forget()
    phone_entry.pack_forget()
    link_entry.pack_forget()
    text_entry.pack_forget()

    if selected_type == "Contact":
        name_entry.pack()
        email_entry.pack()
        phone_entry.pack()
    elif selected_type == "Link":
        link_entry.pack()
    elif selected_type == "Text":
        text_entry.pack()


def generate_button_click():
    update_fields_visibility()

    data_type = data_type_var.get()

    if data_type == "Contact":
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        data = f"MECARD:N:{name};EMAIL:{email};TEL:{phone};;"
    elif data_type == "Link":
        data = link_entry.get()
    elif data_type == "Text":
        data = text_entry.get()
    else:
        result_label.config(text="Unknown data type.")
        return

    output_filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if output_filename:
        generate_qr_code(data, output_filename)


def exit_button_click():
    root.destroy()


def on_entry_click(entry_widget, default_text):
    if entry_widget.get() == default_text:
        entry_widget.delete(0, "end")
        entry_widget.config(fg='white')


def on_focus_out(entry_widget, default_text):
    if entry_widget.get() == "":
        entry_widget.insert(0, default_text)
        entry_widget.config(fg='grey')


def data_type_selected(event):
    update_fields_visibility()


def show_start_screen():
    start_frame.pack(expand=True)

    start_label.pack(pady=50)
    instructions_label.pack(pady=20)
    start_button.pack()


def start_button_click():
    start_frame.pack_forget()
    name_entry.pack_forget()
    email_entry.pack_forget()
    phone_entry.pack_forget()
    link_entry.pack_forget()
    text_entry.pack_forget()


def hide_buttoms():
    name_entry.pack_forget()
    email_entry.pack_forget()
    phone_entry.pack_forget()
    link_entry.pack_forget()
    text_entry.pack_forget()


root = tk.Tk()
root.title("QR Code Generator")
root.configure(bg='black')
root.geometry("700x450")

start_frame = tk.Frame(root, bg='black', width=700, height=100)

start_label = tk.Label(start_frame, text="Welcome to QR Code Generator", bg='black', fg='white', font=("Helvetica", 25))
instructions_label = tk.Label(start_frame,
                              text="Instructions:\n1. Choose a data type from the dropdown menu.\n2. Fill in the required fields.\n3. Click 'Generate QR Code' to create the QR code.",
                              bg='black', fg='white', font=("Helvetica", 20))
start_button = tk.Button(start_frame, text="Get Started", command=start_button_click, bg='green', fg='white',
                         font=("Helvetica", 15))

start_label.pack(pady=50)
instructions_label.pack(pady=20)
start_button.pack(pady=50)
start_button.pack()

start_frame.pack(expand=True)

data_type_var = tk.StringVar(value="Contact")
tk.Label(root, text="", bg='black').pack()

data_type_label = tk.Label(root, text="Choose data type:", bg='black', fg='white', font=("Helvetica", 20))
data_type_optionmenu = tk.OptionMenu(root, data_type_var, "Contact", "Link", "Text", command=data_type_selected)
data_type_label.pack()
data_type_optionmenu.pack()

entry_bg_color = 'black'
entry_fg_color = 'white'
font_style = ("Helvetica", 25)

entry_width = 50

name_entry = tk.Entry(root, width=entry_width, bg=entry_bg_color, fg=entry_fg_color, font=font_style)
name_entry.insert(0, "Full Name")
name_entry.bind("<FocusIn>", lambda event: on_entry_click(name_entry, "Full Name"))
name_entry.bind("<FocusOut>", lambda event: on_focus_out(name_entry, "Full Name"))
name_entry.pack()

tk.Label(root, text="", bg='black').pack()

email_entry = tk.Entry(root, width=entry_width, bg=entry_bg_color, fg=entry_fg_color, font=font_style)
email_entry.insert(0, "Email Address")
email_entry.bind("<FocusIn>", lambda event: on_entry_click(email_entry, "Email Address"))
email_entry.bind("<FocusOut>", lambda event: on_focus_out(email_entry, "Email Address"))
email_entry.pack()

tk.Label(root, text="", bg='black').pack()

phone_entry = tk.Entry(root, width=entry_width, bg=entry_bg_color, fg=entry_fg_color, font=font_style)
phone_entry.insert(0, "Phone Number")
phone_entry.bind("<FocusIn>", lambda event: on_entry_click(phone_entry, "Phone Number"))
phone_entry.bind("<FocusOut>", lambda event: on_focus_out(phone_entry, "Phone Number"))
phone_entry.pack()

tk.Label(root, text="", bg='black').pack()

link_entry = tk.Entry(root, width=entry_width, bg=entry_bg_color, fg=entry_fg_color, font=font_style)
link_entry.insert(0, "Link")
link_entry.bind("<FocusIn>", lambda event: on_entry_click(link_entry, "Link"))
link_entry.bind("<FocusOut>", lambda event: on_focus_out(link_entry, "Link"))

link_entry.pack()

tk.Label(root, text="", bg='black').pack()
text_entry = tk.Entry(root, width=entry_width, bg=entry_bg_color, fg=entry_fg_color, font=font_style, )
text_entry.insert(0, "Enter Text")
text_entry.bind("<FocusIn>", lambda event: on_entry_click(text_entry, "Enter Text"))
text_entry.bind("<FocusOut>", lambda event: on_focus_out(text_entry, "Enter Text"))

text_entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_button_click, bg='green', fg='white',
                            width=entry_width, font=("Helvetica", 15))

result_label = tk.Label(root, text="", bg='black', fg='white')
result_label.pack()

exit_button = tk.Button(root, text="Exit", command=exit_button_click, bg='red', fg='white',
                        width=entry_width, font=("Helvetica", 15))

exit_button.pack(side="bottom")
generate_button.pack(side="bottom", pady=20)

hide_buttoms()
show_start_screen()

root.mainloop()
