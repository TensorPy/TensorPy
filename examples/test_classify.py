from tensorpy import image_base

result = image_base.classify('http://theonlinezoo.com/img/04/toz04142l.jpg')
print("\nBest match classification:\n%s\n" % result)
