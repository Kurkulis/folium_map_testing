import folium

# Create map, centerpoint Kupittaankuja, Turku
m = folium.Map(location=[60.4472368, 22.2937716], zoom_start=12)

#Global tooltip
tooltip = 'Click For More'

# Create markers
folium.Marker([60.4472368, 22.2937716], 
              popup='My Home',
              tooltip = tooltip).add_to(m)

m.save('map.html')
