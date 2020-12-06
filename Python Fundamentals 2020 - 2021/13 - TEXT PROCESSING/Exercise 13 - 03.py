file_path = input().split("\\")

token = file_path[-1].split(".")

filename = token[-2:1]
extension = token[-1::]

print(f"File name: {''.join(filename)}")
print(f"File extension: {''.join(extension)}")

