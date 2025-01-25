"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'prepare_list_from_values_1' block
    prepare_list_from_values_1(container=container)

    return

@phantom.playbook_block()
def prepare_list_from_values_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("prepare_list_from_values_1() called")

    playbook_input_ioc_value_1 = phantom.collect2(container=container, datapath=["playbook_input:ioc_value_1"])
    playbook_input_ioc_value_2 = phantom.collect2(container=container, datapath=["playbook_input:ioc_value_2"])
    playbook_input_ioc_value_3 = phantom.collect2(container=container, datapath=["playbook_input:ioc_value_3"])
    playbook_input_ioc_value_4 = phantom.collect2(container=container, datapath=["playbook_input:ioc_value_4"])
    playbook_input_ioc_value_5 = phantom.collect2(container=container, datapath=["playbook_input:ioc_value_5"])
    playbook_input_ioc_value_6 = phantom.collect2(container=container, datapath=["playbook_input:ioc_value_6"])
    playbook_input_ioc_value_7 = phantom.collect2(container=container, datapath=["playbook_input:ioc_value_7"])
    playbook_input_ioc_value_8 = phantom.collect2(container=container, datapath=["playbook_input:ioc_value_8"])
    playbook_input_ioc_value_9 = phantom.collect2(container=container, datapath=["playbook_input:ioc_value_9"])

    parameters = []

    # build parameters list for 'prepare_list_from_values_1' call
    for playbook_input_ioc_value_1_item in playbook_input_ioc_value_1:
        for playbook_input_ioc_value_2_item in playbook_input_ioc_value_2:
            for playbook_input_ioc_value_3_item in playbook_input_ioc_value_3:
                for playbook_input_ioc_value_4_item in playbook_input_ioc_value_4:
                    for playbook_input_ioc_value_5_item in playbook_input_ioc_value_5:
                        for playbook_input_ioc_value_6_item in playbook_input_ioc_value_6:
                            for playbook_input_ioc_value_7_item in playbook_input_ioc_value_7:
                                for playbook_input_ioc_value_8_item in playbook_input_ioc_value_8:
                                    for playbook_input_ioc_value_9_item in playbook_input_ioc_value_9:
                                        parameters.append({
                                            "input_1": playbook_input_ioc_value_1_item[0],
                                            "input_2": playbook_input_ioc_value_2_item[0],
                                            "input_3": playbook_input_ioc_value_3_item[0],
                                            "input_4": playbook_input_ioc_value_4_item[0],
                                            "input_5": playbook_input_ioc_value_5_item[0],
                                            "input_6": playbook_input_ioc_value_6_item[0],
                                            "input_7": playbook_input_ioc_value_7_item[0],
                                            "input_8": playbook_input_ioc_value_8_item[0],
                                            "input_9": playbook_input_ioc_value_9_item[0],
                                            "input_10": None,
                                        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="local/prepare_list_from_values", parameters=parameters, name="prepare_list_from_values_1", callback=create_events_1)

    return


@phantom.playbook_block()
def create_events_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("create_events_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    external_id_value = container.get("external_id", None)
    playbook_input_ioc_event_name = phantom.collect2(container=container, datapath=["playbook_input:ioc_event_name"])
    prepare_list_from_values_1__result = phantom.collect2(container=container, datapath=["prepare_list_from_values_1:custom_function_result.data.output_list"])

    parameters = []

    # build parameters list for 'create_events_1' call
    for playbook_input_ioc_event_name_item in playbook_input_ioc_event_name:
        for prepare_list_from_values_1__result_item in prepare_list_from_values_1__result:
            if external_id_value is not None:
                parameters.append({
                    "pairs": [
                        { "name": playbook_input_ioc_event_name_item[0], "value": prepare_list_from_values_1__result_item[0] },
                    ],
                    "incident_id": external_id_value,
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("create events", parameters=parameters, name="create_events_1", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    output = {
        "ioc_list": [],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_playbook_output_data(output=output)

    return