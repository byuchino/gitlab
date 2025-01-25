def list_fixup_domain_names(domain_list=None, **kwargs):
    """
    Args:
        domain_list (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        item (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = []
    
    # Write your custom code here...
    for item in domain_list:
        split_list = item.split(".")
        if len(split_list) >= 2:
            outputs.append({"item": ".".join(split_list[-2:])})
            
    phantom.debug(f'fixed-up results:  {outputs}')
    
    # Return a JSON-serializable object
    assert isinstance(outputs, list)  # Will raise an exception if the :outputs: object is not a list
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
