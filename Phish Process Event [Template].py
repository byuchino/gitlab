"""
Main playbook for suspected phish events generated from the MS Graph for O365 on_poll action.\nCalls Virustotal playbooks for real time enrichment, followed by start of file and URL detonation jobs using Splunk Attack Analyzer.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_virustotal_all_ioc_enrichments__template__1' block
    playbook_virustotal_all_ioc_enrichments__template__1(container=container)

    return

@phantom.playbook_block()
def artifact_create_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_create_1() called")

    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "name": "attack analyzer remediation hook",
        "tags": "saa_remediation",
        "label": None,
        "severity": None,
        "cef_field": "remediation_label",
        "cef_value": "phish_remediate",
        "container": id_value,
        "input_json": None,
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

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_1", callback=playbook_attack_analyzer_all_detonations__main__1)

    return


@phantom.playbook_block()
def playbook_virustotal_all_ioc_enrichments__template__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_virustotal_all_ioc_enrichments__template__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Virustotal All IOC Enrichments [Template]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Virustotal All IOC Enrichments [Template]", container=container, name="playbook_virustotal_all_ioc_enrichments__template__1", callback=artifact_create_1)

    return


@phantom.playbook_block()
def playbook_attack_analyzer_all_detonations__main__1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_attack_analyzer_all_detonations__main__1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Attack Analyzer All Detonations [Main]", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Attack Analyzer All Detonations [Main]", container=container)

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