def vt_ip_rep_iter(asset=None, ip=None, artifact_id=None, **kwargs):
    """
    Args:
        asset
        ip (CEF type: ip)
        artifact_id
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(f'asset:  {json.dumps(asset)}')
    phantom.debug(f'ip:  {json.dumps(ip)}')
    phantom.debug(f'artifact_id:  {json.dumps(artifact_id)}')

    parameters = []
    parameters.append({
        "ip": ip,
        "context": {'artifact_id': artifact_id[0]},
    })
    
    phantom.debug(f'parameters:  {json.dumps(parameters, indent=4)}')
    
    #phantom.act("ip reputation", parameters=parameters, name="ip_reputation_1", assets=["vtotalv2"], callback=noop_1)
    phantom.act("ip reputation", parameters=parameters, name="vt_ip_rep_iter", assets=[asset]) # pylint: disable=all
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
