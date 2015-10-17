import os
import re

fin = open("data/input.c", "r")
fout = open("data/output.c", "w")

source = fin.read(os.path.getsize("data/input.c"))

# dword_DEADBEEF = 1; -> WRITE_DWORD(0xDEADBEEF, 1);
source = re.sub(r"(byte|dword)_([a-zA-Z0-9]+) = (.+?);", lambda p: r"WRITE_"+p.group(1).upper()+"(0x"+p.group(2)+", "+p.group(3).strip()+");", source)

# &dword_DEADBEEF -> ((DWORD*)0xDEADBEEF)
source = re.sub(r"&(byte|dword)_([a-zA-Z0-9]+)", lambda p: r"(("+p.group(1).upper() + "*)0x"+p.group(2) + ")", source)
source = re.sub(r"&(unk|stru)_([a-zA-Z0-9]+)", lambda p: r"((void*)0x"+p.group(2) + ")", source)

source = re.sub(r"(byte|dword)_([a-zA-Z0-9]+)", lambda p: r"READ_"+p.group(1).upper()+"(0x"+p.group(2)+")", source)

source = re.sub(r"(off)_([a-zA-Z0-9]+)", lambda p: r"(*((void**)0x"+p.group(2) + "))", source)

print(source)

fout.write(source)
