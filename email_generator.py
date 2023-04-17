from typing import List

def generate_email(company_name: str, craft: str, name: str, image_numbers: List[int]) -> str:
    # Generate the text for image_numbers
    if len(image_numbers) == 1:
        image_text = "this image"
        here_text = "Here"
    else:
        image_text = "these images"
        # Create a list of "Here" based on the number of images and format it with proper commas and "and"
        here_text_list = ["Here"] * len(image_numbers)
        if len(here_text_list) > 2:
            here_text = ", ".join(here_text_list[:-1]) + ", and " + here_text_list[-1]
        else:
            here_text = " and ".join(here_text_list)
    
    # Generate the subject line
    subject_line = f"Subject: Permission to use {company_name} images for NCCER Curriculum"
    
    # Create the email body
    email_body = f"""{subject_line}

Hi {name},

I hope this email finds you well. My name is Adam Black, and I work as the Image Permissions Specialist for NCCER's Product Development department. As you may know, NCCER is a leading non-profit education foundation, offering over 70 craft areas in construction and maintenance curricula.

We're currently updating our {craft} Curricula and would be thrilled to use {image_text}, as it has been well-received by our students. The Request images can be found {here_text}.

In order to include this image in our updated materials, we'll need a signed permission and license form to provide our publisher. If you're interested in assisting us with this, I can send the form for your review and signature. Additionally, we'll need a high-resolution file of the image for both print and digital use. We will credit, "Courtesy of {company_name}" per your specification.

Please feel free to reach out if you have any questions, need further clarification, or would like to discuss this opportunity further.

Respectfully,
Adam Black
"""
    return email_body


# Example usage
company_name = "ABC Construction"
craft = "Carpentry"
name = "John Doe"
image_numbers = [1, 2, 3]

generated_email = generate_email(company_name, craft, name, image_numbers)
print(generated_email)

import tkinter as tk
from typing import List

def submit():
    company_name = entry_company_name.get()
    craft = entry_craft.get()
    name = entry_name.get()
    
    # Parse the number of image_numbers based on a single integer input
    num_images = int(entry_image_numbers.get().strip())
    image_numbers = list(range(1, num_images + 1))
    
    generated_email = generate_email(company_name, craft, name, image_numbers)
    text_generated_email.delete(1.0, tk.END)
    text_generated_email.insert(tk.END, generated_email)



root = tk.Tk()
root.title("Email Generator")

# Create labels and entries for input fields
label_company_name = tk.Label(root, text="Company Name:")
entry_company_name = tk.Entry(root)
label_craft = tk.Label(root, text="Craft:")
entry_craft = tk.Entry(root)
label_name = tk.Label(root, text="Name:")
entry_name = tk.Entry(root)
label_image_numbers = tk.Label(root, text="Image Numbers (comma-separated):")
entry_image_numbers = tk.Entry(root)

# Create text widget to display generated email
text_generated_email = tk.Text(root, height=20, width=80)

# Create submit button
button_submit = tk.Button(root, text="Generate Email", command=submit)

# Layout widgets in the window
label_company_name.pack()
entry_company_name.pack()
label_craft.pack()
entry_craft.pack()
label_name.pack()
entry_name.pack()
label_image_numbers.pack()
entry_image_numbers.pack()
text_generated_email.pack()
button_submit.pack()

# Start the tkinter event loop
root.mainloop()
