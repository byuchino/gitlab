def list_drop_none_recursive(input_list=None, **kwargs):
    """
    Will process lists of lists recursively and build a single list of dictionaries with the actual value keyed by "item"
    
    Args:
        input_list
    
    Returns a JSON-serializable object that implements the configured data paths:
        *.item
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    # this only works on lists, so print a warning and return None if the input is not a list
    if not isinstance(input_list, list):
        phantom.debug("unable to process because the input is not a list")
        return
    
    
    # iterate through the items in the list and append each non-falsy one as its own dictionary
    outputs = []

    """
    Problem occurs when [[{"a":1}, {"a":2}], [{"b":1}, {"b":2}]]
    """
    
    def process_list(sublist=None):
        if sublist and isinstance(sublist, list) and len(sublist) > 0:
            for item in sublist:
                if isinstance(item, list):
                    return process_list(item)
                else:
                    if item:
                        outputs.append({"item": item})
                        
    
    process_list(input_list)
    
    phantom.debug(f'list_drop_none_recursive returning: {json.dumps(outputs, index=4)}')
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs if len(outputs) > 0 else None

