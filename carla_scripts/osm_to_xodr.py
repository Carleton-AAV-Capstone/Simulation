# Read the .osm data
f = open("./carleton_university_map.osm", 'r')
osm_data = f.read()
f.close()

# Define the desired settings. In this case, default values.
settings = carla.Osm2OdrSettings()
# Set OSM road types to export to OpenDRIVE
settings.set_osm_way_types(["motorway", "motorway_link", "trunk", "trunk_link", "primary", "primary_link", "secondary", "secondary_link", "tertiary", "tertiary_link", "unclassified", "residential"])
# enable traffic light generation from OSM data
settings.generate_traffic_lights = True
# Convert to .xodr
xodr_data = carla.Osm2Odr.convert(osm_data, settings)

# save opendrive file
f = open("./carleton_university_map.xodr", 'w')
f.write(xodr_data)
f.close()
