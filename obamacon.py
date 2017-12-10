from PIL import Image

# RGB values for recoloring.
dark_blue = (0, 51, 76)
red = (217, 26, 33)
light_blue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
my_image = Image.open("polar_bear.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.
intensity_list = []


def main():
    for i in image_list:
        intensity = i[0] + i[1] + i[2]
        intensity_list.append(intensity)

    for j in intensity_list:
        if intensity_list[j] < 182:
            recolored.append(dark_blue)
        elif intensity_list[j] >= 182 and intensity_list[j] < 364:
            recolored.append(red)
        elif intensity_list[j] >= 364 and intensity_list[j] < 546:
            recolored.append(light_blue)
        elif intensity_list[j] >= 546:
            recolored.append(yellow)

main()

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
