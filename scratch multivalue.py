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

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef","artifact:*.cef.sourceAddress","artifact:*.cef.sourceHostName","artifact:*.cef.senders"])

    container_artifact_header_item_0 = [item[0] for item in container_artifact_data]
    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]
    container_artifact_cef_item_2 = [item[2] for item in container_artifact_data]
    container_artifact_cef_item_3 = [item[3] for item in container_artifact_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'cef:  {json.dumps(container_artifact_header_item_0, indent=4)}')
    phantom.debug(f'sourceAddress:  {json.dumps(container_artifact_cef_item_1, indent=4)}')
    phantom.debug(f'sourceHostName:  {json.dumps(container_artifact_cef_item_2, indent=4)}')
    phantom.debug(f'senders:  {json.dumps(container_artifact_cef_item_3, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    ip_reputation_1(container=container)

    return


def ip_reputation_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("ip_reputation_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.sourceAddress","artifact:*.id"])

    parameters = []

    # build parameters list for 'ip_reputation_1' call
    for container_artifact_item in container_artifact_data:
        if container_artifact_item[0] is not None:
            parameters.append({
                "ip": container_artifact_item[0],
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

    phantom.act("ip reputation", parameters=parameters, name="ip_reputation_1", assets=["test_virustotal"], callback=code_2)

    return


def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_2() called")

    ip_reputation_1_result_data = phantom.collect2(container=container, datapath=["ip_reputation_1:action_result.summary"], action_results=results)

    ip_reputation_1_result_item_0 = [item[0] for item in ip_reputation_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'result data:  {json.dumps(ip_reputation_1_result_item_0, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def code_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_3() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.sourceAddress"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    code_3__cef = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    cef_orig = container_artifact_cef_item_0
    cef_new = []
    for art in cef_orig:
        items = 0
        for value in art.values():
            if isinstance(value, list):
                if value.len() > items:
                    items = value.len()

        phantom.debug(f'{items} items found')

        for x in range(items):
            art_new = {}
            for key, value in art:
                if isinstance(value, list):
                    if x < value.len():
                        art_new[key] = value[x]
                else:
                    art_new[key] = value
                    
            cef_new.append(art_new)

                

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="code_3:cef", value=json.dumps(code_3__cef))

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