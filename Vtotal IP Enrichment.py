"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


################################################################################
## Global Custom Code Start
################################################################################
ip_reputation_items = []


def ip_reputation_next(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("ip_reputation_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    list_drop_none_2_data = phantom.collect2(container=container, datapath=["list_drop_none_2:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'ip_reputation_1' call
    for list_drop_none_2_data_item in list_drop_none_2_data:
        if list_drop_none_2_data_item[0] is not None:
            parameters.append({
                "ip": list_drop_none_2_data_item[0],
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("ip reputation", parameters=parameters, name="ip_reputation_1", assets=["test_virustotal"], callback=code_1)

    return


################################################################################
## Global Custom Code End
################################################################################

def on_start(container):
    phantom.debug('on_start() called')

    # call 'list_merge_1' block
    list_merge_1(container=container)
    # call 'debug_3' block
    debug_3(container=container)

    return

def list_merge_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("list_merge_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationAddress","artifact:*.cef.sourceAddress","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]
    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "input_1": container_artifact_cef_item_0,
        "input_2": container_artifact_cef_item_1,
        "input_3": None,
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

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="list_merge_1", callback=list_drop_none_2)

    return


def list_drop_none_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("list_drop_none_2() called")

    list_merge_1_data = phantom.collect2(container=container, datapath=["list_merge_1:custom_function_result.data.*.item"])

    list_merge_1_data___item = [item[0] for item in list_merge_1_data]

    parameters = []

    parameters.append({
        "input_list": list_merge_1_data___item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_drop_none", parameters=parameters, name="list_drop_none_2", callback=ip_reputation_1)

    return


def ip_reputation_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("ip_reputation_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    list_drop_none_2_data = phantom.collect2(container=container, datapath=["list_drop_none_2:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'ip_reputation_1' call
    for list_drop_none_2_data_item in list_drop_none_2_data:
        if list_drop_none_2_data_item[0] is not None:
            parameters.append({
                "ip": list_drop_none_2_data_item[0],
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'input:  {json.dumps(list_drop_none_2_data, indent=4)}')
    phantom.debug(f'parameters:  {json.dumps(parameters, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("ip reputation", parameters=parameters, name="ip_reputation_1", assets=["test_virustotal"], callback=code_1)

    return


def debug_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_3() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationAddress","artifact:*.cef.sourceAddress","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]
    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "input_1": container_artifact_cef_item_0,
        "input_2": container_artifact_cef_item_1,
        "input_3": None,
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

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_3")

    return


def debug_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_4() called")

    ip_reputation_1_result_data = phantom.collect2(container=container, datapath=["ip_reputation_1:action_result.data","ip_reputation_1:action_result.parameter.context.artifact_id"], action_results=results)

    ip_reputation_1_result_item_0 = [item[0] for item in ip_reputation_1_result_data]

    parameters = []

    parameters.append({
        "input_1": ip_reputation_1_result_item_0,
        "input_2": None,
        "input_3": None,
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

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_4")

    return


def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_1() called")

    ip_reputation_1_result_data = phantom.collect2(container=container, datapath=["ip_reputation_1:action_result.data","ip_reputation_1:action_result.data.*.attributes.last_analysis_stats"], action_results=results)

    ip_reputation_1_result_item_0 = [item[0] for item in ip_reputation_1_result_data]
    ip_reputation_1_result_item_1 = [item[1] for item in ip_reputation_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    #phantom.debug(f'IP Reputation Data:  {json.dumps(ip_reputation_1_result_item_0, indent=4)}')
    phantom.debug(f'IP Reputation Last Analysis Stats:  {json.dumps(ip_reputation_1_result_item_1, indent=4)}')

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