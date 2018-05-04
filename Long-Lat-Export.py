'''
@Author = Stephen Winter
'''

import time
from pyproj import Proj, transform
import fiona
import re

num = 0

start = time.time()
with fiona.open("ENTER PATH TO SHAPE FILE","r") as test:
    with open('ENTER PATH TO OUTPUT TEXT FILE', 'w') as output:
        output.write("[Line_ID][Polygon]n")
        total = len(test)
        for one in test:
            
            data = str(one['geometry']['coordinates'])
            num+=1
            
            if(one['geometry']['type']=='MultiPolygon'):
                coordinates = 'MultiPolygon ((('
                data = data.replace(']]]','')
                data = data.replace(']]',']')
    
                test = re.split(']', data)
                for geo in test:
                    
                    geo1 = geo.replace('(', "")
                    geo2 = geo1[3:]
                    geo3 = geo2.replace('[', "")
                    geo4 = geo3.replace(']',"")
                    geo5 = geo4.split("), ")
                    
                        
                    for each in geo5:
                        each = each.replace(')', "")
                        each = str(each)
                        
                        a, b = each.split(', ')

                        
# Calculation to convert Easting, Northing to Longitude, Latitude...
# If Using Easting, Northing and need Long, Lat... Uncomment this section and run script.
                        
#                        v84 = Proj(proj="latlong",towgs84="0,0,0",ellps="WGS84")
#                        v36 = Proj(proj="latlong", k=0.9996012717, ellps="airy",
#                                towgs84="446.448,-125.157,542.060,0.1502,0.2470,0.8421,-20.4894")
#                        vgrid = Proj(init="world:bng")
#                        
#                        
#                        def ENtoLL84(easting, northing):
#                            """Returns (longitude, latitude) tuple
#                            """
#                            vlon36, vlat36 = vgrid(easting, northing, inverse=True)
#                            return transform(v36, v84, vlon36, vlat36)
#                        
#                        def LL84toEN(longitude, latitude):
#                            """Returns (easting, northing) tuple
#                            """
#                            vlon36, vlat36 = transform(v84, v36, longitude, latitude)
#                            return vgrid(vlon36, vlat36)
#                        
#                        
#                        if __name__ == '__main__':
#                            coords = ENtoLL84(a, b)
#                            coords = str(coords)
#                            a, b = coords.split(',')
#                            a = a[1:]
#                            b = b[:-1]
                        
                        coordinates = (coordinates  + a + ' ' + b + ',')
                    coordinates = coordinates[:-2]
                    coordinates = (coordinates + ',')    
                    
                coordinates = (coordinates[:-3])
                coordinates = (coordinates + ')')
                
            
            else:
                 coordinates = "Polygon ((" 
                 data = data.replace(']]', '')

                 test = re.split(']', data)
                 
                 for geo in test:
                    
                    geo1 = geo.replace('(', "")
                    geo2 = geo1[2:]
                
                    geo3 = geo2.replace('[', "")
                    geo4 = geo3.replace(']',"")
                    geo5 = geo4.split("), ")
                

                        
                    for each in geo5:
                        each = each.replace(')', "")
                        each = str(each)
                        
                        a, b = each.split(', ')
                        

# Calculation to convert Easting, Northing to Longitude, Latitude...
# If Using Easting, Northing and need Long, Lat... Uncomment this section and run script.
                        
#                        v84 = Proj(proj="latlong",towgs84="0,0,0",ellps="WGS84")
#                        v36 = Proj(proj="latlong", k=0.9996012717, ellps="airy",
#                                towgs84="446.448,-125.157,542.060,0.1502,0.2470,0.8421,-20.4894")
#                        vgrid = Proj(init="world:bng")
#                        
#                        
#                        def ENtoLL84(easting, northing):
#                            """Returns (longitude, latitude) tuple
#                            """
#                            vlon36, vlat36 = vgrid(easting, northing, inverse=True)
#                            return transform(v36, v84, vlon36, vlat36)
#                        
#                        def LL84toEN(longitude, latitude):
#                            """Returns (easting, northing) tuple
#                            """
#                            vlon36, vlat36 = transform(v84, v36, longitude, latitude)
#                            return vgrid(vlon36, vlat36)
#                        
#                        
#                        if __name__ == '__main__':
#                            coords = ENtoLL84(a, b)
#                            coords = str(coords)
#                            a, b = coords.split(',')
#                            a = a[1:]
#                            b = b[:-1]
                        
                        coordinates = (coordinates  + a + ' ' + b + ',')
                    coordinates = coordinates[:-1]
                    coordinates = coordinates + "),("
            
            coordinates = coordinates[:-2]
   
            if(one['geometry']['type']=='MultiPolygon'):
                coordinates = ('[' + str(num) + '][' + coordinates + ')))]\n')
        
            else:
                coordinates = ('[' + str(num) + '][' + coordinates + ')]\n')
            output.write(coordinates)
            
            if(num % 100 == 0):
                print(str(num) + ' of ' + str(total) + ' extracted')

end = time.time()
print(str(num) + ' of ' + str(total) + ' extracted')
print("\n\nExtraction completed in: " + str(end-start) + ' seconds')
