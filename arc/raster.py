import arcpy

def vectorize(
        input_raster,
        output_features):
    """Converts an input raster into a polygon feature.

    args:
       input_raster str: Full path to the raster dataset being converted
       output_feature str: Full path the vector dataset being created
    returns:
       path of the output feature if successful
   """

   try:
       arcpy.RasterToPolygon_conversion(
           input_raster,
           output_features,
           simplify="NO_SIMPLIFY"
           )
   except arcpy.executeerror:
       return None

   return output_features

