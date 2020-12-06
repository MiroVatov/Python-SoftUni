import re
import itertools

initial_text = input()
res2 = re.findall(r'[^,\s]+', initial_text)
# res = [c.strip() for c in initial_text.split(',') if not c.isspace()]
demon_health = 0
demons_dict = {}
demon_name = ''
digits = []
for i in range(len(res2)):
    for s in res2[i]:
        if not s.isdigit() and s != "+" and s != "-" and s != "*" and s != "/" and s != ".":
            demon_health += ord(s)
        demon_name += s

    demons_dict[demon_name] = [demon_health]
    demon_health = 0
    demon_name = ''

demons_damage_lst = []

for ind in range(len(res2)):
    demon_damage = 0

    digits_pattern = r'([-|+]?[0-9]+\.[0-9]+)|([-|+]?[0-9]+)'
    digits_match = re.compile(digits_pattern)
    for k, v in re.findall(digits_match, str(res2[ind])):
        if v == '':
            demon_damage += float(k)
        elif k == '':
            demon_damage += float(v)
    symbols_pattern = r'([\*])|([\/])'
    symbols_match = re.compile(symbols_pattern)
    for st, xe in re.findall(symbols_match, str(res2[ind])):
        if xe == "/":
            demon_damage = demon_damage / 2
        elif st == "*":
            demon_damage *= 2
    demons_damage_lst.append(demon_damage)

for fr, va in itertools.zip_longest(demons_dict, demons_damage_lst):
    demons_dict[fr] += [va]

sorted_demons_dict = dict(sorted(demons_dict.items(),key=lambda x: x[0]))

for f_key, f_val in sorted_demons_dict.items():
    print(f"{f_key} - ", end='')
    print(f"{f_val[0]} health", end=", ")
    print(f"{f_val[1]:.2f} damage")

