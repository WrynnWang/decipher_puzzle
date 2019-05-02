from base32_to_int_map import *

def base32_to_int():
    with open("raw_string.txt", 'r') as file:

        # loading raw string
        raw_data = file.read()
        # get ride of newline char
        data = raw_data.replace('\n', '')

        # open a new file and write decoded int chars in this file by lines
        with open("int_data.txt", 'a') as new_data:
            for i in data:

                # ignore the padding char
                if i == '=':
                    continue
                new_data.write(base32_to_int_map[i] + '\n')

            new_data.close()

        file.close()