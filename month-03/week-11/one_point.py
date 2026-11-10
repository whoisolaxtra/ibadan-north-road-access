
from pyproj import Transformer

# Create a coordinate transformer
to_utm = Transformer.from_crs(
    "EPSG:4326",
    "EPSG:32631",
    always_xy=True
)

# Transform longitude and latitude into UTM coordinates
x, y = to_utm.transform(3.8964, 7.4443)

print("UTM easting:", round(x, 1), "northing:", round(y, 1))
