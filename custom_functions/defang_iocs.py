def defang_iocs(ioc_list=None, **kwargs):
    """
    This CF will defang the IOCs passed to it.
    
    Args:
        ioc_list (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        defanged_ioc.*.item
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import urllib
    import re
    
    outputs = {}
    
    # Write your custom code here...
    
    phantom.debug(f'ioc_list:  {ioc_list}')
    
    # regex for domain detection
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    # Compile the ReGex
    p = re.compile(regex)
    
    defanged_ioc_list=[]
    for ioc in ioc_list:
        if ioc and urllib.parse.urlparse(ioc).scheme in ("http", "https"):
            phantom.debug(f'processing ioc:  {ioc}')
            item = ioc.replace("http", "hXXp").replace(".", "[.]")
            defanged_ioc_list.append(item)
        elif ioc and re.match(p, ioc):
            item = ioc.replace(".", "[.]")
            defanged_ioc_list.append(item)
        else:
            defanged_ioc_list.append(ioc)
    
    phantom.debug(f'defanged_ioc_list:  {defanged_ioc_list}')
    outputs["defanged_ioc"]=[{"item": item} for item in defanged_ioc_list]
    
    phantom.debug(f'outputs:  {outputs}')
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
