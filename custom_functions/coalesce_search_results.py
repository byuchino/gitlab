def coalesce_search_results(result_data=None, **kwargs):
    """
    Args:
        result_data
    
    Returns a JSON-serializable object that implements the configured data paths:
        items.*.item
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {
        "items": []
    }
    
    # Write your custom code here...
    phantom.debug(f'input search results:  {json.dumps(result_data, indent=4)}')

    if result_data and len(result_data) > 0:
        l2 = result_data[0]
        if l2 and isinstance(l2, list) and len(l2) > 0:
            items = l2[0]

            for item in items:
                phantom.debug(f'item:  {json.dumps(item, indent=4)}')
                outputs['items'].append({
                    "item": item
                })
        else:
            phantom.debug("Second level list missing or empty")
        
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
