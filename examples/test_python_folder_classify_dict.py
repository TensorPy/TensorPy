from tensorpy import image_base

dictionary = image_base.classify_folder_images('./images', return_dict=True)
print("*** Displaying Image Classification Results as dictionary: ***")
print dictionary
