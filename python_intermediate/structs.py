#program to demostrate the struct module

import struct
converted_bytes = struct.pack('3i',1,2,3)
print(struct.unpack('3i', converted_bytes))
