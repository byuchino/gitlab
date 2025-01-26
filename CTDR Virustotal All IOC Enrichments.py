"""
Automation playbook to perform enrichment for the following ioc types:  IP, Domain, URL, and file hash.  Calls separate child enrichment playbooks for each ioc type.\n
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_ctdr_virustotal_domain_reputation_enrichment_1' block
    playbook_ctdr_virustotal_domain_reputation_enrichment_1(container=container)
    # call 'playbook_ctdr_virustotal_ip_reputation_enrichment_1' block
    playbook_ctdr_virustotal_ip_reputation_enrichment_1(container=container)
    # call 'playbook_ctdr_virustotal_url_enrichment_1' block
    playbook_ctdr_virustotal_url_enrichment_1(container=container)
    # call 'playbook_ctdr_virustotal_file_hash_enrichment_1' block
    playbook_ctdr_virustotal_file_hash_enrichment_1(container=container)

    return

@phantom.playbook_block()
def playbook_ctdr_virustotal_domain_reputation_enrichment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_ctdr_virustotal_domain_reputation_enrichment_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/CTDR Virustotal Domain Reputation Enrichment", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/CTDR Virustotal Domain Reputation Enrichment", container=container)

    return


@phantom.playbook_block()
def playbook_ctdr_virustotal_ip_reputation_enrichment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_ctdr_virustotal_ip_reputation_enrichment_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/CTDR Virustotal IP Reputation Enrichment", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/CTDR Virustotal IP Reputation Enrichment", container=container)

    return


@phantom.playbook_block()
def playbook_ctdr_virustotal_url_enrichment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_ctdr_virustotal_url_enrichment_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/CTDR Virustotal URL Enrichment", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/CTDR Virustotal URL Enrichment", container=container)

    return


@phantom.playbook_block()
def playbook_ctdr_virustotal_file_hash_enrichment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_ctdr_virustotal_file_hash_enrichment_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/CTDR Virustotal File Hash Enrichment", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/CTDR Virustotal File Hash Enrichment", container=container)

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