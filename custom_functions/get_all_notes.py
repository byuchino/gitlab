def get_all_notes(container=None, **kwargs):
    """
    Args:
        container
    
    Returns a JSON-serializable object that implements the configured data paths:
        items.*.item
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    outputs = {
        "items": []
    }

    for note in phantom.get_notes(container=container):
        outputs['items'].append({
            "item": note['data']
        })

    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
