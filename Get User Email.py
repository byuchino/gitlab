"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'get_first_non_null_input_1' block
    get_first_non_null_input_1(container=container)

    return

@phantom.playbook_block()
def get_first_non_null_input_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("get_first_non_null_input_1() called")

    data_summary_user_email_value = container.get("data", {}).get("summary", {}).get("user_email", None)
    data_summary_src_value = container.get("data", {}).get("summary", {}).get("src", None)

    parameters = []

    parameters.append({
        "input_1": data_summary_user_email_value,
        "input_2": data_summary_src_value,
        "input_3": None,
        "input_4": None,
        "input_5": None,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "contains_text": "@fmglobal.com",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="local/get_first_non_null_input", parameters=parameters, name="get_first_non_null_input_1", callback=mc_create_event_user_email)

    return


@phantom.playbook_block()
def mc_create_event_user_email(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_create_event_user_email() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    external_id_value = container.get("external_id", None)
    get_first_non_null_input_1__result = phantom.collect2(container=container, datapath=["get_first_non_null_input_1:custom_function_result.data.first_non_null_value"])

    parameters = []

    # build parameters list for 'mc_create_event_user_email' call
    for get_first_non_null_input_1__result_item in get_first_non_null_input_1__result:
        if external_id_value is not None:
            parameters.append({
                "pairs": [
                    { "name": "user_email", "value": get_first_non_null_input_1__result_item[0] },
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

    phantom.act("create events", parameters=parameters, name="mc_create_event_user_email", assets=["builtin_mc_connector"])

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