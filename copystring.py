def copy_string(src, dest, index=0):
    if index < len(src):
        dest += src[index]
        return copy_string(src, dest, index + 1)
    else:
        return dest
source_string = input("Enter a string to copy: ")
destination_string = copy_string(source_string, "")
print(f"Copied string: {destination_string}")
