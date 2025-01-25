"""
This playbook triggers the execution of a remediation playbook(s) upon completion of all attack analyzer jobs.\nEnsure all outstanding attack analyzer jobs are complete, then check for the presence of a remediation artifact in the container.  If present (and there is only one), update the container label to the remediation_label value in the artifact.  This will trigger any playbook(s) with that label.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_for_remediation_artifact' block
    filter_for_remediation_artifact(container=container)

    return

@phantom.playbook_block()
def filter_for_remediation_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_for_remediation_artifact() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["saa_remediation", "in", "artifact:*.tags"],
            ["artifact:*.cef.remediation_label", "!=", ""]
        ],
        name="filter_for_remediation_artifact:condition_1",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        count_artifacts(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def update_container_label_from_remediation_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("update_container_label_from_remediation_artifact() called")

    id_value = container.get("id", None)
    filtered_artifact_0_data_filter_for_remediation_artifact = phantom.collect2(container=container, datapath=["filtered-data:filter_for_remediation_artifact:condition_1:artifact:*.cef.remediation_label","filtered-data:filter_for_remediation_artifact:condition_1:artifact:*.id"])

    parameters = []

    # build parameters list for 'update_container_label_from_remediation_artifact' call
    for filtered_artifact_0_item_filter_for_remediation_artifact in filtered_artifact_0_data_filter_for_remediation_artifact:
        parameters.append({
            "name": None,
            "tags": None,
            "label": filtered_artifact_0_item_filter_for_remediation_artifact[0],
            "owner": None,
            "status": None,
            "severity": None,
            "input_json": None,
            "description": None,
            "sensitivity": None,
            "container_input": id_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/container_update", parameters=parameters, name="update_container_label_from_remediation_artifact")

    return


@phantom.playbook_block()
def count_artifacts(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("count_artifacts() called")

    ################################################################################
    # Count the number of remediation artifacts - there should only be 1
    ################################################################################

    filtered_artifact_0_data_filter_for_remediation_artifact = phantom.collect2(container=container, datapath=["filtered-data:filter_for_remediation_artifact:condition_1:artifact:*.cef.remediation_label"], scope="all")

    filtered_artifact_0__cef_remediation_label = [item[0] for item in filtered_artifact_0_data_filter_for_remediation_artifact]

    count_artifacts__num_items = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    count_artifacts__num_items = len(filtered_artifact_0__cef_remediation_label)
    phantom.debug(f'list length:  {count_artifacts__num_items}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="count_artifacts:num_items", value=json.dumps(count_artifacts__num_items))

    number_of_artifacts(container=container)

    return


@phantom.playbook_block()
def number_of_artifacts(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("number_of_artifacts() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["count_artifacts:custom_function:num_items", "==", 1]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        update_container_label_from_remediation_artifact(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    format_error_note(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def format_error_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_error_note() called")

    template = """Error updating label for remediation handler - {0} remediation artifacts were found.  There must be exactly one.\n"""

    # parameter list for template variable replacement
    parameters = [
        "count_artifacts:custom_function:num_items"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_error_note")

    add_note_4(container=container)

    return


@phantom.playbook_block()
def add_note_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_4() called")

    format_error_note = phantom.get_format_data(name="format_error_note")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content=format_error_note, note_format="markdown", note_type="general", title="Remediation Update Error")

    return


@phantom.playbook_block()
def count_pending_jobs(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("count_pending_jobs() called")

    ################################################################################
    # Use REST api to find all artifacts tagged with the block input string.  Return 
    # count of artifacts found.
    ################################################################################

    input_parameter_0 = "saa_pending"

    count_pending_jobs__num_tags = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    check_tag = input_parameter_0
    
    id_value  = container.get("id", None)
    base_url  = phantom.build_phantom_rest_url('container')
    total_url = base_url + '/{0}/artifacts?_filter_tags__contains="{1}"'.format(str(id_value),check_tag)
    count     = 0
    
    response  = phantom.requests.get(total_url, verify=False)
    phantom.debug(f'response:  {json.dumps(response.json(), indent=4)}')
    
    if response.status_code == 200:
        count = response.json()['count']
    else:
        phantom.error(response.text)
    
    phantom.debug(f'There are {count} artifacts tagged {check_tag}')
    count_pending_jobs__num_tags = count
    
    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="count_pending_jobs:num_tags", value=json.dumps(count_pending_jobs__num_tags))

    decision_2(container=container)

    return


@phantom.playbook_block()
def decision_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_2() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["count_pending_jobs:custom_function:num_tags", "==", 0]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        return

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