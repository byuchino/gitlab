"""
Automation playbook to perform IP reputation checks using VirusTotal V3.  Result summary is written back to the originating MC Incident as event data as well as in a note.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


################################################################################
## Global Custom Code Start
################################################################################
from math import log


################################################################################
## Global Custom Code End
################################################################################

@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_iocs' block
    filter_iocs(container=container)

    return

@phantom.playbook_block()
def vt_reputation_check_ip(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("vt_reputation_check_ip() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    remove_duplicates_data = phantom.collect2(container=container, datapath=["remove_duplicates:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'vt_reputation_check_ip' call
    for remove_duplicates_data_item in remove_duplicates_data:
        if remove_duplicates_data_item[0] is not None:
            parameters.append({
                "ip": remove_duplicates_data_item[0],
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("ip reputation", parameters=parameters, name="vt_reputation_check_ip", assets=["virustotalv3"], callback=filter_results)

    return


@phantom.playbook_block()
def format_reputation_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_reputation_note() called")

    template = """%%\nIP:  {0}  \nReputation Summary:  {1}  \nNormalized Score Index:  {2}, {3}  \n\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:filter_results:condition_1:vt_reputation_check_ip:action_result.parameter.ip",
        "filtered-data:filter_results:condition_1:vt_reputation_check_ip:action_result.summary",
        "normalize_score_ip:custom_function:score_index",
        "normalize_score_ip:custom_function:score"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_reputation_note")

    add_ip_reputation_note(container=container)

    return


@phantom.playbook_block()
def remove_duplicates(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("remove_duplicates() called")

    merge_ioc_lists__result = phantom.collect2(container=container, datapath=["merge_ioc_lists:custom_function_result.data.item"])

    merge_ioc_lists_data_item = [item[0] for item in merge_ioc_lists__result]

    parameters = []

    parameters.append({
        "input_list": merge_ioc_lists_data_item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_deduplicate", parameters=parameters, name="remove_duplicates", callback=vt_reputation_check_ip)

    return


@phantom.playbook_block()
def add_ip_reputation_failed_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_ip_reputation_failed_note() called")

    format_reputation_failed_note = phantom.get_format_data(name="format_reputation_failed_note")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content=format_reputation_failed_note, note_format="markdown", note_type="general", title="IP Reputation check failed")

    return


@phantom.playbook_block()
def format_reputation_failed_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_reputation_failed_note() called")

    template = """%%\nVirus Total reputation check failed for IP: {0}\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:filter_results:condition_2:vt_reputation_check_ip:action_result.parameter.ip"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_reputation_failed_note")

    add_ip_reputation_failed_note(container=container)

    return


@phantom.playbook_block()
def add_ip_reputation_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_ip_reputation_note() called")

    format_reputation_note = phantom.get_format_data(name="format_reputation_note")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content=format_reputation_note, note_format="markdown", note_type="general", title="IP Reputation Check Results")

    return


@phantom.playbook_block()
def artifact_create_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_create_5() called")

    id_value = container.get("id", None)
    format_artifact_json__as_list = phantom.get_format_data(name="format_artifact_json__as_list")

    parameters = []

    # build parameters list for 'artifact_create_5' call
    for format_artifact_json__item in format_artifact_json__as_list:
        parameters.append({
            "name": "vt3_ip_reputation_result",
            "tags": None,
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

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_5")

    return


@phantom.playbook_block()
def filter_iocs(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_iocs() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="or",
        conditions=[
            ["artifact:*.cef.sourceAddress", "!=", ""],
            ["artifact:*.cef.destinationAddress", "!=", ""]
        ],
        name="filter_iocs:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        merge_ioc_lists(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def merge_ioc_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("merge_ioc_lists() called")

    filtered_artifact_0_data_filter_iocs = phantom.collect2(container=container, datapath=["filtered-data:filter_iocs:condition_1:artifact:*.cef.sourceAddress","filtered-data:filter_iocs:condition_1:artifact:*.cef.destinationAddress","filtered-data:filter_iocs:condition_1:artifact:*.id"])

    filtered_artifact_0__cef_sourceaddress = [item[0] for item in filtered_artifact_0_data_filter_iocs]
    filtered_artifact_0__cef_destinationaddress = [item[1] for item in filtered_artifact_0_data_filter_iocs]

    parameters = []

    parameters.append({
        "input_1": filtered_artifact_0__cef_sourceaddress,
        "input_2": filtered_artifact_0__cef_destinationaddress,
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

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="merge_ioc_lists", callback=remove_duplicates)

    return


@phantom.playbook_block()
def filter_results(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_results() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["vt_reputation_check_ip:action_result.status", "==", "success"]
        ],
        name="filter_results:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        normalize_score_ip(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["vt_reputation_check_ip:action_result.status", "!=", "success"]
        ],
        name="filter_results:condition_2",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        format_reputation_failed_note(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_2, filtered_results=matched_results_2)

    return


@phantom.playbook_block()
def format_artifact_json(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_artifact_json() called")

    template = """%%\n{{\"cef_data\":{{\"ip\":\"{0}\",\"ioctype\":\"ip\",\"provider\":\"virustotal\",\"summary\":\"{1}\",\"score\":\"{2}\",\"scoreindex\":{3}}}}}\n%%\n"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:filter_results:condition_1:vt_reputation_check_ip:action_result.parameter.ip",
        "filtered-data:filter_results:condition_1:vt_reputation_check_ip:action_result.summary",
        "normalize_score_ip:custom_function:score",
        "normalize_score_ip:custom_function:score_index"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_artifact_json")

    artifact_create_5(container=container)

    return


@phantom.playbook_block()
def normalize_score_ip(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("normalize_score_ip() called")

    filtered_result_0_data_filter_results = phantom.collect2(container=container, datapath=["filtered-data:filter_results:condition_1:vt_reputation_check_ip:action_result.summary"])

    filtered_result_0_summary = [item[0] for item in filtered_result_0_data_filter_results]

    normalize_score_ip__ip_score_object = None
    normalize_score_ip__score = None
    normalize_score_ip__score_index = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    score_table = {
        "0":"Unknown",
        "1":"Very_Safe",
        "2":"Safe",
        "3":"Probably_Safe",
        "4":"Leans_Safe",
        "5":"May_not_be_Safe",
        "6":"Exercise_Caution",
        "7":"Suspicious_or_Risky",
        "8":"Possibly_Malicious",
        "9":"Probably_Malicious",
        "10":"Malicious"
    }
    
    ip_summary_list = filtered_result_0_summary
    normalize_score_ip__ip_score_object = []
    normalize_score_ip__score = []
    normalize_score_ip__score_index = []
    
    for summary_data in ip_summary_list:
        # Set confidence based on percentage of vendors undetected
        # Reduce the confidence by percentage of vendors undetected.
        vendors = summary_data['harmless'] + summary_data['undetected'] + summary_data['malicious'] + summary_data['suspicious']
        if not vendors:
            vendors = 1
        confidence = 100 - int((summary_data['undetected']/vendors) * 100)
        
        # Normalize reputation on a 10 point scale based on number of malicious and suspicious divided by harmless vendors
        # This can be adjusted to include whatever logic is desired.
        suspect = summary_data['malicious'] + summary_data['suspicious']
        # If there are only harmless verdicts and no suspicious entries, set score_id to 1.
        if not suspect:
            score_id = 1
        else:
            # customize score calculation as desired
            log_result = log((suspect/vendors) * 100, 100) # log imported from math in global code block
            score_id = int(log_result * 10) + 3
            if score_id > 10:
                score_id = 10
            
        score = score_table[str(score_id)]

        normalize_score_ip__ip_score_object.append({'score': score, 'score_id': score_id, 'confidence': confidence})
        normalize_score_ip__score.append(score)
        normalize_score_ip__score_index.append(score_id)

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="normalize_score_ip:ip_score_object", value=json.dumps(normalize_score_ip__ip_score_object))
    phantom.save_run_data(key="normalize_score_ip:score", value=json.dumps(normalize_score_ip__score))
    phantom.save_run_data(key="normalize_score_ip:score_index", value=json.dumps(normalize_score_ip__score_index))

    format_artifact_json(container=container)
    format_reputation_note(container=container)

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