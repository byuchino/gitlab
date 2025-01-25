"""
Check outstanding attack analyzer jobs for completion.  Perform &quot;get job summary&quot; action for artifacts tagged with &quot;saa_pending&quot; - they hold the job IDs for pending jobs - and clear the tag for each completed job.  Finally, update the container tag based on remaining tagged artifacts.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_for_pending' block
    filter_for_pending(container=container)

    return

@phantom.playbook_block()
def filter_for_pending(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_for_pending() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["saa_pending", "in", "artifact:*.tags"]
        ],
        name="filter_for_pending:condition_1",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        code_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)
        get_job_summary_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["saa_pending", "not in", "artifact:*.tags"]
        ],
        name="filter_for_pending:condition_2",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        code_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_2, filtered_results=matched_results_2)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    filtered_artifact_0_data_filter_for_pending = phantom.collect2(container=container, datapath=["filtered-data:filter_for_pending:condition_1:artifact:*.id"])

    filtered_artifact_0__id = [item[0] for item in filtered_artifact_0_data_filter_for_pending]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'tag found in artifact id {filtered_artifact_0__id}')
 
    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_2() called")

    filtered_artifact_0_data_filter_for_pending = phantom.collect2(container=container, datapath=["filtered-data:filter_for_pending:condition_2:artifact:*.id"])

    filtered_artifact_0__id = [item[0] for item in filtered_artifact_0_data_filter_for_pending]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'tag not found in artifact {filtered_artifact_0__id}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def get_job_summary_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("get_job_summary_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    filtered_artifact_0_data_filter_for_pending = phantom.collect2(container=container, datapath=["filtered-data:filter_for_pending:condition_1:artifact:*.cef.jobid","filtered-data:filter_for_pending:condition_1:artifact:*.id"], scope="all")

    parameters = []

    # build parameters list for 'get_job_summary_1' call
    for filtered_artifact_0_item_filter_for_pending in filtered_artifact_0_data_filter_for_pending:
        if filtered_artifact_0_item_filter_for_pending[0] is not None:
            parameters.append({
                "job_id": filtered_artifact_0_item_filter_for_pending[0],
                "context": {'artifact_id': filtered_artifact_0_item_filter_for_pending[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'parameters:  {json.dumps(parameters, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get job summary", parameters=parameters, name="get_job_summary_1", assets=["saa_asset"], callback=action_status)

    return


@phantom.playbook_block()
def action_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("action_status() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["get_job_summary_1:action_result.status", "==", "success"]
        ],
        name="action_status:condition_1",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        job_state(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["get_job_summary_1:action_result.status", "!=", "success"]
        ],
        name="action_status:condition_2",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        pass

    return


@phantom.playbook_block()
def job_state(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("job_state() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:action_status:condition_1:get_job_summary_1:action_result.data.*.State", "==", "done"]
        ],
        name="job_state:condition_1",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        format_artifact_json(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)
        format_job_complete_note(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:action_status:condition_1:get_job_summary_1:action_result.data.*.State", "!=", "done"]
        ],
        name="job_state:condition_2",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        pass

    return


@phantom.playbook_block()
def artifact_update_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_update_1() called")

    format_artifact_json__as_list = phantom.get_format_data(name="format_artifact_json__as_list")

    parameters = []

    # build parameters list for 'artifact_update_1' call
    for format_artifact_json__item in format_artifact_json__as_list:
        parameters.append({
            "name": None,
            "tags": None,
            "label": None,
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "input_json": format_artifact_json__item,
            "artifact_id": None,
            "cef_data_type": None,
            "overwrite_tags": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_update", parameters=parameters, name="artifact_update_1", callback=playbook_update_artifact_tags__utility__1)

    return


@phantom.playbook_block()
def format_artifact_json(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_artifact_json() called")

    template = """%%\n{{\"artifact_id\":\"{0}\",\"cef_data\":{{\"Score\":\"{1}\",\"Verdict\":\"{2}\"}}}}\n%%\n"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:job_state:condition_1:get_job_summary_1:action_result.parameter.context.artifact_id",
        "filtered-data:job_state:condition_1:get_job_summary_1:action_result.summary.Score",
        "filtered-data:job_state:condition_1:get_job_summary_1:action_result.summary.Verdict"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_artifact_json", scope="all")

    artifact_update_1(container=container)

    return


@phantom.playbook_block()
def playbook_update_artifact_tags__utility__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_update_artifact_tags__utility__1() called")

    filtered_result_0_data_job_state = phantom.collect2(container=container, datapath=["filtered-data:job_state:condition_1:get_job_summary_1:action_result.parameter.context.artifact_id"])

    filtered_result_0_parameter_context_artifact_id = [item[0] for item in filtered_result_0_data_job_state]

    inputs = {
        "artifact_id": filtered_result_0_parameter_context_artifact_id,
        "artifact_op": ["remove=saa_pending"],
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
def format_job_complete_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_job_complete_note() called")

    template = """%%\n{0}   \n\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:job_state:condition_1:get_job_summary_1:action_result.message"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_job_complete_note")

    add_job_complete_note(container=container)

    return


@phantom.playbook_block()
def add_job_complete_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_job_complete_note() called")

    format_job_complete_note = phantom.get_format_data(name="format_job_complete_note")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content=format_job_complete_note, note_format="markdown", note_type="general", title="Attack Analyzer Job Complete")

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