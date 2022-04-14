import arcpy
import pandas as pd


def get_attribute_values(
    layer: str,
    fields: list = None,
    as_pandas: bool = True):
    """Fetch attributes from an ESRI supported datasoure as a python object.

    Args:
        layer (str): Full path to the data source
        fields (list): list a subset of field names to include in the output. If not specified all fields will be returned.
        as_pandas (bool, optional): Returns the data as a pandas DataFrame rather than a list. Defaults to True.

    Returns:
        pandas.DataFrame: DataFrame of the requested fields
        list: List of data corresponding to the requested fields.
    """

    # If no subset of fields is specified collect all of the field names in the layer
    fields = fields if fields else [f.name for f in arcpy.ListFields(layer)]

    with arcpy.da.SearchCursor(layer, fields) as scur:
        if len(fields) == 1:
            # If only one field is requested return data as a 1d list
            data = [r[0] for r in scur]
        else:
            data = [r for r in scur]

    if as_pandas:
        df = pd.DataFrame(
            data,
            columns=fields)
        return df
    else:
        return data