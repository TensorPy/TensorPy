from tensorpy import image_base

classifications = image_base.classify_folder_images('./images')
print("*** Displaying Image Classification Results as a list: ***")
for classification in classifications:
    print classification
