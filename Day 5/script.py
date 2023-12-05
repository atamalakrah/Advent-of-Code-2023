import re

file_path = "./input_file.txt"
mapping_array = []
mapping_dict = {}
current_map = ""
mapped_values = []
seed_list = []
soil_list = []
fertilizer_list = []
water_list = []
light_list = []
temp_list = []
humidity_list = []
location_list = []

def parse_line(line):
    line = re.sub(r'\n', '', line).lstrip().replace(":", "")
    mapping_array.append(line)


with open(file_path) as input_file:
    [parse_line(line) for line in input_file]

mapping_data = [m for m in mapping_array if m != ""]

for counter, m in enumerate(mapping_data):
    if "soil" in m or "map" in m:
        current_map = m
    elif "seeds" in m:
        map_data = m.split()
        current_map = map_data[0]
        map_data.remove(map_data[0])
        for j in map_data:
            seed_list.append(int(j))
    else:
        map_data = m.split()
        dest_range_start = int(map_data[0])
        source_range_start = int(map_data[1])
        map_range = int(map_data[2])
        mapping_dict[counter] = {"map_name":current_map, "dest_range_start":dest_range_start, "source_range_start":source_range_start, "map_range":map_range}

def list_conversion (origin_list, dest_list, map_name):
    dest_list.extend([None] * len(origin_list))
    for value in mapping_dict.values():
        if value["map_name"] == map_name:
            full_source_range = value["source_range_start"] + (value["map_range"] - 1)
            for counter, s in enumerate(origin_list):
                if value["source_range_start"] <= s <= full_source_range:
                    difference = value["dest_range_start"] - value["source_range_start"] 
                    #print(counter, s, difference, s + difference, value["map_name"], dest_list)
                    dest_list[counter] = s + difference
            for counter, d in enumerate(origin_list):
                if dest_list[counter] is None:
                    #print(counter, d, value["map_name"], dest_list)
                    dest_list[counter] = d

list_conversion(seed_list, soil_list, "seed-to-soil map")
print(soil_list)
list_conversion(soil_list, fertilizer_list, "soil-to-fertilizer map")
print(fertilizer_list)
list_conversion(fertilizer_list, water_list, "fertilizer-to-water map")
print(water_list)
list_conversion(water_list, light_list, "water-to-light map")
print(light_list)
list_conversion(light_list, temp_list, "light-to-temperature map")
print(temp_list)
list_conversion(temp_list, humidity_list, "temperature-to-humidity map")
print(humidity_list)
list_conversion(humidity_list, location_list, "humidity-to-location map")
print(location_list)
lowest_number = location_list[0]
for l in location_list: 
    if l < lowest_number:
        lowest_number = l

print(lowest_number)