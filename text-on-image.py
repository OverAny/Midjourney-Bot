from PIL import Image, ImageDraw, ImageFont
import os
from os import listdir
import csv 

def add_text_to_image(img_path):
    # Open the image
    img = Image.open(img_path)

    # text on image
    text = os.path.splitext(img_path)[0]
    text = text.replace('attachments-split/blue-bananas35_', '')
    id = text.split('.')[0]


    #only the first 10
 

    print(id)

    with open("prompts/Ron_prompt_list.csv", 'r') as file:
        reader = csv.reader(file)
        print(reader)
        zzz = None
        for row in csv.reader(file):
            print(row[0])
            print(id)
            if row[0] == id:
                print("IN")
                zzz = row
                break

        interestingrows=zzz
        text = interestingrows[1]
        name = interestingrows[2]
    # Create an ImageDraw objec
    draw = ImageDraw.Draw(img)

    # Define the font and size
    font = ImageFont.truetype("arial.ttf", 18)

    # Get the size of the image
    width, height = img.size

    # Calculate the position of the text
    text_width, text_height = draw.textsize(text, font)
    text_x = width - text_width - 10
    text_y = height - text_height - 10
    
    # rectangle = Image.new("RGB", (width, 30), (255, 255, 255))

    # Add the rectangle to the bottom of the image
    # img.paste(rectangle, (0, height))

    # Draw the text on the image
    draw.text((text_x, text_y), text, font=font, fill=(144, 238, 144))

    print(name)
    # Save the modified image
    img_path = img_path.replace('attachments-split/', '')
    img.save("attachments-text/" + name)

# Example usage
folder_dir = "attachments"

for images in os.listdir(folder_dir):
    print("1")
    # check if the image ends with png
    if (images.endswith(".png")):
        print(images)
        add_text_to_image("attachments-split/" + images)

