def json_to_csv_attachment(json_payloads=None, container_id=None, name_prefix=None, forced_headers=None, **kwargs):
    """
    Takes a json payload and converts it to a csv attachment
    
    Args:
        json_payloads: list of json payloads to parse and attach
        container_id: event.id or case.id
        name_prefix
        forced_headers
    
    Returns a JSON-serializable object that implements the configured data paths:
        *.vault_id (CEF type: *): vault_id returned from attachment
        *.error (CEF type: *): error encountered if we fail.
        *.filename (CEF type: *): The name of the file written
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import csv
    import os
    from tempfile import NamedTemporaryFile
    
    if not name_prefix:
        name_prefix="default_log"
    
    outputs = {}
    
    VAULT_BASE_DIR='/opt/phantom/vault/tmp'
    
    
    # Write your custom code here...
    ##if we're passed a single dict payload, convert to an array and handle the same.
    if json_payloads and isinstance(json_payloads, dict):
        json_payloads = [json_payloads]
        
    if json_payloads and isinstance(json_payloads, list) and len(json_payloads) > 0:
        
        phantom.debug(f'Attaching CSV File. Entry Count: {len(json_payloads)} Container ID: {container_id}')
        
        for payload in json_payloads:
            
            if payload is not None and len(payload) > 0:
                
                phantom.debug(f'operating on payload. record count: {len(payload)}')
                
                first_entry = payload[0]
                
                with NamedTemporaryFile(mode="w", dir=VAULT_BASE_DIR, prefix=name_prefix, suffix=".csv", newline="", delete=False) as csv_file:
                    phantom.debug(f'writing to: {csv_file.name}')
                    phantom.debug(f'Getting headers from first_entry: {first_entry}')
                    fieldnames = list(first_entry.keys())
                    
                    phantom.debug(f'Resolved headers: {fieldnames}')
                    
                    if forced_headers and len(forced_headers) > 0:
                        for header in forced_headers:
                            if header not in fieldnames:
                                fieldnames.append(header)
                                
                    phantom.debug(f'Constructing DictWriter')
                    writer = csv.DictWriter(csv_file, fieldnames=first_entry.keys(), extrasaction='ignore')
                    writer.writeheader()
                    phantom.debug(f'Entering row iterator')
                    for row in payload:
                        writer.writerow(row)
                        
                    # attach to case
                    
                    file_name = os.path.basename(csv_file.name)
                    phantom.debug(f'Getting file reference: {file_name}')
                    try:
                        phantom.debug(f'Attaching file: {csv_file.name} id: {container_id}')
                        success, message, vault_id = phantom.vault_add(container=container_id, file_location=csv_file.name, file_name=file_name)
                        
                        
                        outputs[file_name] = {
                            "success":success,
                            "message":message,
                            "vault_id":vault_id,
                            "file_name":file_name
                        }
                        
                    except Exception as e:
                        phantom.error(f'Exception in json_to_csv_attachment {e}')
                        outputs[file_name] = {
                            "success":False,
                            "error":e
                        }
    
    # Return a JSON-serializable object
    phantom.debug(f'json_to_csv_attachment returning: {json.dumps(outputs, index=4)}')
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
