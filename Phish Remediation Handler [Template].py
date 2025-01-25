"""
Phish use case remediation playbook.  This playbook is triggered on completion of all outstanding Attack Analyzer jobs that were launched from the phish main playbook.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_attack_analyzer_update_malicious_1' block
    playbook_attack_analyzer_update_malicious_1(container=container)

    return

@phantom.playbook_block()
def filter_for_malicious(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_for_malicious() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["malicious", "in", "artifact:*.tags"]
        ],
        name="filter_for_malicious:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        filter_by_ioc_type(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def sentinelone_placeholder(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("sentinelone_placeholder() called")

    filtered_artifact_0_data_filter_file_by_provider = phantom.collect2(container=container, datapath=["filtered-data:filter_file_by_provider:condition_2:artifact:*.cef.ioc"])

    filtered_artifact_0__cef_ioc = [item[0] for item in filtered_artifact_0_data_filter_file_by_provider]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for item in filtered_artifact_0__cef_ioc:
        phantom.debug(f'{item} submitted to SentinelOne block hash action')

    ################################################################################
    ## Custom Code End
    ################################################################################

    join_ews_block_sender_placeholder(container=container)

    return


@phantom.playbook_block()
def code_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_4() called")

    filtered_artifact_0_data_filter_by_provider = phantom.collect2(container=container, datapath=["filtered-data:filter_by_provider:condition_3:artifact:*.cef.ioc"])

    filtered_artifact_0__cef_ioc = [item[0] for item in filtered_artifact_0_data_filter_by_provider]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for item in filtered_artifact_0__cef_ioc:
        phantom.debug(f'IP {item} is malicious and requires remediation')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def filter_file_by_provider(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_file_by_provider() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_by_ioc_type:condition_1:artifact:*.cef.provider", "==", "splunk attack analyzer"]
        ],
        name="filter_file_by_provider:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        code_6(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_by_ioc_type:condition_1:artifact:*.cef.provider", "==", "virustotal"]
        ],
        name="filter_file_by_provider:condition_2",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        pass

    return


@phantom.playbook_block()
def join_ews_block_sender_placeholder(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("join_ews_block_sender_placeholder() called")

    if phantom.completed(playbook_names=["playbook_attack_analyzer_update_malicious_1"]):
        # call connected block "ews_block_sender_placeholder"
        ews_block_sender_placeholder(container=container, handle=handle)

    return


@phantom.playbook_block()
def ews_block_sender_placeholder(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ews_block_sender_placeholder() called")

    filtered_artifact_0_data_filter_file_by_provider = phantom.collect2(container=container, datapath=["filtered-data:filter_file_by_provider:condition_2:artifact:*.cef.ioc"])

    filtered_artifact_0__cef_ioc = [item[0] for item in filtered_artifact_0_data_filter_file_by_provider]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for item in filtered_artifact_0__cef_ioc:
        phantom.debug(f'{item} submitted to EWS for O365 block sender action')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def code_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_6() called")

    filtered_artifact_0_data_filter_file_by_provider = phantom.collect2(container=container, datapath=["filtered-data:filter_file_by_provider:condition_2:artifact:*.cef.ioc"])

    filtered_artifact_0__cef_ioc = [item[0] for item in filtered_artifact_0_data_filter_file_by_provider]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for item in filtered_artifact_0__cef_ioc:
        phantom.debug(f'file {item} is malicious and requires remediation')

    ################################################################################
    ## Custom Code End
    ################################################################################

    sentinelone_placeholder(container=container)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    filtered_artifact_0_data_filter_by_provider = phantom.collect2(container=container, datapath=["filtered-data:filter_by_provider:condition_1:artifact:*.cef.ioc"])

    filtered_artifact_0__cef_ioc = [item[0] for item in filtered_artifact_0_data_filter_by_provider]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for item in filtered_artifact_0__cef_ioc:
        phantom.debug(f'url {item} is malicious and requires remediation')

    ################################################################################
    ## Custom Code End
    ################################################################################

    ews_block_url_placeholder(container=container)

    return


@phantom.playbook_block()
def ews_block_url_placeholder(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ews_block_url_placeholder() called")

    filtered_artifact_0_data_filter_by_provider = phantom.collect2(container=container, datapath=["filtered-data:filter_by_provider:condition_1:artifact:*.cef.ioc"])

    filtered_artifact_0__cef_ioc = [item[0] for item in filtered_artifact_0_data_filter_by_provider]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for item in filtered_artifact_0__cef_ioc:
        phantom.debug(f'{item} submitted to EWS for O365 block url action')

    ################################################################################
    ## Custom Code End
    ################################################################################

    join_ews_block_sender_placeholder(container=container)

    return


@phantom.playbook_block()
def playbook_attack_analyzer_update_malicious_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_attack_analyzer_update_malicious_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Attack Analyzer Update Malicious", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Attack Analyzer Update Malicious", container=container, name="playbook_attack_analyzer_update_malicious_1", callback=filter_for_malicious)

    return


@phantom.playbook_block()
def code_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_7() called")

    filtered_artifact_0_data_filter_by_provider = phantom.collect2(container=container, datapath=["filtered-data:filter_by_provider:condition_4:artifact:*.cef.ioc"])

    filtered_artifact_0__cef_ioc = [item[0] for item in filtered_artifact_0_data_filter_by_provider]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for item in filtered_artifact_0__cef_ioc:
        phantom.debug(f'Domain {item} is malicious and requires remediation')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def filter_by_ioc_type(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_by_ioc_type() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_for_malicious:condition_1:artifact:*.cef.ioctype", "==", "file"]
        ],
        name="filter_by_ioc_type:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        filter_file_by_provider(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_for_malicious:condition_1:artifact:*.cef.ioctype", "==", "url"]
        ],
        name="filter_by_ioc_type:condition_2",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        filter_url_by_provider(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_2, filtered_results=matched_results_2)

    # collect filtered artifact ids and results for 'if' condition 3
    matched_artifacts_3, matched_results_3 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_for_malicious:condition_1:artifact:*.cef.ioctype", "==", "ip"]
        ],
        name="filter_by_ioc_type:condition_3",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_3 or matched_results_3:
        code_4(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_3, filtered_results=matched_results_3)

    # collect filtered artifact ids and results for 'if' condition 4
    matched_artifacts_4, matched_results_4 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_for_malicious:condition_1:artifact:*.cef.ioctype", "==", "domain"]
        ],
        name="filter_by_ioc_type:condition_4",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_4 or matched_results_4:
        code_7(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_4, filtered_results=matched_results_4)

    return


@phantom.playbook_block()
def filter_url_by_provider(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_url_by_provider() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_by_ioc_type:condition_2:artifact:*.cef.provider", "==", "splunk attack analyzer"]
        ],
        name="filter_url_by_provider:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        code_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:filter_by_ioc_type:condition_2:artifact:*.cef.provider", "==", "virustotal"]
        ],
        name="filter_url_by_provider:condition_2",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        pass

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