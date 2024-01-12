filename = "videolist.txt"


with open("/Users/chinen/Downloads/videolist.txt", "r") as f:
    file_lines = ["".join(["file '", x.strip(), "'\n"]) for x in f.readlines()]
    
with open("/Users/chinen/Downloads/forffmpeg.txt", "w") as f:
    f.writelines(file_lines)