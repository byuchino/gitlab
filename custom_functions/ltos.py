def ltos(input_list=None, **kwargs):
    """
    list to string
    
    Args:
        input_list
    
    Returns a JSON-serializable object that implements the configured data paths:
        output_string
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(f"input:  {input_list}")
    
    try:
        l = json.loads(input_list)
        phantom.debug("valid json string")
    except:
        phantom.debug("exception")
        l = input_list
        
    phantom.debug(f"input type is {type(l)}")
    phantom.debug(f"input is {json.dumps(l, indent=4)}")
    
    if isinstance(l, list):
        s = ",".join(str(x) for x in l)
        phantom.debug(f"after conversion: {s}")
        phantom.debug(f"type is {type(s)}")
    else:
        phantom.debug("input is not convertible")
        s = l

    '''
    try:
        item = json.loads(input_list)
        phantom.debug("input is valid json")
        if isinstance(item, list):
            phantom.debug("input is a list")
            s = ",".join([str(x) for x in item])
    except:
        phantom.debug("Exception occurred")
        s = input_list
       
    '''
    
    #outputs = s
    outputs['output_string'] = s
    phantom.debug(f"outputs:  {json.dumps(outputs)}")
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
