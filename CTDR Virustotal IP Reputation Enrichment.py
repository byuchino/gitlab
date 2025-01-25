"""
Automation playbook to perform IP reputation checks using VirusTotal V3.  Result summary is written back to the originating MC Incident as event data as well as in a note.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'merge_ip_ioc_lists' block
    merge_ip_ioc_lists(container=container)

    return

@phantom.playbook_block()
def vt_reputation_check_ip(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("vt_reputation_check_ip() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    remove_duplicate_ips_data = phantom.collect2(container=container, datapath=["remove_duplicate_ips:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'vt_reputation_check_ip' call
    for remove_duplicate_ips_data_item in remove_duplicate_ips_data:
        if remove_duplicate_ips_data_item[0] is not None:
            parameters.append({
                "ip": remove_duplicate_ips_data_item[0],
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("ip reputation", parameters=parameters, name="vt_reputation_check_ip", assets=["production virustotal3"], callback=db_is_reputation_check_success_ip)

    return


@phantom.playbook_block()
def mc_note_reputation_ip(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_note_reputation_ip() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    title_formatted_string = phantom.format(
        container=container,
        template="""IP Reputation check results - {0}\n""",
        parameters=[
            "vt_reputation_check_ip:action_result.parameter.ip"
        ])
    content_formatted_string = phantom.format(
        container=container,
        template="""{0}""",
        parameters=[
            "format_reputation_note:formatted_data.*"
        ])

    external_id_value = container.get("external_id", None)
    vt_reputation_check_ip_result_data = phantom.collect2(container=container, datapath=["vt_reputation_check_ip:action_result.parameter.ip","vt_reputation_check_ip:action_result.parameter.context.artifact_id","vt_reputation_check_ip:action_result.parameter.context.artifact_external_id"], action_results=results)
    format_reputation_note__as_list = phantom.get_format_data(name="format_reputation_note__as_list")

    parameters = []

    # build parameters list for 'mc_note_reputation_ip' call
    for vt_reputation_check_ip_result_item in vt_reputation_check_ip_result_data:
        for format_reputation_note__item in format_reputation_note__as_list:
            if external_id_value is not None and title_formatted_string is not None and content_formatted_string is not None:
                parameters.append({
                    "id": external_id_value,
                    "title": title_formatted_string,
                    "content": content_formatted_string,
                    "context": {'artifact_id': vt_reputation_check_ip_result_item[1], 'artifact_external_id': vt_reputation_check_ip_result_item[2]},
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add incident note", parameters=parameters, name="mc_note_reputation_ip", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def db_is_reputation_check_success_ip(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("db_is_reputation_check_success_ip() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["vt_reputation_check_ip:action_result.status", "==", "success"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        mc_event_reputation_ip(action=action, success=success, container=container, results=results, handle=handle)
        format_reputation_note(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    mc_note_reputation_failed_ip(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def mc_note_reputation_failed_ip(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_note_reputation_failed_ip() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    content_formatted_string = phantom.format(
        container=container,
        template="""Virus Total reputation check failed for IP: {0}\n""",
        parameters=[
            "vt_reputation_check_ip:action_result.parameter.ip"
        ])

    external_id_value = container.get("external_id", None)
    vt_reputation_check_ip_result_data = phantom.collect2(container=container, datapath=["vt_reputation_check_ip:action_result.parameter.ip","vt_reputation_check_ip:action_result.parameter.context.artifact_id","vt_reputation_check_ip:action_result.parameter.context.artifact_external_id"], action_results=results)

    parameters = []

    # build parameters list for 'mc_note_reputation_failed_ip' call
    for vt_reputation_check_ip_result_item in vt_reputation_check_ip_result_data:
        if external_id_value is not None and content_formatted_string is not None:
            parameters.append({
                "id": external_id_value,
                "title": "IP Reputation check failed",
                "content": content_formatted_string,
                "context": {'artifact_id': vt_reputation_check_ip_result_item[1], 'artifact_external_id': vt_reputation_check_ip_result_item[2]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add incident note", parameters=parameters, name="mc_note_reputation_failed_ip", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def mc_event_reputation_ip(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_event_reputation_ip() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    external_id_value = container.get("external_id", None)
    vt_reputation_check_ip_result_data = phantom.collect2(container=container, datapath=["vt_reputation_check_ip:action_result.parameter.ip","vt_reputation_check_ip:action_result.summary","vt_reputation_check_ip:action_result.parameter.context.artifact_id","vt_reputation_check_ip:action_result.parameter.context.artifact_external_id"], action_results=results)

    parameters = []

    # build parameters list for 'mc_event_reputation_ip' call
    for vt_reputation_check_ip_result_item in vt_reputation_check_ip_result_data:
        if external_id_value is not None:
            parameters.append({
                "pairs": [
                    { "name": vt_reputation_check_ip_result_item[0], "value": vt_reputation_check_ip_result_item[1] },
                ],
                "incident_id": external_id_value,
                "context": {'artifact_id': vt_reputation_check_ip_result_item[2], 'artifact_external_id': vt_reputation_check_ip_result_item[3]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("create events", parameters=parameters, name="mc_event_reputation_ip", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def format_reputation_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_reputation_note() called")

    template = """%%\nIP:  {0}\nReputation Summary:  {1}\n\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "vt_reputation_check_ip:action_result.parameter.ip",
        "vt_reputation_check_ip:action_result.summary"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_reputation_note")

    mc_note_reputation_ip(container=container)

    return


@phantom.playbook_block()
def decision_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_2() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["merge_ip_ioc_lists:custom_function_result.data.item", "!=", ""]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        remove_duplicate_ips(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def merge_ip_ioc_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("merge_ip_ioc_lists() called")

    data_summary_src_value = container.get("data", {}).get("summary", {}).get("src", None)
    data_summary_src_ip_value = container.get("data", {}).get("summary", {}).get("src_ip", None)
    data_summary_dest_value = container.get("data", {}).get("summary", {}).get("dest", None)
    data_summary_dest_ip_value = container.get("data", {}).get("summary", {}).get("dest_ip", None)
    data_summary_values_src__value = container.get("data", {}).get("summary", {}).get("values(src)", None)
    data_summary_values_dest__value = container.get("data", {}).get("summary", {}).get("values(dest)", None)
    data_summary_orig_host_value = container.get("data", {}).get("summary", {}).get("orig_host", None)

    parameters = []

    parameters.append({
        "input_1": data_summary_src_value,
        "input_2": data_summary_src_ip_value,
        "input_3": data_summary_dest_value,
        "input_4": data_summary_dest_ip_value,
        "input_5": data_summary_values_src__value,
        "input_6": data_summary_values_dest__value,
        "input_7": data_summary_orig_host_value,
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

    phantom.custom_function(custom_function="local/list_merge_handle_all_none", parameters=parameters, name="merge_ip_ioc_lists", callback=decision_2)

    return


@phantom.playbook_block()
def remove_duplicate_ips(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("remove_duplicate_ips() called")

    merge_ip_ioc_lists__result = phantom.collect2(container=container, datapath=["merge_ip_ioc_lists:custom_function_result.data.item"])

    merge_ip_ioc_lists_data_item = [item[0] for item in merge_ip_ioc_lists__result]

    parameters = []

    parameters.append({
        "input_list": merge_ip_ioc_lists_data_item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_deduplicate", parameters=parameters, name="remove_duplicate_ips", callback=vt_reputation_check_ip)

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