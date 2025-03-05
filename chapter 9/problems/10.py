import os

oldname = "name.txt"
newname = "rename.txt"

os.rename(oldname,newname)

print(f"Renamed {oldname} to {newname}")