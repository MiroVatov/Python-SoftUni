band_members_dict = {}
band_stage_time = {}

bands_total_stage_time = 0
while True:
    command = input()
    if command == "start of concert":
        break

    token = command.split("; ")
    action = token[0]

    if action == "Add":
        band_name = token[1]
        band_members = token[2].split(", ")
        if band_name not in band_members_dict:
            band_members_dict[band_name] = band_members
        else:
            for member in band_members:
                if member not in band_members_dict[band_name]:
                    band_members_dict[band_name].append(member)

    elif action == "Play":
        band_name = token[1]
        time = int(token[2])
        if band_name not in band_stage_time:
            band_stage_time[band_name] = time
        else:
            band_stage_time[band_name] += time
        bands_total_stage_time += time

print(f"Total time: {bands_total_stage_time}")

sorted_bands_time = dict(sorted(band_stage_time.items(),key=lambda x:(-x[1],x[0])))

for b, t in sorted_bands_time.items():
    print(f"{b} -> {t}")

band_to_show = input()

print(band_to_show)
for k in band_members_dict[band_to_show]:

    print(f"=> {k}")

