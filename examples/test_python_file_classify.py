from tensorpy import image_base

result = image_base.classify_local_image("images/cat_animal.jpg")
print("\nBest match classification:\n%s\n" % result)
