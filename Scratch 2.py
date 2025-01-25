"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'parse_out_sender_emails' block
    parse_out_sender_emails(container=container)

    return

def playbook_case_test_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_case_test_1() called")

    inputs = {
        "promotion_reason": "just because",
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "phantom_pb_templates/Case test", returns the playbook_run_id
    playbook_run_id = phantom.playbook("phantom_pb_templates/Case test", container=container, inputs=inputs)

    return


def container_update_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("container_update_1() called")

    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "name": "Updated Container",
        "tags": None,
        "label": None,
        "owner": None,
        "status": None,
        "severity": None,
        "input_json": "{\"custom_fields\": {\"field1\": 1, \"field2\": 2}}",
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

    phantom.custom_function(custom_function="community/container_update", parameters=parameters, name="container_update_1", callback=code_3)

    return


def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_2() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'container:  {json.dumps(container, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    container_update_1(container=container)

    return


def code_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_3() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'container:  {json.dumps(container, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def parse_out_sender_emails(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("parse_out_sender_emails() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.senders","artifact:*.id"])

    parameters = []

    # build parameters list for 'parse_out_sender_emails' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "convert_list_input": container_artifact_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="phantom_pb_templates/csv_string_to_output", parameters=parameters, name="parse_out_sender_emails", callback=remove_null_emails)

    return


def remove_null_emails(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("remove_null_emails() called")

    parse_out_sender_emails_data = phantom.collect2(container=container, datapath=["parse_out_sender_emails:custom_function_result.data.*.output_item"])

    parse_out_sender_emails_data___output_item = [item[0] for item in parse_out_sender_emails_data]

    parameters = []

    parameters.append({
        "input_1": parse_out_sender_emails_data___output_item,
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

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="remove_null_emails", callback=remove_null_emails_callback)

    return


def remove_null_emails_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("remove_null_emails_callback() called")

    
    create_senderemailaddress_artifacts(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    regex_extract_email_5(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


def create_senderemailaddress_artifacts(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_senderemailaddress_artifacts() called")

    id_value = container.get("id", None)
    remove_null_emails_data = phantom.collect2(container=container, datapath=["remove_null_emails:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'create_senderemailaddress_artifacts' call
    for remove_null_emails_data_item in remove_null_emails_data:
        parameters.append({
            "container": id_value,
            "name": "senderEmailAddress",
            "label": "artifact",
            "severity": None,
            "cef_field": "senderEmailAddress",
            "cef_value": remove_null_emails_data_item[0],
            "cef_data_type": "email",
            "tags": None,
            "run_automation": None,
            "input_json": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="create_senderemailaddress_artifacts", callback=rename_event_with_sender)

    return


def rename_event_with_sender(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("rename_event_with_sender() called")

    ################################################################################
    # This uses the sender and renames the event to:
    # 
    # PP Message Delivered: Possible Phish from: <SENDER>
    ################################################################################

    remove_null_emails_data = phantom.collect2(container=container, datapath=["remove_null_emails:custom_function_result.data.*.item"])

    remove_null_emails_data___item = [item[0] for item in remove_null_emails_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    label=container.get('label')
    
    EMAIL_EVENT_TEMPLATE="PP Message Delivered: Possible Phish from: {0}"
    TAP_CLICK_EVENT_TEMPLATE="PP TAP Click Alert. Sender: {0}"
    
    # Adjust our template for the case name based on the label type
    TEMPLATE = TAP_CLICK_EVENT_TEMPLATE if label == "tap_click_event_automation" else EMAIL_EVENT_TEMPLATE
    
    sender = remove_null_emails_data___item[0] if remove_null_emails_data___item and len(remove_null_emails_data___item) > 0 else "unknown"
    
    
    event_name = TEMPLATE.format(sender)
    
    update = {
        "name":event_name
    }
    
    success, message = phantom.update(container, update)
    
    if not success:
        phantom.error(f'Failed to update container name. Message Returned: {message}')
        

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def regex_extract_email_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("regex_extract_email_5() called")

    remove_null_emails_data = phantom.collect2(container=container, datapath=["remove_null_emails:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'regex_extract_email_5' call
    for remove_null_emails_data_item in remove_null_emails_data:
        parameters.append({
            "input_string": remove_null_emails_data_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/regex_extract_email", parameters=parameters, name="regex_extract_email_5", callback=list_deduplicate_8)

    return


def debug_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_6() called")

    list_deduplicate_8_data = phantom.collect2(container=container, datapath=["list_deduplicate_8:custom_function_result.data.*.item"])

    list_deduplicate_8_data___item = [item[0] for item in list_deduplicate_8_data]

    parameters = []

    parameters.append({
        "input_1": list_deduplicate_8_data___item,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_6")

    return


def artifact_create_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("artifact_create_7() called")

    id_value = container.get("id", None)
    list_deduplicate_8_data = phantom.collect2(container=container, datapath=["list_deduplicate_8:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'artifact_create_7' call
    for list_deduplicate_8_data_item in list_deduplicate_8_data:
        parameters.append({
            "container": id_value,
            "name": "senderEmailDomain",
            "label": "artifact",
            "severity": None,
            "cef_field": "destinationDnsDomain",
            "cef_value": list_deduplicate_8_data_item[0],
            "cef_data_type": "email",
            "tags": None,
            "run_automation": None,
            "input_json": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_7")

    return


def list_deduplicate_8(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("list_deduplicate_8() called")

    regex_extract_email_5_data = phantom.collect2(container=container, datapath=["regex_extract_email_5:custom_function_result.data.*.domain"])

    regex_extract_email_5_data___domain = [item[0] for item in regex_extract_email_5_data]

    parameters = []

    parameters.append({
        "input_list": regex_extract_email_5_data___domain,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_deduplicate", parameters=parameters, name="list_deduplicate_8", callback=list_deduplicate_8_callback)

    return


def list_deduplicate_8_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("list_deduplicate_8_callback() called")

    
    artifact_create_7(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    debug_6(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return