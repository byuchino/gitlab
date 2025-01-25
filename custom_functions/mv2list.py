def mv2list(mvfield=None, **kwargs):
    """
    Args:
        mvfield
    
    Returns a JSON-serializable object that implements the configured data paths:
        outlist
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(f"mvinput:  {mvfield}")
    phantom.debug(f"mvinput type:  {type(mvfield)}")
    
    try:
        l = json.loads(mvfield)
        phantom.debug("valid json string")
    except:
        # assume string
        phantom.debug("exception")
        if isinstance(mvfield, str):
            l = mvfield.split(",")
        else:
            l = mvfield
        
    phantom.debug(f"after conversion: {json.dumps(l, indent=4)}")
    phantom.debug(f"converted type:  {type(l)}")
    
    outputs['outlist'] = []
    if isinstance(l, list):
        for item in l:
            outputs['outlist'].append({ "item": item })

    phantom.debug(f"outputs:  {json.dumps(outputs)}")
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
