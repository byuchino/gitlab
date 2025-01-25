"""
Automation playbook to perform domain reputation checks using VirusTotal V3.  Result summary is written back to the originating MC Incident as event data as well as in a note.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'merge_domain_ioc_lists_1' block
    merge_domain_ioc_lists_1(container=container)

    return

@phantom.playbook_block()
def vt_reputation_check_domain(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("vt_reputation_check_domain() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    remove_duplicate_domains_data = phantom.collect2(container=container, datapath=["remove_duplicate_domains:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'vt_reputation_check_domain' call
    for remove_duplicate_domains_data_item in remove_duplicate_domains_data:
        if remove_duplicate_domains_data_item[0] is not None:
            parameters.append({
                "domain": remove_duplicate_domains_data_item[0],
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("domain reputation", parameters=parameters, name="vt_reputation_check_domain", assets=["production virustotal3"], callback=decision_1)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["vt_reputation_check_domain:action_result.status", "==", "success"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        mc_event_reputation_domain(action=action, success=success, container=container, results=results, handle=handle)
        format_reputation_note(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    mc_note_reputation_failed_domain(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def mc_note_reputation_failed_domain(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_note_reputation_failed_domain() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    content_formatted_string = phantom.format(
        container=container,
        template="""Virus Total reputation check failed for domain: {0}\n""",
        parameters=[
            "vt_reputation_check_domain:action_result.parameter.domain"
        ])

    external_id_value = container.get("external_id", None)
    vt_reputation_check_domain_result_data = phantom.collect2(container=container, datapath=["vt_reputation_check_domain:action_result.parameter.domain","vt_reputation_check_domain:action_result.parameter.context.artifact_id","vt_reputation_check_domain:action_result.parameter.context.artifact_external_id"], action_results=results)

    parameters = []

    # build parameters list for 'mc_note_reputation_failed_domain' call
    for vt_reputation_check_domain_result_item in vt_reputation_check_domain_result_data:
        if external_id_value is not None and content_formatted_string is not None:
            parameters.append({
                "id": external_id_value,
                "title": "Domain Reputation check failed",
                "content": content_formatted_string,
                "context": {'artifact_id': vt_reputation_check_domain_result_item[1], 'artifact_external_id': vt_reputation_check_domain_result_item[2]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add incident note", parameters=parameters, name="mc_note_reputation_failed_domain", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def mc_note_reputation_domain(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_note_reputation_domain() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    title_formatted_string = phantom.format(
        container=container,
        template="""Domain Reputation check results - {0}\n\n""",
        parameters=[
            "vt_reputation_check_domain:action_result.parameter.domain"
        ])
    content_formatted_string = phantom.format(
        container=container,
        template="""{0}\n""",
        parameters=[
            "format_reputation_note:formatted_data.*"
        ])

    external_id_value = container.get("external_id", None)
    vt_reputation_check_domain_result_data = phantom.collect2(container=container, datapath=["vt_reputation_check_domain:action_result.parameter.domain","vt_reputation_check_domain:action_result.parameter.context.artifact_id","vt_reputation_check_domain:action_result.parameter.context.artifact_external_id"], action_results=results)
    format_reputation_note__as_list = phantom.get_format_data(name="format_reputation_note__as_list")

    parameters = []

    # build parameters list for 'mc_note_reputation_domain' call
    for vt_reputation_check_domain_result_item in vt_reputation_check_domain_result_data:
        for format_reputation_note__item in format_reputation_note__as_list:
            if external_id_value is not None and title_formatted_string is not None and content_formatted_string is not None:
                parameters.append({
                    "id": external_id_value,
                    "title": title_formatted_string,
                    "content": content_formatted_string,
                    "context": {'artifact_id': vt_reputation_check_domain_result_item[1], 'artifact_external_id': vt_reputation_check_domain_result_item[2]},
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add incident note", parameters=parameters, name="mc_note_reputation_domain", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def mc_event_reputation_domain(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_event_reputation_domain() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    external_id_value = container.get("external_id", None)
    vt_reputation_check_domain_result_data = phantom.collect2(container=container, datapath=["vt_reputation_check_domain:action_result.parameter.domain","vt_reputation_check_domain:action_result.summary","vt_reputation_check_domain:action_result.parameter.context.artifact_id","vt_reputation_check_domain:action_result.parameter.context.artifact_external_id"], action_results=results)

    parameters = []

    # build parameters list for 'mc_event_reputation_domain' call
    for vt_reputation_check_domain_result_item in vt_reputation_check_domain_result_data:
        if external_id_value is not None:
            parameters.append({
                "pairs": [
                    { "name": vt_reputation_check_domain_result_item[0], "value": vt_reputation_check_domain_result_item[1] },
                ],
                "incident_id": external_id_value,
                "context": {'artifact_id': vt_reputation_check_domain_result_item[2], 'artifact_external_id': vt_reputation_check_domain_result_item[3]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("create events", parameters=parameters, name="mc_event_reputation_domain", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def normalize_domain_names(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("normalize_domain_names() called")

    merge_domain_ioc_lists_1__result = phantom.collect2(container=container, datapath=["merge_domain_ioc_lists_1:custom_function_result.data.item"])

    merge_domain_ioc_lists_1_data_item = [item[0] for item in merge_domain_ioc_lists_1__result]

    parameters = []

    parameters.append({
        "domain_list": merge_domain_ioc_lists_1_data_item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="local/list_fixup_domain_names", parameters=parameters, name="normalize_domain_names", callback=check_for_iocs)

    return


@phantom.playbook_block()
def format_reputation_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_reputation_note() called")

    template = """%%\nDomain:  {0}\nReputation Summary:  {1}\n\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "vt_reputation_check_domain:action_result.parameter.domain",
        "vt_reputation_check_domain:action_result.summary"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_reputation_note")

    mc_note_reputation_domain(container=container)

    return


@phantom.playbook_block()
def merge_domain_ioc_lists_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("merge_domain_ioc_lists_1() called")

    data_summary_src_dns_value = container.get("data", {}).get("summary", {}).get("src_dns", None)
    data_summary_dest_dns_value = container.get("data", {}).get("summary", {}).get("dest_dns", None)
    data_summary_ext_domain_value = container.get("data", {}).get("summary", {}).get("ext_domain", None)

    parameters = []

    parameters.append({
        "input_1": data_summary_src_dns_value,
        "input_2": data_summary_dest_dns_value,
        "input_3": data_summary_ext_domain_value,
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

    phantom.custom_function(custom_function="local/list_merge_handle_all_none", parameters=parameters, name="merge_domain_ioc_lists_1", callback=check_for_iocs_1)

    return


@phantom.playbook_block()
def check_for_iocs_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("check_for_iocs_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["merge_domain_ioc_lists_1:custom_function_result.data.item", "!=", ""]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        normalize_domain_names(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def check_for_iocs(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("check_for_iocs() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["normalize_domain_names:custom_function_result.data.item", "!=", ""]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        filter_domain_list(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def filter_domain_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_domain_list() called")

    normalize_domain_names__result = phantom.collect2(container=container, datapath=["normalize_domain_names:custom_function_result.data.item"])

    normalize_domain_names_data_item = [item[0] for item in normalize_domain_names__result]

    parameters = []

    parameters.append({
        "input_list": normalize_domain_names_data_item,
        "regex": "(?i)fmglobal\\.com",
        "action": "drop",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="local/regex_filter_list_handle_empty", parameters=parameters, name="filter_domain_list", callback=check_for_iocs_2)

    return


@phantom.playbook_block()
def check_for_iocs_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("check_for_iocs_2() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["filter_domain_list:custom_function_result.data.item", "!=", ""]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        remove_duplicate_domains(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def remove_duplicate_domains(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("remove_duplicate_domains() called")

    filter_domain_list__result = phantom.collect2(container=container, datapath=["filter_domain_list:custom_function_result.data.item"])

    filter_domain_list_data_item = [item[0] for item in filter_domain_list__result]

    parameters = []

    parameters.append({
        "input_list": filter_domain_list_data_item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_deduplicate", parameters=parameters, name="remove_duplicate_domains", callback=vt_reputation_check_domain)

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