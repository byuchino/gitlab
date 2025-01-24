"""
Find and tag all malicious VirusTotal result artifacts.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_by_provider' block
    filter_by_provider(container=container)

    return

@phantom.playbook_block()
def filter_by_provider(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_by_provider() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.cef.provider", "==", "virustotal"],
            ["artifact:*.cef.scoreindex", "!=", ""]
        ],
        name="filter_by_provider:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        vt3_check_if_malicious(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def vt3_check_if_malicious(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("vt3_check_if_malicious() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_by_provider:condition_1:artifact:*.cef.scoreindex", ">=", 8]
        ],
        name="vt3_check_if_malicious:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        playbook_update_artifact_tags__utility__1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_by_provider:condition_1:artifact:*.cef.scoreindex", "<", 8]
        ],
        name="vt3_check_if_malicious:condition_2",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        playbook_update_artifact_tags__utility__2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_2, filtered_results=matched_results_2)

    return


@phantom.playbook_block()
def playbook_update_artifact_tags__utility__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_update_artifact_tags__utility__1() called")

    filtered_artifact_0_data_vt3_check_if_malicious = phantom.collect2(container=container, datapath=["filtered-data:vt3_check_if_malicious:condition_1:artifact:*.id"])

    filtered_artifact_0__id = [item[0] for item in filtered_artifact_0_data_vt3_check_if_malicious]

    inputs = {
        "artifact_id": filtered_artifact_0__id,
        "artifact_op": ["add=malicious"],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Update Artifact Tags [Utility]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Update Artifact Tags [Utility]", container=container, name="playbook_update_artifact_tags__utility__1", inputs=inputs)

    return


@phantom.playbook_block()
def playbook_update_artifact_tags__utility__2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_update_artifact_tags__utility__2() called")

    filtered_artifact_0_data_vt3_check_if_malicious = phantom.collect2(container=container, datapath=["filtered-data:vt3_check_if_malicious:condition_2:artifact:*.id"])

    filtered_artifact_0__id = [item[0] for item in filtered_artifact_0_data_vt3_check_if_malicious]

    inputs = {
        "artifact_id": filtered_artifact_0__id,
        "artifact_op": ["remove=malicious"],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Update Artifact Tags [Utility]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Update Artifact Tags [Utility]", container=container, name="playbook_update_artifact_tags__utility__2", inputs=inputs)

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