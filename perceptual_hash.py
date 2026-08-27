from PIL import Image
import imagehash

filename = r"hhOoYZtHBqQi3d-dmxcGooXKTbiT3HJ2-eNsE7HNtKg.mp4"

image = Image.open(filename)

print("dHash:", imagehash.dhash(image))
print("aHash:", imagehash.average_hash(image))