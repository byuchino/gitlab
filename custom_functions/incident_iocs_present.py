def incident_iocs_present(input_1=None, input_2=None, input_3=None, input_4=None, input_5=None, **kwargs):
    """
    Args:
        input_1 (CEF type: *)
        input_2 (CEF type: *)
        input_3 (CEF type: *)
        input_4 (CEF type: *)
        input_5 (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        present (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = []
    
    # Write your custom code here...
    outputs.append({"present": True})
    
    # Return a JSON-serializable object
    assert isinstance(outputs, list)  # Will raise an exception if the :outputs: object is not a list
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
