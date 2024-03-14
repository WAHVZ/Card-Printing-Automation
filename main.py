from PIL import Image, ImageDraw, ImageFont
import os

# Get the full path to the image file
image_path = os.path.join("C:/Users/Wali/Desktop/idk/", "vis.png")

# Load certificate template
certificate_template = Image.open(image_path)
draw = ImageDraw.Draw(certificate_template)

# font_size = 20  # Adjust the font size as needed
font_path = os.path.join("C:/Users/Wali/Desktop/idk/", "FutuBd.ttf")
enhanced_font = ImageFont.truetype(font_path, 60)


# Input
name = str(input("Enter Name: "))
designation = str(input("Enter designation: "))
company = str(input("Enter company name: "))

# Array of name, designation, and company
names = [name, designation, company]

name_string = "{:^20}".format(names[0])
print(name_string)
certificate = certificate_template.copy()
draw_cert = ImageDraw.Draw(certificate)

# Customize the position, font size, and color as needed
draw_cert.text((300, 600), name_string, font=enhanced_font, fill="black")

designation = "{:^20}".format(names[1])
print(designation)
draw_cert.text((300, 750), designation, font=enhanced_font, fill="black")  # write designation

company = "{:^20}".format(names[2])
print(company)
draw_cert.text((300, 900), company, font=enhanced_font, fill="black")  # write company

# Save each certificate with a unique name
certificate.save(f"{names[0]}_certificate.png")

print("Certificates generated successfully.")
