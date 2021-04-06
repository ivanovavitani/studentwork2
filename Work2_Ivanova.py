import gdal
from osgeo import ogr
import ogr
import pprint
import json as js
# Функция открытия shp-файла, определение геометрии и проекции
def get_ref_and_geom():
    data = ogr.Open('./parking_wgs84.shp')
    layer = data.GetLayer(0)
    feature = layer.GetNextFeature()
    # Определяется проекция
    geom_ref = feature.GetGeometryRef()
    spatialRef = geom_ref.GetSpatialReference()
    type = geom_ref.GetGeometryName()
    return print("Тип геометрии \n", type), \
           print("Проекция \n", spatialRef)


# Функция преобразования геометрии в форматы wkt и prj
def geom():
    data = ogr.Open('./parking_wgs84.shp')
    layer = data.GetLayer(0)
    spatialRef = layer.GetSpatialRef()
    with open('file_wkt.wkt', 'w') as file:
        file.write(spatialRef.ExportToWkt())
    with open('file_prj.prj', 'w') as file:
        file.write(spatialRef.ExportToWkt())

get_ref_and_geom()
geom()