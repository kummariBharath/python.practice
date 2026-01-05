def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        
        secret_codes.append(secret_code)

    return secret_codes
poem = input("enter your poem:\n")
poem2 =input("enter you poem:\n")
poem3 = input("enter your poem:\n")

print(pin_extractor([poem,poem2,poem3]))