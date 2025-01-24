"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'code_1' block
    code_1(container=container)

    return

def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef","artifact:*.cef.sender","artifact:*.cef.recipient"])

    container_artifact_header_item_0 = [item[0] for item in container_artifact_data]
    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]
    container_artifact_cef_item_2 = [item[2] for item in container_artifact_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'cef:  {json.dumps(container_artifact_header_item_0, indent=4)}')
    phantom.debug(f'sender:  {json.dumps(container_artifact_cef_item_1)}')
    phantom.debug(f'recipient:  {json.dumps(container_artifact_cef_item_2)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    send_email_1(container=container)

    return


def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_1() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="or",
        conditions=[
            ["artifact:*.cef.sourceAddress", "!=", ""],
            ["artifact:*.cef.requestURL", "!=", ""]
        ],
        name="filter_1:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        code_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_2() called")

    filtered_artifact_0_data_filter_1 = phantom.collect2(container=container, datapath=["filtered-data:filter_1:condition_1:artifact:*.cef","filtered-data:filter_1:condition_1:artifact:*.cef.sourceAddress","filtered-data:filter_1:condition_1:artifact:*.cef.requestURL","filtered-data:filter_1:condition_1:artifact:*.cef.destinationDnsDomain"])

    filtered_artifact_0__cef = [item[0] for item in filtered_artifact_0_data_filter_1]
    filtered_artifact_0__cef_sourceaddress = [item[1] for item in filtered_artifact_0_data_filter_1]
    filtered_artifact_0__cef_requesturl = [item[2] for item in filtered_artifact_0_data_filter_1]
    filtered_artifact_0__cef_destinationdnsdomain = [item[3] for item in filtered_artifact_0_data_filter_1]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'cef after filter:  {json.dumps(filtered_artifact_0__cef, indent=4)}')
    phantom.debug(f'sourceAddress:  {json.dumps(filtered_artifact_0__cef_sourceaddress)}')
    phantom.debug(f'requestURL:  {json.dumps(filtered_artifact_0__cef_requesturl)}')
    phantom.debug(f'destinationDnsDomain:  {json.dumps(filtered_artifact_0__cef_destinationdnsdomain)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    passthrough_1(container=container)

    return


def passthrough_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("passthrough_1() called")

    filtered_artifact_0_data_filter_1 = phantom.collect2(container=container, datapath=["filtered-data:filter_1:condition_1:artifact:*.cef.sourceAddress","filtered-data:filter_1:condition_1:artifact:*.cef.requestURL","filtered-data:filter_1:condition_1:artifact:*.cef.destinationDnsDomain","filtered-data:filter_1:condition_1:artifact:*.id"])

    filtered_artifact_0__cef_sourceaddress = [item[0] for item in filtered_artifact_0_data_filter_1]
    filtered_artifact_0__cef_requesturl = [item[1] for item in filtered_artifact_0_data_filter_1]
    filtered_artifact_0__cef_destinationdnsdomain = [item[2] for item in filtered_artifact_0_data_filter_1]

    parameters = []

    parameters.append({
        "input_1": filtered_artifact_0__cef_sourceaddress,
        "input_2": filtered_artifact_0__cef_requesturl,
        "input_3": filtered_artifact_0__cef_destinationdnsdomain,
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

    phantom.custom_function(custom_function="community/passthrough", parameters=parameters, name="passthrough_1", callback=code_3)

    return


def code_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_3() called")

    passthrough_1_data = phantom.collect2(container=container, datapath=["passthrough_1:custom_function_result.data.*.item"])

    passthrough_1_data___item = [item[0] for item in passthrough_1_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    #phantom.debug(f'passthrough data:  {json.dumps(passthrough_1_data, indent=4)}')
    phantom.debug(f'passthrough item:  {json.dumps(passthrough_1_data___item, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def send_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("send_email_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    body_formatted_string = phantom.format(
        container=container,
        template="""Test email\n""",
        parameters=[])

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.recipient","artifact:*.cef.sender","artifact:*.id"])

    parameters = []

    # build parameters list for 'send_email_1' call
    for container_artifact_item in container_artifact_data:
        if container_artifact_item[0] is not None and body_formatted_string is not None:
            parameters.append({
                "to": container_artifact_item[0],
                "body": body_formatted_string,
                "subject": "test email",
                "from": container_artifact_item[1],
                "context": {'artifact_id': container_artifact_item[2]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("send email", parameters=parameters, name="send_email_1", assets=["wpoven"])

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