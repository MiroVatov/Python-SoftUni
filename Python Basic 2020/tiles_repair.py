ground_area = int(input())
tile_width = float(input())
tile_length = float(input())
bench_width = int(input())
bench_length = int(input())

bench_size = bench_width * bench_length
tile_size = tile_length * tile_width
ground_area_total = (ground_area * ground_area) - bench_size
tiles_needed = ground_area_total / tile_size
time_needed = tiles_needed * 0.2


print(tiles_needed)
print(time_needed)