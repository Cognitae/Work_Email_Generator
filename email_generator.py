import tkinter as tk
from tkinter import ttk, messagebox
from typing import List
import sys  # Import the sys module
import os   # Import the os module
import json

# Define three email body templates (template_1, template_2, template_3)
template_1 = """{subject_line}

Hi {name},

I hope this email finds you well. My name is Adam Black, and I work as the Image Permissions Specialist for NCCER's Product Development department. As you may know, NCCER is a leading non-profit education foundation, offering over 70 craft areas in construction and maintenance curricula.

We're currently updating our {craft} Curricula and would be thrilled to use {image_text}, as it has been well-received by our students. The Requested {imag_text} can be found {here_text} 

In order to include {image_text} our updated materials, we'll need a signed permission and license form to provide our publisher. If you're interested in assisting us with this, I can send the form for your review and signature. Additionally, we'll need a high-resolution file of the image for both print and digital use. We will credit, "Courtesy of {company_name}" per your specification.

Please feel free to reach out if you have any questions, need further clarification, or would like to discuss this opportunity further.

Respectfully,
Adam Black
"""

# Define two more templates (template_2 and template_3) with variations in text
template_2 = """{subject_line}

Dear {name},

I'm reaching out on behalf of NCCER's Product Development department. My name is Adam Black, and I serve as the Image Permissions Specialist. NCCER, a leading non-profit education foundation, is in the process of updating its curricula for over 70 craft areas in construction and maintenance.

As part of this effort, we're updating our {craft} Curricula and are excited about the possibility of including {image_text}. The {imag_text} we're interested in can be found {here_text}.

To proceed, we require a signed permission and license form for our publisher, as well as high-resolution image files for print and digital use. We're happy to credit the {imag_text} as "Courtesy of {company_name}" as specified by you.

Please let me know if you have any questions or if you'd like to discuss this further.

Best regards,
Adam Black
"""

template_3 = """{subject_line}

Hello {name},

My name is Adam Black, and I work with NCCER's Product Development team as the Image Permissions Specialist. NCCER is updating its curricula across more than 70 craft areas, and we're known for our dedication to high-quality education in construction and maintenance.

We're currently working on the {craft} Curricula and are very interested in using {image_text} in our materials. You can view the images in question {here_text}.

To include these {imag_text}, we'll need a completed permission and license form, as well as high-resolution image files suitable for print and digital formats. Image credit will be given as "Courtesy of {company_name}" according to your preferences.

If you have any questions or would like more information, please don't hesitate to reach out.

Sincerely,
Adam Black
"""

# Define a dictionary of templates
templates = {
    "Template 1": template_1,
    "Template 2": template_2,
    "Template 3": template_3
}

import tkinter as tk
from tkinter import ttk
from typing import List

# [TEMPLATE DEFINITIONS AND CODE]

# Function to convert inches to pixels (assuming standard DPI of 96)
def inches_to_pixels(inches, dpi=96):
    return int(inches * dpi)

root = tk.Tk()
root.title("Email Generator")

# Create notebook (tabbed layout)
notebook = ttk.Notebook(root)

# Create frames for each tab
email_generation_frame = ttk.Frame(notebook)
template_editing_frame = ttk.Frame(notebook)

# Add frames as tabs to the notebook
notebook.add(email_generation_frame, text="Email Generation")
notebook.add(template_editing_frame, text="Edit Templates")
# Determine the correct path for the resource file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load logo image (after defining email_generation_frame)
logo_image_path = resource_path("resources/cognitae.png")  # Use the resource_path function
logo_image = tk.PhotoImage(file=logo_image_path)
# Resize the logo to 1.5 inches x 1.5 inches
logo_size_in_inches = 1.5
logo_size_in_pixels = inches_to_pixels(logo_size_in_inches)
logo_image = logo_image.subsample(logo_image.width() // logo_size_in_pixels)

label_logo = tk.Label(email_generation_frame, image=logo_image)
label_logo.place(x=500, y=0)

# Create label and entry for "Company Name" (after defining email_generation_frame)
label_company_name = tk.Label(email_generation_frame, text="Company Name:")
entry_company_name = tk.Entry(email_generation_frame)


# Create label and entry for "Craft"
label_craft = tk.Label(email_generation_frame, text="Craft:")
entry_craft = tk.Entry(email_generation_frame)

# Create label and entry for "Name"
label_name = tk.Label(email_generation_frame, text="Name:")
entry_name = tk.Entry(email_generation_frame)

# Create label and entry for "Image Numbers"
label_image_numbers = tk.Label(email_generation_frame, text="Image Numbers:")
entry_image_numbers = tk.Entry(email_generation_frame)

# Create label and entry for "Module" parameter
label_module = tk.Label(email_generation_frame, text="Module:")
entry_module = tk.Entry(email_generation_frame)

# Adjust grid layout to accommodate labels and entries, and logo
label_company_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_company_name.grid(row=0, column=1, padx=10, pady=10, sticky="w")
label_craft.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_craft.grid(row=1, column=1, padx=10, pady=10, sticky="w")
label_name.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")
label_image_numbers.grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_image_numbers.grid(row=3, column=1, padx=10, pady=10, sticky="w")
label_module.grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_module.grid(row=4, column=1, padx=10, pady=10, sticky="w")
# Define the selected_template_var variable for radiobuttons
selected_template_var = tk.StringVar(value="Template 1")

# Create radiobuttons for selecting templates
for i, (template_name, template_text) in enumerate(templates.items()):
    rb = tk.Radiobutton(email_generation_frame, text=template_name, variable=selected_template_var, value=template_name)
    rb.grid(row=i+6, column=0, padx=10, pady=10, sticky="w", columnspan=2)

# Custom function to generate module sentence
def generate_module_sentence(here_text, module):
    if module:
        return f"{here_text} to use in our module on {module}."
    else:
        return f"{here_text}."

def submit():
    # Retrieve user inputs
    company_name = entry_company_name.get()
    craft = entry_craft.get()
    name = entry_name.get()
    module = entry_module.get().strip()
    num_images = int(entry_image_numbers.get().strip())
    image_numbers = list(range(1, num_images + 1))
    
    # Generate the subject line
    subject_line = f"Subject: Permission to use {company_name} images for NCCER {craft} Curriculum"
    
    # Determine the text based on the number of images
    if len(image_numbers) == 1:
        image_text = "this image"
        here_text = "Here"
        imag_text = "image"
    else:
        image_text = "these images"
        imag_text = "images"
        here_text_list = ["Here"] * len(image_numbers)
        if len(here_text_list) > 2:
            here_text = ", ".join(here_text_list[:-1]) + ", and " + here_text_list[-1]
        else:
            here_text = " and ".join(here_text_list)

    # Generate module sentence based on whether module is provided
    module_sentence = generate_module_sentence(here_text, module)
    
    # Retrieve the selected template and format it with actual values
    selected_template = templates[selected_template_var.get()]
    generated_email = selected_template.format(
        subject_line=subject_line,
        name=name,
        craft=craft,
        image_text=image_text,
        imag_text=imag_text,
        here_text=module_sentence,  # Use the module_sentence here
        company_name=company_name
    )
    text_generated_email.delete(1.0, tk.END)
    text_generated_email.insert(tk.END, generated_email)

# (5) Create text widgets for editing templates and Save buttons (in template_editing_frame) [NO CHANGES HERE]
# Create text widget to display generated email (in email_generation_frame)
text_generated_email = tk.Text(email_generation_frame, height=20, width=80)

# Create submit button (in email_generation_frame)
button_submit = tk.Button(email_generation_frame, text="Generate Email", command=submit)
text_generated_email.grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
button_submit.grid(row=9, column=0, padx=10, pady=10, sticky="w")

# (6) Add to layout in the template_editing_frame [NO CHANGES HERE]
# Layout widgets in the email_generation_frame
label_company_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_company_name.grid(row=0, column=1, padx=10, pady=10, sticky="w")
label_craft.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_craft.grid(row=1, column=1, padx=10, pady=10, sticky="w")
label_name.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")
label_image_numbers.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_image_numbers.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# File to store templates
TEMPLATES_FILE = "templates.json"

# Function to save templates to a file
def save_templates_to_file(templates):
    with open(TEMPLATES_FILE, 'w') as f:
        json.dump(templates, f)

# Function to load templates from a file
def load_templates_from_file():
    try:
        with open(TEMPLATES_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file does not exist, return the default templates
        return {
            "Template 1": template_1,
            "Template 2": template_2,
            "Template 3": template_3
        }

# Modify the save_template function
def save_template(template_name, text_widget):
    # Update the template in the templates dictionary
    templates[template_name] = text_widget.get(1.0, tk.END)
    # Save the updated templates to the file
    save_templates_to_file(templates)

# Load the templates from the file when the program starts
templates = load_templates_from_file()


# Create text widgets for editing templates and Save buttons (in template_editing_frame)
text_template_1 = tk.Text(template_editing_frame, height=8, width=80)
text_template_1.insert(tk.END, template_1)
button_save_template_1 = tk.Button(template_editing_frame, text="Save Template 1", command=lambda: save_template("Template 1", text_template_1))
text_template_2 = tk.Text(template_editing_frame, height=8, width=80)
text_template_2.insert(tk.END, template_2)
button_save_template_2 = tk.Button(template_editing_frame, text="Save Template 2", command=lambda: save_template("Template 2", text_template_2))
text_template_3 = tk.Text(template_editing_frame, height=8, width=80)
text_template_3.insert(tk.END, template_3)
button_save_template_3 = tk.Button(template_editing_frame, text="Save Template 3", command=lambda: save_template("Template 3", text_template_3))

# Add to layout in the template_editing_frame
text_template_1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
button_save_template_1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
text_template_2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
button_save_template_2.grid(row=3, column=0, padx=10, pady=10, sticky="w")
text_template_3.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
button_save_template_3.grid(row=5, column=0, padx=10, pady=10, sticky="w")


# [INSERT THE NEW CODE HERE]
def on_closing():
    if messagebox.askokcancel("Save changes", "Do you want to save changes to templates before closing?"):
        save_templates_to_file(templates)
    root.destroy()

# Modify the save_template function
def save_template(template_name, text_widget):
    # Update the template in the templates dictionary
    templates[template_name] = text_widget.get(1.0, tk.END)
    # Save the updated templates to the file
    save_templates_to_file(templates)
    messagebox.showinfo("Template Saved", f"{template_name} has been saved successfully.")
# Function to copy the generated email text to the clipboard
def copy_to_clipboard():
    # Retrieve the text from the text_generated_email widget
    generated_email_text = text_generated_email.get(1.0, tk.END)
    # Clear the clipboard and set the retrieved text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(generated_email_text)

# Create the "Copy" button and set its command to the copy_to_clipboard function
button_copy = tk.Button(email_generation_frame, text="Copy", command=copy_to_clipboard)
button_copy.grid(row=9, column=1, padx=10, pady=10, sticky="w")

# Grid the notebook to the root window
notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#Start the tkinter event loop
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
