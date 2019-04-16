import folium

m = folium.Map(location=[60.4472368, 22.2937716], zoom_start=12)

m.save('map.html')
