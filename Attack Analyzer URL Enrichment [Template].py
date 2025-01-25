"""
Submits URL(s) to Attack Analyzer for detonation.  Stores detonation job ID(s) from response in new artifact(s) for later processing and tags the container with &quot;saa_job_wait&quot;
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'urls_only_filter' block
    urls_only_filter(container=container)

    return

@phantom.playbook_block()
def attack_analyzer_detonate_url(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("attack_analyzer_detonate_url() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    merge_into_single_list__result = phantom.collect2(container=container, datapath=["merge_into_single_list:custom_function_result.data.item"])

    parameters = []

    # build parameters list for 'attack_analyzer_detonate_url' call
    for merge_into_single_list__result_item in merge_into_single_list__result:
        if merge_into_single_list__result_item[0] is not None:
            parameters.append({
                "url": merge_into_single_list__result_item[0],
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'parameters:  {json.dumps(parameters, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("detonate url", parameters=parameters, name="attack_analyzer_detonate_url", assets=["saa_asset"], callback=check_status)

    return


@phantom.playbook_block()
def urls_only_filter(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("urls_only_filter() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.cef.requestURL", "!=", ""]
        ],
        name="urls_only_filter:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        merge_into_single_list(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def merge_into_single_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("merge_into_single_list() called")

    filtered_artifact_0_data_urls_only_filter = phantom.collect2(container=container, datapath=["filtered-data:urls_only_filter:condition_1:artifact:*.cef.requestURL","filtered-data:urls_only_filter:condition_1:artifact:*.id"])

    filtered_artifact_0__cef_requesturl = [item[0] for item in filtered_artifact_0_data_urls_only_filter]

    parameters = []

    parameters.append({
        "input_1": filtered_artifact_0__cef_requesturl,
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

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="merge_into_single_list", callback=attack_analyzer_detonate_url)

    return


@phantom.playbook_block()
def check_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("check_status() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["attack_analyzer_detonate_url:action_result.status", "==", "success"]
        ],
        name="check_status:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        format_artifact_json(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["attack_analyzer_detonate_url:action_result.status", "!=", "success"]
        ],
        name="check_status:condition_2",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        format_detonate_failure_note(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_2, filtered_results=matched_results_2)

    return


@phantom.playbook_block()
def artifact_create_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_create_2() called")

    id_value = container.get("id", None)
    format_artifact_json__as_list = phantom.get_format_data(name="format_artifact_json__as_list")

    parameters = []

    # build parameters list for 'artifact_create_2' call
    for format_artifact_json__item in format_artifact_json__as_list:
        parameters.append({
            "name": "attack analyzer url detonation",
            "tags": "saa_pending",
            "label": None,
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "container": id_value,
            "input_json": format_artifact_json__item,
            "cef_data_type": None,
            "run_automation": None,
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


@phantom.playbook_block()
def format_detonate_failure_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_detonate_failure_note() called")

    template = """%%\n{0}: {1}  \n%%"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:check_status:condition_2:attack_analyzer_detonate_url:action_result.parameter.url",
        "filtered-data:check_status:condition_2:attack_analyzer_detonate_url:action_result.message"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_detonate_failure_note")

    add_note_4(container=container)

    return


@phantom.playbook_block()
def add_note_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_4() called")

    format_detonate_failure_note = phantom.get_format_data(name="format_detonate_failure_note")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content=format_detonate_failure_note, note_format="markdown", note_type="general", title="Attack Analyzer URL Detonation Failure ")

    return


@phantom.playbook_block()
def format_artifact_json(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_artifact_json() called")

    template = """%%\n{{\"cef_data\":{{\"ioc\":\"{0}\",\"ioctype\":\"url\",\"provider\":\"splunk attack analyzer\",\"jobid\":\"{1}\"}}}}\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:check_status:condition_1:attack_analyzer_detonate_url:action_result.parameter.url",
        "filtered-data:check_status:condition_1:attack_analyzer_detonate_url:action_result.data.*.JobID"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_artifact_json")

    artifact_create_2(container=container)

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