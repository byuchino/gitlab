"""
Top-level handler for outstanding Attack Analyzer work.\nFirst calls a playbook to process pending Attack Analyzer jobs.  Next, calls a playbook to update the container pending tag based on the results of the previous playbook.  Finally, based on updated tag, either set the label to a non-triggering value, or call playbook to enable the remediation handler.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_attack_analyzer_check_pending_jobs__template__1' block
    playbook_attack_analyzer_check_pending_jobs__template__1(container=container)

    return

@phantom.playbook_block()
def playbook_attack_analyzer_check_pending_jobs__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_attack_analyzer_check_pending_jobs__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Attack Analyzer Check Pending Jobs [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Attack Analyzer Check Pending Jobs [Template]", container=container, name="playbook_attack_analyzer_check_pending_jobs__template__1", callback=playbook_attack_analyzer_update_container_tag__template__1)

    return


@phantom.playbook_block()
def playbook_attack_analyzer_update_container_tag__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_attack_analyzer_update_container_tag__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Attack Analyzer Update Container Tag [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Attack Analyzer Update Container Tag [Template]", container=container, name="playbook_attack_analyzer_update_container_tag__template__1", callback=decision_1)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_1() called")

    tags_value = container.get("tags", None)

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["saa_pending", "in", tags_value]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        set_label_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    playbook_attack_analyzer_trigger_remediation__template__1(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def set_label_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("set_label_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.set_label(container=container, label="saa_job_wait")

    container = phantom.get_container(container.get('id', None))

    return


@phantom.playbook_block()
def playbook_attack_analyzer_trigger_remediation__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_attack_analyzer_trigger_remediation__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Attack Analyzer Trigger Remediation [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Attack Analyzer Trigger Remediation [Template]", container=container, name="playbook_attack_analyzer_trigger_remediation__template__1", callback=playbook_attack_analyzer_trigger_remediation__template__1_callback)

    return


@phantom.playbook_block()
def playbook_attack_analyzer_trigger_remediation__template__1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_attack_analyzer_trigger_remediation__template__1_callback() called")

    
    # Downstream End block cannot be called directly, since execution will call on_finish automatically.
    # Using placeholder callback function so child playbook is run synchronously.


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