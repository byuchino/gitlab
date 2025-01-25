"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'post_data_1' block
    post_data_1(container=container)

    return

@phantom.playbook_block()
def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("get_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    location_formatted_string = phantom.format(
        container=container,
        template="""/services/authentication/users/{0}\n""",
        parameters=[
            "artifact:*.cef.userid"
        ])

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.userid","artifact:*.id"])

    parameters = []

    # build parameters list for 'get_data_1' call
    for container_artifact_item in container_artifact_data:
        if location_formatted_string is not None:
            parameters.append({
                "location": location_formatted_string,
                "context": {'artifact_id': container_artifact_item[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'parameters:  {json.dumps(parameters, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_data_1", assets=["http to splunk 138"], callback=code_1)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    get_data_1_result_data = phantom.collect2(container=container, datapath=["get_data_1:action_result.status","get_data_1:action_result.summary"], action_results=results)

    get_data_1_result_item_0 = [item[0] for item in get_data_1_result_data]
    get_data_1_result_item_1 = [item[1] for item in get_data_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    status = get_data_1_result_item_0[0]
    summary = get_data_1_result_item_1[0]
    
    phantom.debug(f'status: {status}, summary: {json.dumps(summary, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def post_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("post_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    location_formatted_string = phantom.format(
        container=container,
        template="""/services/authentication/users/{0}\n""",
        parameters=[
            "artifact:*.cef.userid"
        ])

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.userid","artifact:*.id"])

    parameters = []

    # build parameters list for 'post_data_1' call
    for container_artifact_item in container_artifact_data:
        if location_formatted_string is not None:
            parameters.append({
                "location": location_formatted_string,
                "body": "password=12345678, force-change-pass=false",
                "context": {'artifact_id': container_artifact_item[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("post data", parameters=parameters, name="post_data_1", assets=["http to splunk 138"], callback=code_2)

    return


@phantom.playbook_block()
def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_2() called")

    post_data_1_result_data = phantom.collect2(container=container, datapath=["post_data_1:action_result.data.*.parsed_response_body"], action_results=results)

    post_data_1_result_item_0 = [item[0] for item in post_data_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'parsed response body:  {json.dumps(post_data_1_result_item_0, indent=4)}')

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