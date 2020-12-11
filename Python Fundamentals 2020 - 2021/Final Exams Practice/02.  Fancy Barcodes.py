import re

number_of_inputs = int(input())

for i in range(number_of_inputs):
    command = input()
    product_group = ''
    pattern = r'(^[@]{1}[#]+)([A-Z][A-Z|a-z|0-9]{4,}[A-Z])([@]{1}[#]+$)'
    matches = re.match(pattern, command)
    
    if matches is not None:
        for w in matches.group():
            if w.isdigit():
                product_group += w
        if len(product_group) == 0:
            product_group = "00"
            print(f"Product group: 00")
        else:
            print(f"Product group: {product_group}")

    else:
        print(f"Invalid barcode")
