"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_case_promotion__utility__1' block
    playbook_case_promotion__utility__1(container=container)

    return

def playbook_case_promotion__utility__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_case_promotion__utility__1() called")

    inputs = {
        "promotion_reason": "Test Case Promotion PB",
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Case Promotion [utility]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Case Promotion [utility]", container=container, name="playbook_case_promotion__utility__1", callback=add_note_1, inputs=inputs)

    return


def add_note_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_note_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content="Did this work?", note_format="markdown", note_type="general", title="Case Note Test")

    artifact_create_2(container=container)

    return


def artifact_create_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("artifact_create_2() called")

    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "container": id_value,
        "name": "Case Artifact 1",
        "label": None,
        "severity": None,
        "cef_field": "MyCefField1",
        "cef_value": "this is a test",
        "cef_data_type": "*",
        "tags": None,
        "run_automation": None,
        "input_json": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_2")

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