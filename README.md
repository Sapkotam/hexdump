# hexdump
The hex dump is a view of data in hexadecimal format. It is the “Hello World” of digital forensics. The hex dump is a hexadecimal view of computer data, from RAM or from a computer file or storage device. Looking at a hex dump of data is usually done in the context of either debugging or reverse engineering.

Each full line represents 16 bytes. The first column is the offset (starting at zero; the second line starts at offset 0x00000010, 16 bytes into the file). The middle column is the byte values in hex. There is an extra space between the eighth and ninth byte. The final column is the the same bytes in so-called perusal format, enclosed in vertical bar. Perusal format means that bytes that represent printable ASCII characters are shown as those ASCII characters; all other bytes are replaced by a period ('.') (ie. any value that is not between 0x20 and 0x7E).
This program, will cover edge cases like: 1. empty inputs, 2. inputs with fewer than 16 bytes (that is, less than one full line of output), 3. inputs with an exact multiple of 16 bytes, 4. inputs with more than one line of output, 5. inputs with any/all of the printable ASCII characters, and 6. inputs with any/all of the non-printable ASCII characters.

to run:

hexdump filename 
