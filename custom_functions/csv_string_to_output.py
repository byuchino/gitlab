def csv_string_to_output(convert_list_input=None, **kwargs):
    """
    Convert either a string list, or a single string/int or an actual array of data to a list of dictionaries keyed with output_item
    
    Args:
        convert_list_input (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        *.output_item (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    phantom.debug(convert_list_input)
    
    outputs = []
    
    if convert_list_input and isinstance(convert_list_input, list):
        
        for item in convert_list_input:
            outputs.append({'output_item':item})
    
    
    elif convert_list_input and (isinstance(convert_list_input, str) or isinstance(convert_list_input, int)):
        if isinstance(convert_list_input, int):
            convert_list_input = str(convert_list_input)
            
        convert_list_input = convert_list_input.lstrip().rstrip()
        convert_list_input = convert_list_input.lstrip("[").rstrip("]")
        convert_list_input = convert_list_input.split(",")
        outputs = []

        for item in convert_list_input:
            item = item.lstrip().rstrip()
            item = item.lstrip("\"").rstrip("\"")
            outputs.append({'output_item':item})
        
    phantom.debug(f'Converted List:  {json.dumps(outputs, indent=4)}')
    
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
