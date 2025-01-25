"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'list_merge_1' block
    list_merge_1(container=container)

    return

def list_merge_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("list_merge_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.requestURL","artifact:*.cef.sourceAddress","artifact:*.cef.destinationDnsDomain","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]
    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]
    container_artifact_cef_item_2 = [item[2] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "input_1": container_artifact_cef_item_0,
        "input_2": container_artifact_cef_item_1,
        "input_3": container_artifact_cef_item_2,
        "input_4": None,
        "input_5": None,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "input_10": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    import urllib
    
    phantom.debug(f'parameters:  {json.dumps(parameters, indent=4)}')

    param_copy = dict(parameters[0])
    
    for k, v in param_copy.items():
        if isinstance(v, list):  # skip the Nones
            new_list = []
            
            for item in v:  # iterate over list items and defang valid urls
                if item is not None and urllib.parse.urlparse(item).scheme in ("http", "https"):
                    phantom.debug(f'defanging {item}')
                    item = item.replace("http", "hXXp").replace(".", "[.]")
                new_list.append(item)
            
            # replace list in original parameters
            parameters[0][k] = new_list
                
    phantom.debug(f'parameters:  {json.dumps(parameters, indent=4)}')
        

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="list_merge_1", callback=code_3)

    return


def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_1() called")

    list_merge_1__result = phantom.collect2(container=container, datapath=["list_merge_1:custom_function_result.data"])

    list_merge_1_data = [item[0] for item in list_merge_1__result]

    code_1__output = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    import urllib
    
    code_1__output = []
    
    phantom.debug(f'list:  {json.dumps(list_merge_1_data, indent=4)}')
    for item in list_merge_1_data[0]:
        url_candidate = item["item"]
        if urllib.parse.urlparse(url_candidate).scheme in ("http", "https"):
            item["item"] = url_candidate.replace("http", "hXXp").replace(".", "[.]")

    code_1__output = list_merge_1_data
        
    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="code_1:output", value=json.dumps(code_1__output))

    code_2(container=container)

    return


def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_2() called")

    code_1__output = json.loads(phantom.get_run_data(key="code_1:output"))

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'defanged:  {json.dumps(code_1__output, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def code_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_3() called")

    list_merge_1_data = phantom.collect2(container=container, datapath=["list_merge_1:custom_function_result.data.*.item"])

    list_merge_1_data___item = [item[0] for item in list_merge_1_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'list:  {json.dumps(list_merge_1_data___item, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return