import folium
from folium.plugins import MarkerCluster
import os
import json

# Assuming the locator.py file is in the project folder (CS210_PROJ)
folder_path = os.path.dirname(os.path.realpath(__file__))

# Corrected path to the images folder
image_folder_path = os.path.join(folder_path, 'resources', 'images')
json_file_path = os.path.join(folder_path, 'sources', 'files', 'gps_info.json')

with open(json_file_path, 'r') as json_file:
    gps_info_dict = json.load(json_file)

# create a map object
turkey_center = [39.9334, 32.8597]
mymap = folium.Map(location=turkey_center, zoom_start=6)

# Create Marker Cluster
marker_cluster = MarkerCluster(name="Markers Demo").add_to(mymap)

for filename, info in gps_info_dict.items():
    if 'GPSInfo' in info and '2' in info['GPSInfo'] and '4' in info['GPSInfo']:
        lat_deg, lat_min, lat_sec = info['GPSInfo']['2']
        lon_deg, lon_min, lon_sec = info['GPSInfo']['4']

        # Check if the latitude and longitude information is present
        if lat_deg and lon_deg:
            # Convert degrees, minutes, seconds to decimal degrees
            lat = lat_deg[0] + lat_min[0] / 60.0 + lat_sec[0] / lat_sec[1] / 3600.0
            lon = lon_deg[0] + lon_min[0] / 60.0 + lon_sec[0] / lon_sec[1] / 3600.0

            # Adjust coordinates based on direction (N/S, E/W)
            if info['GPSInfo']['1'] == 'S':
                lat = -lat
            if info['GPSInfo']['3'] == 'W':
                lon = -lon

            # Create a Marker for each GPS location
            photo_path = "resources/images/" + filename

            folder_path = os.path.dirname(os.path.realpath(__file__))

            image_folder_path = os.path.join(folder_path, 'resources', 'images').replace("\\", "/")
            current_image_path = os.path.join(image_folder_path, filename).replace("\\", "/")
            #print("XXXXXXXXXXXXXXXXXXXXXXX:", current_image_path)
            if os.path.exists(photo_path):
                #print(filename, " ", photo_path)
                popup_content = f"<b>Filename:</b> {filename}<br>" \
                                f"<b>DateTime:</b> {info.get('DateTime', '')}<br>" \
                                f"<img loading='lazy' src='{current_image_path}' width='200'></a>"

                folium.Marker(location=[lat, lon],
                              popup=folium.Popup(popup_content, max_width=300),
                              tooltip=f"DateTime: {info.get('DateTime', '')}").add_to(marker_cluster)

# Layer control for turning Marker Cluster on/off
folium.LayerControl().add_to(mymap)

# Save the map object as html
output_html = os.path.join(folder_path, 'sources', 'files', 'gps_visualization_with_cluster_and_photo_popup.html')
mymap.save(output_html)

print(f' {output_html}')
print(image_folder_path)