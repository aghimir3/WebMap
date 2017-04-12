import folium
import pandas


df = pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()], zoom_start = 6, tiles = 'Stamen Terrain')

def color(elev):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV']) - min(df['ELEV']))/3)
    if elev in range(minimum,minimum+step):
        markerColor = 'green'
    elif elev in range(minimum+step,minimum + step*2):
        markerColor = 'orange'
    else:
        markerColor='red'
    return markerColor

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    folium.Marker(location = [lat, lon], popup= name,icon =folium.Icon(color= color(elev))).add_to(map)

map.save('USVolcanoes.html')
