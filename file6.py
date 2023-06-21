import os

# os.removedirs("../sem4")
file_names = os.listdir("../sem4")
print(file_names)
for i in file_names:
     os.remove(f"../sem4/{i}")
     print("File removed successfully...")
os.removedirs("../sem4")
