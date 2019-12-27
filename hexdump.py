import argparse
import string


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    if args.file:
        blockOffset = 0
        lastLine = 0
        with open(args.file, 'rb') as inputFile:
            with open(args.file+".dat", 'w') as outputFile:
                while True:
                    data = inputFile.read(16)
                    if len(data) == 0:
                        #print("{:08x}".format(blockOffset + len(data)))
                        break

                    PIPE = "|" #chr(124)
                    unprintable = ""
                    for i in data:
                        if (i < 32 or i > 126):
                            unprintable += '.'
                        else:
                            unprintable += chr(i)

                    result = "{:08x}".format(blockOffset) + "  "
                    for j in data[:8]:
                        result += "".join("{:02x}".format(j)) + " "
                        #print(" ",end='')
                    result += " "
                    # print(" ",end='')
                    for j in data[8:]:
                        result += "".join("{:02x}".format(j)) + " "
                        #print(" ",end='')
                    result += " "

                    if len(data) % 16 != 0:
                        result += "   " * (16 - len(data))
                        result += PIPE
                        result += unprintable
                        result += PIPE
                        print(result)
                        print("{:08x}".format(blockOffset + len(data)))
                        lastLine = 0
                        break
                    else:
                        result += PIPE
                        result += unprintable
                        result += PIPE
                        print(result)
                        lastLine = 1

                    outputFile.write(result + '\n')
                    blockOffset += 16

                if lastLine == 1:
                    print("{:08x}".format(blockOffset + len(data)))

    else:
        print ("please provide input, and output file if you want to save it to the file\n")

if __name__ == '__main__':
    Main()
