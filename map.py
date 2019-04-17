import folium
import os

# Create map, centerpoint Alicante, Spain
m = folium.Map(location=[38.3537, -0.49018499999999676], zoom_start=14)

#Global tooltip
tooltip = 'Click For More'

# Area data JSON
area = os.path.join('data', 'area.json')

# Create marker pointing to Universidad de Alicante
folium.Marker([38.3799,-0.5059360000000197], 
              popup='Universidad de Alicante',
              tooltip = tooltip,
              icon = folium.Icon(color='red')).add_to(m)

# Draw area from JSON
folium.GeoJson(area, name='living area').add_to(m)

m.save('map.html')
