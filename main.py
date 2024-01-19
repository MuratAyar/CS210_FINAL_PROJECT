import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import json

folder_path = r"resources\images"
output_path = r"sources\files"
gps_info_dict = {}

for filename in os.listdir(folder_path):
    if filename.lower().endswith('.jpg'):
        img_path = os.path.join(folder_path, filename)
        image = Image.open(img_path)
        exif = {}

        # Check if EXIF data is available
        if image._getexif():
            for tag, value in image._getexif().items():
                if tag in TAGS:
                    tag_name = TAGS[tag]
                    if tag_name == 'DateTimeOriginal' or tag_name == 'DateTimeDigitized':
                        exif['DateTime'] = value
                    elif tag == 34853:  # GPSInfo tag
                        gps_info = {}
                        for gps_tag, gps_value in value.items():
                            gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                            if gps_tag_name == 'GPSDateStamp':
                                gps_info[gps_tag_name] = gps_value
                            elif gps_tag_name == 'GPSTimeStamp':
                                gps_info[gps_tag_name] = tuple(map(float, gps_value))
                        exif['GPSInfo'] = gps_info

            if exif:
                gps_info_dict[filename] = exif

json_output_file = os.path.join(output_path, 'gps_info.json')
with open(json_output_file, 'w') as json_file:
    json.dump(gps_info_dict, json_file, indent=2, default=str)