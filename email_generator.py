import tkinter as tk
from tkinter import ttk
from typing import List

# Define three email body templates (template_1, template_2, template_3)
template_1 = """{subject_line}

Hi {name},

I hope this email finds you well. My name is Adam Black, and I work as the Image Permissions Specialist for NCCER's Product Development department. As you may know, NCCER is a leading non-profit education foundation, offering over 70 craft areas in construction and maintenance curricula.

We're currently updating our {craft} Curricula and would be thrilled to use {image_text}, as it has been well-received by our students. The Requested images can be found {here_text}.

In order to include this image in our updated materials, we'll need a signed permission and license form to provide our publisher. If you're interested in assisting us with this, I can send the form for your review and signature. Additionally, we'll need a high-resolution file of the image for both print and digital use. We will credit, "Courtesy of {company_name}" per your specification.

Please feel free to reach out if you have any questions, need further clarification, or would like to discuss this opportunity further.

Respectfully,
Adam Black
"""

# Define two more templates (template_2 and template_3) with variations in text
template_2 = """{subject_line}

Dear {name},

I'm reaching out on behalf of NCCER's Product Development department. My name is Adam Black, and I serve as the Image Permissions Specialist. NCCER, a leading non-profit education foundation, is in the process of updating its curricula for over 70 craft areas in construction and maintenance.

As part of this effort, we're updating our {craft} Curricula and are excited about the possibility of including {image_text}. The images we're interested in can be found {here_text}.

To proceed, we require a signed permission and license form for our publisher, as well as high-resolution image files for print and digital use. We're happy to credit the images as "Courtesy of {company_name}" as specified by you.

Please let me know if you have any questions or if you'd like to discuss this further.

Best regards,
Adam Black
"""

template_3 = """{subject_line}

Hello {name},

My name is Adam Black, and I work with NCCER's Product Development team as the Image Permissions Specialist. NCCER is updating its curricula across more than 70 craft areas, and we're known for our dedication to high-quality education in construction and maintenance.

We're currently working on the {craft} Curricula and are very interested in using {image_text} in our materials. You can view the images in question {here_text}.

To include these images, we'll need a completed permission and license form, as well as high-resolution image files suitable for print and digital formats. Image credit will be given as "Courtesy of {company_name}" according to your preferences.

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

# Function to save the edited templates [MODIFY FUNCTION]
def save_template(template_key, text_widget):
    templates[template_key] = text_widget.get(1.0, tk.END)

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

# (3) Create labels, entries, radio buttons, text widgets, and buttons for the email_generation_frame [NO CHANGES HERE]
# Create labels and entries for input fields (in email_generation_frame)
label_company_name = tk.Label(email_generation_frame, text="Company Name:")
entry_company_name = tk.Entry(email_generation_frame)
label_craft = tk.Label(email_generation_frame, text="Craft:")
entry_craft = tk.Entry(email_generation_frame)
label_name = tk.Label(email_generation_frame, text="Name:")
entry_name = tk.Entry(email_generation_frame)
label_image_numbers = tk.Label(email_generation_frame, text="Image Numbers (comma-separated):")
entry_image_numbers = tk.Entry(email_generation_frame)

# Create radio buttons for template selection (in email_generation_frame)
selected_template_var = tk.StringVar(value="Template 1")
for i, (template_name, template_text) in enumerate(templates.items()):
    rb = tk.Radiobutton(email_generation_frame, text=template_name, variable=selected_template_var, value=template_name)
    rb.grid(row=i+4, column=0, padx=10, pady=10, sticky="w", columnspan=2)  # span across two columns
    
# (4) Define the submit function after creating the necessary tkinter widgets
def submit():
    # Retrieve user inputs
    company_name = entry_company_name.get()
    craft = entry_craft.get()
    name = entry_name.get()
    num_images = int(entry_image_numbers.get().strip())
    image_numbers = list(range(1, num_images + 1))
    
    # Generate the subject line
    subject_line = f"Subject: Permission to use {company_name} images for NCCER Curriculum"
    
    # Determine the text based on the number of images
    if len(image_numbers) == 1:
        image_text = "this image"
        here_text = "Here"
    else:
        image_text = "these images"
        here_text_list = ["Here"] * len(image_numbers)
        if len(here_text_list) > 2:
            here_text = ", ".join(here_text_list[:-1]) + ", and " + here_text_list[-1]
        else:
            here_text = " and ".join(here_text_list)
    
    # Retrieve the selected template and format it with actual values
    selected_template = templates[selected_template_var.get()]
    generated_email = selected_template.format(
        subject_line=subject_line,
        name=name,
        craft=craft,
        image_text=image_text,
        here_text=here_text,
        company_name=company_name
    )
    text_generated_email.delete(1.0, tk.END)
    text_generated_email.insert(tk.END, generated_email)

# (5) Create text widgets for editing templates and Save buttons (in template_editing_frame) [NO CHANGES HERE]
# Create text widget to display generated email (in email_generation_frame)
text_generated_email = tk.Text(email_generation_frame, height=20, width=80)

# Create submit button (in email_generation_frame)
button_submit = tk.Button(email_generation_frame, text="Generate Email", command=submit)
text_generated_email.grid(row=7, column=0, columnspan=2, padx=10, pady=10)  # move to row 7
button_submit.grid(row=8, column=0, padx=10, pady=10, sticky="w")  # move to row 8

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

# Grid the notebook to the root window
notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#Start the tkinter event loop
root.mainloop()
