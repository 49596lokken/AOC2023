f = open("5.txt").read().splitlines()



ans = 0
f 

seeds = [int(i) for i in f[0].removeprefix("seeds: ").split(" ")]


seed_soil = f[f.index("seed-to-soil map:")+1:f.index("soil-to-fertilizer map:")-1]
soil_fert = f[f.index("soil-to-fertilizer map:")+1:f.index("fertilizer-to-water map:")-1]
fert_water = f[f.index("fertilizer-to-water map:")+1:f.index("water-to-light map:")-1]
water_light = f[f.index("water-to-light map:")+1:f.index("light-to-temperature map:")-1]
light_temp = f[f.index("light-to-temperature map:")+1:f.index("temperature-to-humidity map:")-1]
temp_humid = f[f.index("temperature-to-humidity map:")+1:f.index("humidity-to-location map:")-1]
humid_location = f[f.index("humidity-to-location map:")+1:]

def do_map(start, map):
    for line in map:
        a = [int(i) for i in line.split(" ")]
        if start in range(a[1],a[1] + a[2]):
            return a[0] - a[1] +  start
    
    return start

locs = []
for seed in seeds:
    soil = do_map(seed, seed_soil)
    fert = do_map(soil, soil_fert)
    water = do_map(fert, fert_water)
    light = do_map(water, water_light)
    temp = do_map(light, light_temp)
    humid = do_map(temp, temp_humid)
    location = do_map(humid, humid_location)

    locs.append(location)

print(min(locs))
