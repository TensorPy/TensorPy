from tensorpy import image_base

result = image_base.classify("https://raw.githubusercontent.com/mdmintz/TensorPy/master/sample_images/happy_animal.jpg")
print("\nBest match classification:\n%s\n" % result)
