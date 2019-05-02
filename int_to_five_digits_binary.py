def int_to_five_digits_binary():
    with open("int_data.txt", 'r') as file:

        #create a string variable to store all the binary string that converted in the next step
        whole_binary_string = ''

        for line in file:

            # convert each line from string to int
            number = int(line.replace('\n', ''))

            # convert each int number to 5 digits binary string
            # because the base32 map's range is 0~31 so the max binary number should be 11111
            # which is 5 digit, so we need to padding all the binary number with 5 digits
            bin_number = str(bin(number))[2:]
            bin_len = len(bin_number)
            if bin_len == 1:
                bin_number = "0000" + bin_number
            elif bin_len == 2:
                bin_number = "000" + bin_number
            elif bin_len == 3:
                bin_number = "00" + bin_number
            elif bin_len == 4:
                bin_number = "0" + bin_number
            else:
                pass

            whole_binary_string += bin_number

        file.close()

        # open a new file and write all 5 digits binary string into it
        with open("bin_string.txt", 'a') as bin_data:
            bin_data.write(whole_binary_string)

            bin_data.close()