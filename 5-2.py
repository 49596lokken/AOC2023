f = open("5.txt").read().splitlines()


ans = 0
f 

seeds1 = [int(i) for i in f[0].removeprefix("seeds: ").split(" ")]
seedranges = [(seeds1[2*i],seeds1[2*i] + seeds1[2*i+1]-1) for i in range(len(seeds1)//2)]




seed_soil = f[f.index("seed-to-soil map:")+1:f.index("soil-to-fertilizer map:")-1]
soil_fert = f[f.index("soil-to-fertilizer map:")+1:f.index("fertilizer-to-water map:")-1]
fert_water = f[f.index("fertilizer-to-water map:")+1:f.index("water-to-light map:")-1]
water_light = f[f.index("water-to-light map:")+1:f.index("light-to-temperature map:")-1]
light_temp = f[f.index("light-to-temperature map:")+1:f.index("temperature-to-humidity map:")-1]
temp_humid = f[f.index("temperature-to-humidity map:")+1:f.index("humidity-to-location map:")-1]
humid_location = f[f.index("humidity-to-location map:")+1:]


def mapRange(r, map):
    for line in map:
        line = [int(i) for i in line.split(" ")]
        if r[0] >= line[1] and r[0] < line[1] + line[2]:
            # We are in the mapping
            if r[1] < line[1] + line[2]:
                # The range given is completely within the mapping
                return [(r[0] - line[1] + line[0], r[1] - line[1] + line[0])]
            else:
                # The range exceeds the mapping
                out = [(r[0] - line[1] + line[0], line[0] + line[2]-1)]
                out.extend(mapRange((line[1] + line[2], r[1]), map))
                return out
    for line in map:
        line = [int(i) for i in line.split(" ")]
        if r[1] >= line[1] and r[1] <= line[1] + line[2]:
            #The upper bound is in the mapping
            return [(r[0], line[1]-1), (line[0], r[1] + line[0]-line[1])]
    return [r]

def do_map(ranges, map):
    out = []
    for r in ranges:
        out.extend(mapRange(r, map))
    return out

maps = [seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_location]

soil = do_map(seedranges, seed_soil)
fert = do_map(soil, soil_fert)
water = do_map(fert, fert_water)
light = do_map(water, water_light)
temp = do_map(light, light_temp)
humid = do_map(temp, temp_humid)
location = do_map(humid, humid_location)

print(min(i[0] for i in location))