"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'incident_iocs_present_6' block
    incident_iocs_present_6(container=container)

    return

@phantom.playbook_block()
def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_2() called")

    regex_filter_list_1__result = phantom.collect2(container=container, datapath=["regex_filter_list_1:custom_function_result.data.item"])

    regex_filter_list_1_data_item = [item[0] for item in regex_filter_list_1__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'after filter:  {json.dumps(regex_filter_list_1_data_item, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def list_merge_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("list_merge_3() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationDnsDomain","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "input_1": container_artifact_cef_item_0,
        "input_2": None,
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

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="list_merge_3", callback=code_5)

    return


@phantom.playbook_block()
def code_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_4() called")

    list_merge_3__result = phantom.collect2(container=container, datapath=["list_merge_3:custom_function_result.data.item"])

    list_merge_3_data_item = [item[0] for item in list_merge_3__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    input_list = list_merge_3_data_item
    
    outputs = []
    
    for item in input_list:
        split_list = item.split(".")
        if len(split_list) >= 2:
            outputs.append({"item": ".".join(split_list[-2:])})
            
    phantom.debug(f'outputs:  {json.dumps(outputs, indent=4)}')
        

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def list_fixup_domain_names_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("list_fixup_domain_names_4() called")

    list_merge_3__result = phantom.collect2(container=container, datapath=["list_merge_3:custom_function_result.data.item"])

    list_merge_3_data_item = [item[0] for item in list_merge_3__result]

    parameters = []

    parameters.append({
        "domain_list": list_merge_3_data_item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="phantom_pb_templates/list_fixup_domain_names", parameters=parameters, name="list_fixup_domain_names_4", callback=regex_filter_list_1)

    return


@phantom.playbook_block()
def code_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_5() called")

    list_merge_3__result = phantom.collect2(container=container, datapath=["list_merge_3:custom_function_result.data.item"])

    list_merge_3_data_item = [item[0] for item in list_merge_3__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'after merge:  {json.dumps(list_merge_3_data_item, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    list_fixup_domain_names_4(container=container)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    list_fixup_domain_names_4__result = phantom.collect2(container=container, datapath=["list_fixup_domain_names_4:custom_function_result.data.item"])

    list_fixup_domain_names_4_data_item = [item[0] for item in list_fixup_domain_names_4__result]

    input_parameter_0 = "fmglobal.com"

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    input_list = list_fixup_domain_names_4_data_item
    exclude = input_parameter_0
    
    outputs = []
    
    for item in input_list:
        if item and exclude.lower() not in item.lower():
            outputs.append({"item": item})
            
    phantom.debug(f'outputs:  {json.dumps(outputs, indent=4)}')


    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def regex_filter_list_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("regex_filter_list_1() called")

    list_fixup_domain_names_4__result = phantom.collect2(container=container, datapath=["list_fixup_domain_names_4:custom_function_result.data.item"])

    list_fixup_domain_names_4_data_item = [item[0] for item in list_fixup_domain_names_4__result]

    parameters = []

    parameters.append({
        "regex": "(?i)fmglobal\\.com",
        "action": "drop",
        "input_list": list_fixup_domain_names_4_data_item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/regex_filter_list", parameters=parameters, name="regex_filter_list_1", callback=code_2)

    return


@phantom.playbook_block()
def regex_filter_list_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("regex_filter_list_2() called")

    list_merge_5__result = phantom.collect2(container=container, datapath=["list_merge_5:custom_function_result.data.item"])
    format_1 = phantom.get_format_data(name="format_1")

    list_merge_5_data_item = [item[0] for item in list_merge_5__result]

    parameters = []

    parameters.append({
        "regex": format_1,
        "action": "drop",
        "input_list": list_merge_5_data_item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/regex_filter_list", parameters=parameters, name="regex_filter_list_2", callback=code_6)

    return


@phantom.playbook_block()
def code_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_6() called")

    regex_filter_list_2__result = phantom.collect2(container=container, datapath=["regex_filter_list_2:custom_function_result.data.item"])

    regex_filter_list_2_data_item = [item[0] for item in regex_filter_list_2__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'url list after filter:  {json.dumps(regex_filter_list_2_data_item, indent=4)}')
    
    assert json.dumps([])

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def list_merge_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("list_merge_5() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.requestURL","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "input_1": container_artifact_cef_item_0,
        "input_2": None,
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

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="list_merge_5", callback=code_7)

    return


@phantom.playbook_block()
def code_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_7() called")

    list_merge_5__result = phantom.collect2(container=container, datapath=["list_merge_5:custom_function_result.data.item"])

    list_merge_5_data_item = [item[0] for item in list_merge_5__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'after list_merge:  {json.dumps(list_merge_5_data_item, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    format_1(container=container)

    return


@phantom.playbook_block()
def code_8(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_8() called")

    list_merge_5__result = phantom.collect2(container=container, datapath=["list_merge_5:custom_function_result.data.item"])
    format_1 = phantom.get_format_data(name="format_1")

    list_merge_5_data_item = [item[0] for item in list_merge_5__result]

    input_parameter_0 = "drop"

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    import re
    
    #input_parameter_1 = "[^\s]*fmglobal.com[^\s]*"
    
    input_list = list_merge_5_data_item
    action = input_parameter_0
    regex = format_1

    # this only works on lists, so print a warning and return None if the input is not a list
    if not isinstance(input_list, list):
        raise ValueError('input_list is not a list')

    action = action.lower()
    if action not in ('keep', 'drop'):
        raise ValueError("action is not 'keep' or 'drop'")

    # iterate through the items in the list and append each non-falsy one as its own dictionary
    outputs = []
    for item in input_list:
        if item:
            phantom.debug(f're.match {str(regex)}, {str(item)}')
            if re.match(str(regex), str(item)):
                phantom.debug('match')
                if action == 'keep':
                    outputs.append({"item": item})
            else:
                phantom.debug('no match')
                if action == 'drop':
                    outputs.append({"item": item})
                    
    phantom.debug(f'outputs:  {json.dumps(outputs, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_1() called")

    template = """[^\\s]*fmglobal.com/.*|[^\\s]*fmglobal.com$"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    code_8(container=container)
    regex_filter_list_2(container=container)

    return


@phantom.playbook_block()
def incident_iocs_present_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("incident_iocs_present_6() called")

    parameters = []

    parameters.append({
        "input_1": None,
        "input_2": None,
        "input_3": None,
        "input_4": None,
        "input_5": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="phantom_pb_templates/incident_iocs_present", parameters=parameters, name="incident_iocs_present_6", callback=code_3)

    return


@phantom.playbook_block()
def code_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_3() called")

    incident_iocs_present_6__result = phantom.collect2(container=container, datapath=["incident_iocs_present_6:custom_function_result.data.present"])

    incident_iocs_present_6_data_present = [item[0] for item in incident_iocs_present_6__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'present:  {json.dumps(incident_iocs_present_6_data_present, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    decision_1(container=container)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["incident_iocs_present_6:custom_function_result.data.present", "!=", ""]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        code_9(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    code_10(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def code_9(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_9() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug('iocs_present is TRUE')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


@phantom.playbook_block()
def code_10(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_10() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug('iocs present is FALSE')

    ################################################################################
    ## Custom Code End
    ################################################################################

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