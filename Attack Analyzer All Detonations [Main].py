"""
Main Attack Analyzer detonation playbook.\nCalls the Attack Analyzer file and URL detonation playbooks to launch the detonation jobs, then tags the container with saa_pending.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_attack_analyzer_file_enrichment__template__1' block
    playbook_attack_analyzer_file_enrichment__template__1(container=container)

    return

@phantom.playbook_block()
def playbook_attack_analyzer_file_enrichment__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_attack_analyzer_file_enrichment__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Attack Analyzer File Enrichment [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Attack Analyzer File Enrichment [Template]", container=container, name="playbook_attack_analyzer_file_enrichment__template__1", callback=playbook_attack_analyzer_url_enrichment__template__1)

    return


@phantom.playbook_block()
def playbook_attack_analyzer_url_enrichment__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_attack_analyzer_url_enrichment__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Attack Analyzer URL Enrichment [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Attack Analyzer URL Enrichment [Template]", container=container, name="playbook_attack_analyzer_url_enrichment__template__1", callback=playbook_attack_analyzer_update_container_tag__template__1)

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
    playbook_run_id = phantom.playbook("phantom_pb_templates/Attack Analyzer Update Container Tag [Template]", container=container, name="playbook_attack_analyzer_update_container_tag__template__1", callback=playbook_attack_analyzer_update_container_tag__template__1_callback)

    return


@phantom.playbook_block()
def playbook_attack_analyzer_update_container_tag__template__1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_attack_analyzer_update_container_tag__template__1_callback() called")

    
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