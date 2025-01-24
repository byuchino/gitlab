"""
Main VirusTotal enrichment playbook.\nCalls VirusTotal enrichment playbook for each IOC type, then tags all artifacts determined to be malicious.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_virustotal_url_enrichment__template__1' block
    playbook_virustotal_url_enrichment__template__1(container=container)

    return

@phantom.playbook_block()
def playbook_virustotal_url_enrichment__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_virustotal_url_enrichment__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Virustotal URL Enrichment [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Virustotal URL Enrichment [Template]", container=container, name="playbook_virustotal_url_enrichment__template__1", callback=playbook_virustotal_file_hash_enrichment__template__1)

    return


@phantom.playbook_block()
def playbook_virustotal_file_hash_enrichment__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_virustotal_file_hash_enrichment__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Virustotal File Hash Enrichment [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Virustotal File Hash Enrichment [Template]", container=container, name="playbook_virustotal_file_hash_enrichment__template__1", callback=playbook_virustotal_ip_reputation_enrichment__template__1)

    return


@phantom.playbook_block()
def playbook_virustotal_ip_reputation_enrichment__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_virustotal_ip_reputation_enrichment__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Virustotal IP Reputation Enrichment [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Virustotal IP Reputation Enrichment [Template]", container=container, name="playbook_virustotal_ip_reputation_enrichment__template__1", callback=playbook_virustotal_domain_reputation_enrichment__template__1)

    return


@phantom.playbook_block()
def playbook_virustotal_domain_reputation_enrichment__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_virustotal_domain_reputation_enrichment__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Virustotal Domain Reputation Enrichment [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Virustotal Domain Reputation Enrichment [Template]", container=container, name="playbook_virustotal_domain_reputation_enrichment__template__1", callback=playbook_virustotal_update_malicious_1)

    return


@phantom.playbook_block()
def playbook_virustotal_update_malicious_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_virustotal_update_malicious_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Virustotal Update Malicious", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Virustotal Update Malicious", container=container, name="playbook_virustotal_update_malicious_1", callback=playbook_virustotal_update_malicious_1_callback)

    return


@phantom.playbook_block()
def playbook_virustotal_update_malicious_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_virustotal_update_malicious_1_callback() called")

    
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