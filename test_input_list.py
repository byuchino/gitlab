"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'url_parse_2' block
    url_parse_2(container=container)

    return

@phantom.playbook_block()
def list_merge_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("list_merge_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.requestURL","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "input_1": container_artifact_cef_item_0,
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

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="list_merge_1", callback=playbook_process_container_1)

    return


@phantom.playbook_block()
def playbook_process_container_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_process_container_1() called")

    list_merge_1__result = phantom.collect2(container=container, datapath=["list_merge_1:custom_function_result.data.item"])

    list_merge_1_data_item = [item[0] for item in list_merge_1__result]

    inputs = {
        "container_id": list_merge_1_data_item,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/process_container", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/process_container", container=container, name="playbook_process_container_1", inputs=inputs)

    return


@phantom.playbook_block()
def playbook_process_container_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_process_container_2() called")

    inputs = {
        "container_id": [4],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/process_container", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/process_container", container=container, name="playbook_process_container_2", inputs=inputs)

    return


@phantom.playbook_block()
def url_parse_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("url_parse_2() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.requestURL","artifact:*.id"])

    parameters = []

    # build parameters list for 'url_parse_2' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "input_url": container_artifact_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/url_parse", parameters=parameters, name="url_parse_2", callback=debug_3)

    return


@phantom.playbook_block()
def debug_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("debug_3() called")

    url_parse_2__result = phantom.collect2(container=container, datapath=["url_parse_2:custom_function_result.data","url_parse_2:custom_function_result.data.scheme","url_parse_2:custom_function_result.data.netloc","url_parse_2:custom_function_result.data.path"])

    url_parse_2_data = [item[0] for item in url_parse_2__result]
    url_parse_2_data_scheme = [item[1] for item in url_parse_2__result]
    url_parse_2_data_netloc = [item[2] for item in url_parse_2__result]
    url_parse_2_data_path = [item[3] for item in url_parse_2__result]

    parameters = []

    parameters.append({
        "input_1": url_parse_2_data,
        "input_2": url_parse_2_data_scheme,
        "input_3": url_parse_2_data_netloc,
        "input_4": url_parse_2_data_path,
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


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    list_merge_1__result = phantom.collect2(container=container, datapath=["list_merge_1:custom_function_result.data.item"])

    list_merge_1_data_item = [item[0] for item in list_merge_1__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return