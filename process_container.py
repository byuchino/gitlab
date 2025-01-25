"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'code_2' block
    code_2(container=container)
    # call 'debug_1' block
    debug_1(container=container)
    # call 'format_1' block
    format_1(container=container)

    return

@phantom.playbook_block()
def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("get_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_1__as_list = phantom.get_format_data(name="format_1__as_list")

    parameters = []

    # build parameters list for 'get_data_1' call
    for format_1__item in format_1__as_list:
        if format_1__item is not None:
            parameters.append({
                "location": format_1__item,
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_data_1", assets=["http_asset"], callback=code_1)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    get_data_1_result_data = phantom.collect2(container=container, datapath=["get_data_1:action_result.summary"], action_results=results)

    get_data_1_result_item_0 = [item[0] for item in get_data_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'data:  {json.dumps(get_data_1_result_item_0, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_2() called")

    playbook_input_container_id = phantom.collect2(container=container, datapath=["playbook_input:container_id"])

    playbook_input_container_id_values = [item[0] for item in playbook_input_container_id]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'pb input:  {json.dumps(playbook_input_container_id_values, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def debug_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("debug_1() called")

    playbook_input_container_id = phantom.collect2(container=container, datapath=["playbook_input:container_id"])

    playbook_input_container_id_values = [item[0] for item in playbook_input_container_id]

    parameters = []

    parameters.append({
        "input_1": playbook_input_container_id_values,
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
def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_1() called")

    template = """%%\n/rest/container/{0}\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "playbook_input:container_id"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    get_data_1(container=container)

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