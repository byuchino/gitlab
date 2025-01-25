def list_to_dicts(list=None, **kwargs):
    """
    Takes a list of strings and returns a list of dictionaries keyed with keyName
    
    Args:
        list
    
    Returns a JSON-serializable object that implements the configured data paths:
        items.*.item (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {
        "item": []
    }
    
    phantom.debug(f'function processing list: {list} type: {type(list)}')
    
    # Write your custom code here...
    if list and isinstance(list, str):
        list = [list]
        phantom.debug(f'converted to list: {type(list)} {list}')
        
    if list and len(list) > 0:
        items = list[0]
        for item in items:
            outputs['items'].append({
                "item":item
            })
            
    phantom.debug(f'returning: {json.dumps(outputs, indent=4)}')
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
