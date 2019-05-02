import subprocess
import os

def binary_to_two_digits_hex():
    with open("bin_string.txt", 'r') as bin_data:

        # load the whole binary string from the first line of the binary file
        for line in bin_data:
            whole_binary_string = line

        bin_data.close()

        # for each 8 digits of this binary string
        # convert to a 2 digits heximal number
        index = 0
        bin_str_length = len(whole_binary_string)
        bin_str_length -= bin_str_length%8
        # with open("eureka.txt", 'a') as final_data:
        final_string = ''
        while index < bin_str_length:

            # an 8 digits binary string
            this_binary_str = whole_binary_string[index:index+8]

            # a 2 digits heximal string
            this_hex = hex(int(this_binary_str, 2))[2:]

            # the string should be written into final file
            if(this_hex == '0'):
                hex_str = this_hex + "0 "
            else:
                hex_str = this_hex + ' '
            final_string += hex_str

            # each end of iteration index should plus 8
            index += 8

        final_string = "\"" + final_string[:-1] + "\""

        # generate a gcc file to echo string into gif file
        subprocess.call(["gcc", "eureka.c"])

        # write a bash command
        bash_command = "echo " + final_string +" | ./a.out > eureka.gif"

        # execute the final bash command to get a gif
        os.system(bash_command)
