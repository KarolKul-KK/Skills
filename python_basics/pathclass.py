from pathlib import Path

#ABsolute path
#/user/local/bin MACOS
#Relative path

path = Path()
for file in path.glob('*.txt'):
    print(file)
