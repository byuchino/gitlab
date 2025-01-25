"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_none' block
    filter_none(container=container)

    return

def filter_none(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_none() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.cef.destinationAddressList", "!=", ""]
        ],
        name="filter_none:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        csv_string_to_output_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


def csv_string_to_output_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("csv_string_to_output_1() called")

    filtered_artifact_0_data_filter_none = phantom.collect2(container=container, datapath=["filtered-data:filter_none:condition_1:artifact:*.cef.destinationAddressList","filtered-data:filter_none:condition_1:artifact:*.id"])

    parameters = []

    # build parameters list for 'csv_string_to_output_1' call
    for filtered_artifact_0_item_filter_none in filtered_artifact_0_data_filter_none:
        parameters.append({
            "convert_list_input": filtered_artifact_0_item_filter_none[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="local/csv_string_to_output", parameters=parameters, name="csv_string_to_output_1", callback=delete_all_cef)

    return


def create_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_artifact() called")

    csv_string_to_output_1_data = phantom.collect2(container=container, datapath=["csv_string_to_output_1:custom_function_result.data.*.ouput_item"])

    csv_string_to_output_1_data___ouput_item = [item[0] for item in csv_string_to_output_1_data]

    input_parameter_0 = "cef_name=destinationAddress"

    ################################################################################
    ## Custom Code Start
    ################################################################################
    
    id_value  = container.get("id", None)
    base_url  = phantom.build_phantom_rest_url('artifact')
    total_url = base_url
    cef_key   = input_parameter_0.split("=")[1].lstrip().rstrip()
    
    
    #note https://docs.splunk.com/Documentation/SOARonprem/5.3.1/PlatformAPI/RESTArtifacts
    #read the part on run_automation if you dont want this to trigger automation
    
    art_json = {"container_id":id_value,
                "name":"flatened_artifact",
                "label":"even",
                "severity":"Medium",
                "cef": {}
               }
    
    for item in csv_string_to_output_1_data___ouput_item:
        
        art_json["cef"] = {cef_key:item}
        
        response  = phantom.requests.post(total_url, json=art_json, verify=False)
    
        if response.status_code == 200:
            phantom.debug(response.text)
        else:
            phantom.error(response.text)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def delete_all_cef(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("delete_all_cef() called")

    input_parameter_0 = "cef_to_delete=destinationAddressList"

    ################################################################################
    ## Custom Code Start
    ################################################################################

    id_value  = container.get("id", None)
    base_url  = phantom.build_phantom_rest_url('container')
    total_url = base_url + "/{0}/artifacts".format(str(id_value))
    
    key_del   = str(input_parameter_0).split("=")[1].lstrip().rstrip()
    jsn_mod   = []
    
    ################################
    response  = phantom.requests.get(total_url, verify=False)
    
    if response.status_code == 200:
            for item in response.json()['data']:
                if key_del in item['cef']:
                    del item['cef'][key_del]
                    jsn_mod.append(item)                    
    else:
        phantom.error(response.text)
    
    ################################
    
    
    base_url  = phantom.build_phantom_rest_url('artifact')
    
    for item in jsn_mod:
        
        art_id    = str(item['id'])
        total_url = base_url + "/{0}".format(art_id)
        response  = phantom.requests.post(total_url, json=item, verify=False)
        
        if response.status_code == 200:
            phantom.debug("cef item deleted on artifact id={0}".format(art_id))
        else:
            phantom.error(response.text)

    ################################################################################
    ## Custom Code End
    ################################################################################

    create_artifact(container=container)

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