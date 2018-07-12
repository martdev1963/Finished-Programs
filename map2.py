import folium
import pandas

#---------------------------------------------------------------------------------------
# This program posted on my Github minus the excess commenting...Name: world_map.py
# Code now contains a map base layer object
# a polygon layer obejct
# and a marker layer object
# a lambda inline function...at line of code: 45
#---------------------------------------------------------------------------------------

# data object
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
# function for determining the color of the markers
def color_producer(elevation):
    if elevation < 1000: # under 1000 meters
        return 'green'
    elif 1000 <= elevation < 3000: # between 1000 and under 3000 meters
        return 'orange'
    else:
        return 'red' # greater than 3000 meters

# map base layer object
map = folium.Map(location=[28.121198, -82.022581], zoom_start=10, tiles="Mapbox Bright") # the map initially goes to these coordinates and zoom level when it loads...
# circle maker layer object fgv for volcano elevation data
fgv = folium.FeatureGroup(name="Volcanoes") # this bundles all 62 volcanoes into one group and/or object...otherwise you'd have 62 buttons on the webpage for volcanoes


for lt, ln, el in zip(lat, lon, elev): #zip() method allows you to iterate multiple variables simultaneously
    #print(type(el))                                                                                                     function call returns whats expected...a string type
    #fg.add_child(folium.Marker(location=[lt, ln], popup="Elevation is: "+str(el)+ " meters high", icon=folium.Icon(color=color_producer(el))))
    # keep adding characteristics or features to the map...via the fg object
    # circleMarker layer (elevation) object
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup="Elevation is: "+str(el)+ " meters high",
    fill_color=color_producer(el), color = 'grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

# Polygon layer object....code below color's the polygons...
# GeoJson code below breaks the CircleMarker popup attribute code above....the markers' popup attribute no longer works...
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'red' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'blue' if 20000000 <= x['properties']['POP2005'] < 30000000 else 'black '})) # dictionary with its key,value pair

#  ---------------------------------------------------------------------------------------------------------------------------
#  note: you may get a blank webpage if there are quotes ('') in the strings....to avoid this change the popup argument to:
#  popup=folium.Popup(str(el).parse_html=True)
#  However for simple strings like elevation values this is not a problem since there are no quotes in them.
#  ---------------------------------------------------------------------------------------------------------------------------

# code below is outside the forloop
map.add_child(fgv) # adding volcano elevation marker layer object to map
map.add_child(fgp) # adding geojson population polygon layer object to map
map.add_child(folium.LayerControl()) # adding the layercontrol to the map object....the LayerControl() method now sees the fgv and fgp layer objects...

map.save("Map2.html")


"""This is a working code above...

>>> l = lambda x: x**2
>>> l
<function <lambda> at 0x10c97a950>

>>> l(5)
25
>>> l(10)
100

"""

#len(lat)
"""
>>> len(lat)
62

for i, j in zip([1,2,3], [4,5,6]):
    print(i, "and", j)


ERROR:

Martins-iMac:mapping martinbatista$ python3 map2.py <------running map2.py
Traceback (most recent call last):
  File "map2.py", line 17, in <module>
    fg.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color='green')))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/folium/map.py", line 653, in __init__
    self.add_child(popup)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/branca/element.py", line 100, in add_child
    name = child.get_name()
AttributeError: 'float' object has no attribute 'get_name'
"""
