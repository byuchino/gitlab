"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'csv_string_to_output_2' block
    csv_string_to_output_2(container=container)

    return

def csv_string_to_output_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("csv_string_to_output_2() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.threats","artifact:*.id"])

    parameters = []

    # build parameters list for 'csv_string_to_output_2' call
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

    phantom.custom_function(custom_function="phantom_pb_templates/csv_string_to_output", parameters=parameters, name="csv_string_to_output_2", callback=remove_none)

    return


def remove_none(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("remove_none() called")

    csv_string_to_output_2_data = phantom.collect2(container=container, datapath=["csv_string_to_output_2:custom_function_result.data.*.output_item"])

    csv_string_to_output_2_data___output_item = [item[0] for item in csv_string_to_output_2_data]

    parameters = []

    parameters.append({
        "input_1": csv_string_to_output_2_data___output_item,
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

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="remove_none", callback=url_parse_5)

    return


def create_artifacts_from_threats(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_artifacts_from_threats() called")

    id_value = container.get("id", None)
    remove_none_data = phantom.collect2(container=container, datapath=["remove_none:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'create_artifacts_from_threats' call
    for remove_none_data_item in remove_none_data:
        parameters.append({
            "name": "threatUrl",
            "tags": None,
            "label": "artifact",
            "severity": None,
            "cef_field": "threatUrl",
            "cef_value": remove_none_data_item[0],
            "container": id_value,
            "input_json": None,
            "cef_data_type": "network",
            "run_automation": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="create_artifacts_from_threats")

    return


def url_parse_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("url_parse_5() called")

    remove_none_data = phantom.collect2(container=container, datapath=["remove_none:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'url_parse_5' call
    for remove_none_data_item in remove_none_data:
        parameters.append({
            "input_url": remove_none_data_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/url_parse", parameters=parameters, name="url_parse_5", callback=url_parse_5_callback)

    return


def url_parse_5_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("url_parse_5_callback() called")

    
    list_deduplicate_8(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    after_url_parse(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


def after_list_deduplicate(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("after_list_deduplicate() called")

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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="after_list_deduplicate")

    return


def artifact_create_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("artifact_create_7() called")

    id_value = container.get("id", None)
    list_deduplicate_8_data = phantom.collect2(container=container, datapath=["list_deduplicate_8:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'artifact_create_7' call
    for list_deduplicate_8_data_item in list_deduplicate_8_data:
        parameters.append({
            "name": "threatUrl Domain",
            "tags": None,
            "label": "artifact",
            "severity": None,
            "cef_field": "destinationDnsDomain",
            "cef_value": list_deduplicate_8_data_item[0],
            "container": id_value,
            "input_json": None,
            "cef_data_type": "Network",
            "run_automation": None,
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

    url_parse_5__result = phantom.collect2(container=container, datapath=["url_parse_5:custom_function_result.data.netloc"])

    url_parse_5_data_netloc = [item[0] for item in url_parse_5__result]

    parameters = []

    parameters.append({
        "input_list": url_parse_5_data_netloc,
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

    
    after_list_deduplicate(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    list_drop_none_11(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


def after_url_parse(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("after_url_parse() called")

    url_parse_5__result = phantom.collect2(container=container, datapath=["url_parse_5:custom_function_result.data.scheme","url_parse_5:custom_function_result.data.netloc","url_parse_5:custom_function_result.data.path","url_parse_5:custom_function_result.data.params","url_parse_5:custom_function_result.data.query","url_parse_5:custom_function_result.data.fragment","url_parse_5:custom_function_result.data.output_url"])

    url_parse_5_data_scheme = [item[0] for item in url_parse_5__result]
    url_parse_5_data_netloc = [item[1] for item in url_parse_5__result]
    url_parse_5_data_path = [item[2] for item in url_parse_5__result]
    url_parse_5_data_params = [item[3] for item in url_parse_5__result]
    url_parse_5_data_query = [item[4] for item in url_parse_5__result]
    url_parse_5_data_fragment = [item[5] for item in url_parse_5__result]
    url_parse_5_data_output_url = [item[6] for item in url_parse_5__result]

    parameters = []

    parameters.append({
        "input_1": url_parse_5_data_scheme,
        "input_2": url_parse_5_data_netloc,
        "input_3": url_parse_5_data_path,
        "input_4": url_parse_5_data_params,
        "input_5": url_parse_5_data_query,
        "input_6": url_parse_5_data_fragment,
        "input_7": url_parse_5_data_output_url,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="after_url_parse")

    return


def code_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_4() called")

    url_parse_5__result = phantom.collect2(container=container, datapath=["url_parse_5:custom_function_result.data.netloc"])

    url_parse_5_data_netloc = [item[0] for item in url_parse_5__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'netloc:  {json.dumps(url_parse_5_data_netloc, indent=4)}')
    
    url_doms = url_parse_5_data_netloc
    
    for dom in url_doms:
        phantom.debug('.'.join(dom.split('.')[-2:]))
        

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def list_drop_none_11(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("list_drop_none_11() called")

    list_deduplicate_8_data = phantom.collect2(container=container, datapath=["list_deduplicate_8:custom_function_result.data.*.item"])

    list_deduplicate_8_data___item = [item[0] for item in list_deduplicate_8_data]

    parameters = []

    parameters.append({
        "input_list": list_deduplicate_8_data___item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_drop_none", parameters=parameters, name="list_drop_none_11", callback=after_drop_none)

    return


def after_drop_none(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("after_drop_none() called")

    list_drop_none_11_data = phantom.collect2(container=container, datapath=["list_drop_none_11:custom_function_result.data.*.item"])

    list_drop_none_11_data___item = [item[0] for item in list_drop_none_11_data]

    parameters = []

    parameters.append({
        "input_1": list_drop_none_11_data___item,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="after_drop_none")

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