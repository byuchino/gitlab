"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'find_all_pending_containers' block
    find_all_pending_containers(container=container)

    return

@phantom.playbook_block()
def find_all_pending_containers(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("find_all_pending_containers() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "location": "/rest/container?_filter_tags__contains=\"saa_pending\"",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="find_all_pending_containers", assets=["http_asset"], callback=action_result)

    return


@phantom.playbook_block()
def prepare_container_id_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("prepare_container_id_list() called")

    find_all_pending_containers_result_data = phantom.collect2(container=container, datapath=["find_all_pending_containers:action_result.data.*.response_body"], action_results=results)

    find_all_pending_containers_result_item_0 = [item[0] for item in find_all_pending_containers_result_data]

    prepare_container_id_list__num_containers = None
    prepare_container_id_list__container_id_list = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    output = []
    len = find_all_pending_containers_result_item_0[0]['count']
    
    if len:
        containers_list = find_all_pending_containers_result_item_0[0]['data']
        phantom.debug(f'data:  {json.dumps(containers_list, indent=4)}')

        for container in containers_list:
            #output.append({"item": {"id": container["id"], "hash": container["hash"]}})

            output.append({
                'id': container['id']
            })

    prepare_container_id_list__num_containers = len
    prepare_container_id_list__container_id_list = output

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="prepare_container_id_list:num_containers", value=json.dumps(prepare_container_id_list__num_containers))
    phantom.save_run_data(key="prepare_container_id_list:container_id_list", value=json.dumps(prepare_container_id_list__container_id_list))

    decision_2(container=container)

    return


@phantom.playbook_block()
def debug_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("debug_1() called")

    code_2__output = json.loads(_ if (_ := phantom.get_run_data(key="code_2:output")) != "" else "null")  # pylint: disable=used-before-assignment

    parameters = []

    parameters.append({
        "input_1": code_2__output,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_1")

    return


@phantom.playbook_block()
def list_demux_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("list_demux_4() called")

    prepare_container_id_list__container_id_list = json.loads(_ if (_ := phantom.get_run_data(key="prepare_container_id_list:container_id_list")) != "" else "null")  # pylint: disable=used-before-assignment

    parameters = []

    parameters.append({
        "input_list": prepare_container_id_list__container_id_list,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_demux", parameters=parameters, name="list_demux_4", callback=container_update_6)

    return


@phantom.playbook_block()
def debug_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("debug_5() called")

    list_demux_4__result = phantom.collect2(container=container, datapath=["list_demux_4:custom_function_result.data.output"])

    list_demux_4_data_output = [item[0] for item in list_demux_4__result]

    parameters = []

    parameters.append({
        "input_1": list_demux_4_data_output,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_5")

    return


@phantom.playbook_block()
def container_update_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("container_update_6() called")

    list_demux_4__result = phantom.collect2(container=container, datapath=["list_demux_4:custom_function_result.data.output.id"])

    parameters = []

    # build parameters list for 'container_update_6' call
    for list_demux_4__result_item in list_demux_4__result:
        parameters.append({
            "name": None,
            "tags": "test",
            "label": None,
            "owner": None,
            "status": None,
            "severity": None,
            "input_json": None,
            "description": None,
            "sensitivity": None,
            "container_input": list_demux_4__result_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/container_update", parameters=parameters, name="container_update_6")

    return


@phantom.playbook_block()
def action_result(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("action_result() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["find_all_pending_containers:action_result.status", "==", "success"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        prepare_container_id_list(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def decision_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_2() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["prepare_container_id_list:custom_function:num_containers", ">", 0]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        list_demux_4(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    code_3(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def code_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_3() called")

    prepare_container_id_list__output = json.loads(_ if (_ := phantom.get_run_data(key="prepare_container_id_list:output")) != "" else "null")  # pylint: disable=used-before-assignment

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug('no containers in list')
    phantom.debug(f'list:  {json.dumps(prepare_container_id_list__output, indent=4)}')

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