import re
import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
def camel_to_snake(camel_str):
    for x in camel_str:
        snake_str = re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel_str)
    return snake_str.lower()

@transformer
def transform(data, *args, **kwargs):
    print('Preprocessing: rows with zero passagers:'+str(data['passenger_count'].isin([0]).sum()))
    print('Preprocessing: rows with zero trip distance:'+str(data['trip_distance'].isin([0]).sum()))
    
    #Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero.
    data= data[ (data['passenger_count']>0) & (data['trip_distance']>0)]
    #Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    
    #Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    old=data.columns 
    data.columns = [camel_to_snake(col) for col in data.columns]
    new=data.columns 
    diff_cols = [ 1 for index in range(len(data.columns)) if(old[index]!=new[index])]
    
    print("Number of columns renamed: "+str(len(diff_cols)))
    print("Unique values:"+str(data["vendor_id"].unique()))
    return data
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum()==0, 'There are rides with zero passangers'
    assert output['trip_distance'].isin([0]).sum()==0, 'There are rides with zero trip distance'
    assert not pd.api.types.is_datetime64_any_dtype(output['lpep_pickup_date']), "lpep_pickup_date isn't a date"
    assert "vendor_id" in output.columns, "vendor_id is one of the existing values in the column"