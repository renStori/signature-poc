## poc.py
```python
coords = [(77, 327), (76, 328), (77, 328), (79, 328), (85, 328), (104, 328), (113, 328), (120, 327), (122, 324), (122, 316), (121, 300), (112, 279), (99, 258), (87, 242), (80, 233), (78, 231), (77, 230), (77, 231), (83, 238), (99, 255), (120, 274), (137, 286), (152, 292), (165, 294), (171, 290), (174, 275), (174, 248), (170, 222), (164, 205), (161, 194), (159, 190), (165, 190), (184, 199), (215, 213), (249, 223), (273, 227), (289, 226), (298, 215), (296, 185), (278, 145), (255, 112), (238, 92)]

# Convert the coordinates list to a big integer (prefixed with `111`)
big_number = from_coords_to_int(coords)

# Convert that big number to a base62 string
b62 = int_to_base62(big_number)

# Convert back the base62 string to an int
back_big_number = base62_to_int(b62)

assert back_big_number == big_number, "FAIL"

# Convert that int to a list of coordinates
back_coords = from_int_to_coords(back_big_number)

assert coords == back_coords, "FAIL"
```