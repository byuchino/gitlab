"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'get_all_notes_8' block
    get_all_notes_8(container=container)

    return

def artifact_create_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("artifact_create_1() called")

    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "name": "threats",
        "tags": None,
        "label": None,
        "severity": None,
        "cef_field": "threatIds",
        "cef_value": "[\"88888888\", \"99999999\"]",
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

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_1")

    return


def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.threatIds"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    user_id = phantom.get_effective_user()
    phantom.debug(f'user_id:  {user_id}')
    phantom.debug(f'threatIds:  {json.dumps(container_artifact_cef_item_0, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_2() called")

    format_1 = phantom.get_format_data(name="format_1")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(format_1)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def ltos_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("ltos_2() called")

    passthrough_3_data = phantom.collect2(container=container, datapath=["passthrough_3:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'ltos_2' call
    for passthrough_3_data_item in passthrough_3_data:
        parameters.append({
            "input_list": passthrough_3_data_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug("LTOS CALLED")

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="phantom_pb_templates/ltos", parameters=parameters, name="ltos_2", callback=code_3)

    return


def code_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_3() called")

    ltos_2__result = phantom.collect2(container=container, datapath=["ltos_2:custom_function_result.data.output_string"])

    ltos_2_data_output_string = [item[0] for item in ltos_2__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'output_string:  {ltos_2_data_output_string}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("run_query_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "query": "|inputlookup abc",
        "command": "",
        "end_time": "now",
        "start_time": "-1m",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("run query", parameters=parameters, name="run_query_1", assets=["splunk50"])

    return


def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_1() called")

    template = """%%\nthreatID = \"{0}\"\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.threatIds"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    code_2(container=container)

    return


def code_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_4() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.threatIds"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    code_4__outlist = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    art1 = ["1.2.3.4","8.8.8.8"]
    art2 = ["192.168.254.57","192.168.1.17"]
    art3 = ["10.36.101.20","10.42.73.151"]
    
    #code_4__outlist = {"threatIds": [art1, art2, art3]}
    code_4__outlist = [art1, art2, art3]

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="code_4:outlist", value=json.dumps(code_4__outlist))

    code_5(container=container)

    return


def code_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_5() called")

    code_4__outlist = json.loads(phantom.get_run_data(key="code_4:outlist"))

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'outlist:  {json.dumps(code_4__outlist, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    passthrough_3(container=container)

    return


def passthrough_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("passthrough_3() called")

    code_4__outlist = json.loads(phantom.get_run_data(key="code_4:outlist"))

    parameters = []

    parameters.append({
        "input_1": code_4__outlist,
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

    phantom.custom_function(custom_function="community/passthrough", parameters=parameters, name="passthrough_3", callback=mv2list_6)

    return


def code_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_6() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug("check json")
    #i = ['44444444', '88888888']
    #i = "[44444444, 88888888]"
    i = "44444444, 88888888"

    try:
        l = json.loads(i)
        phantom.debug("valid json string")
    except:
        phantom.debug("exception")
        l = i
        
    phantom.debug(f"input type is {type(l)}")
    phantom.debug(f"input is {json.dumps(l, indent=4)}")
    
    if isinstance(l, list):
        s = ",".join(str(x) for x in l)
        phantom.debug(f"after conversion: {s}")
        phantom.debug(f"type is {type(s)}")
    else:
        phantom.debug("input is not convertible")
    
    
    '''    
    if isinstance(l, list):
        phantom.debug(f"type is {type(l)}")
        s = ",".join(l)
        phantom.debug(f"after conversion: {s}")
        phantom.debug(f"type is {type(s)}")
    else:
        try:
            json.loads(l)
            phantom.debug("valid json")
        except:
            phantom.debug("invalid json")
    '''

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def code_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_7() called")

    code_7__outlist = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    art1 = {"cn": "User One", "email": "userone@nowhere.com" }
    art2 = {"cn": "User Two", "email": "usertwo@nowhere.com" }
    art3 = {"cn": "User Three", "email": "userthree@nowhere.com" }
    
    l1 = [art1, art2, art3]
    l2 = [l1]
    
    #code_4__outlist = {"threatIds": [art1, art2, art3]}
    code_7__outlist = [l2]


    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="code_7:outlist", value=json.dumps(code_7__outlist))

    passthrough_4(container=container)

    return


def code_8(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_8() called")

    code_7__outlist = json.loads(phantom.get_run_data(key="code_7:outlist"))

    code_8__output = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'sim response:  {json.dumps(code_7__outlist, indent=4)}')
    
    
    l2 = code_7__outlist[0]
    l3 = l2[0]
    
    for item in l3:
        phantom.debug(f'item:  {json.dumps(item, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="code_8:output", value=json.dumps(code_8__output))

    return


def passthrough_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("passthrough_4() called")

    code_7__outlist = json.loads(phantom.get_run_data(key="code_7:outlist"))

    parameters = []

    parameters.append({
        "input_1": code_7__outlist,
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

    phantom.custom_function(custom_function="community/passthrough", parameters=parameters, name="passthrough_4", callback=coalesce_search_results_5)

    return


def coalesce_search_results_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("coalesce_search_results_5() called")

    passthrough_4_data = phantom.collect2(container=container, datapath=["passthrough_4:custom_function_result.data.*.item"])

    passthrough_4_data___item = [item[0] for item in passthrough_4_data]

    parameters = []

    parameters.append({
        "result_data": passthrough_4_data___item,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="phantom_pb_templates/coalesce_search_results", parameters=parameters, name="coalesce_search_results_5", callback=format_2)

    return


def code_9(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_9() called")

    format_2 = phantom.get_format_data(name="format_2")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    #phantom.debug(f'after coalesce:  {json.dumps(coalesce_search_results_5_data_items, indent=4)}')
    phantom.debug(f'format:  {format_2}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_2() called")

    template = """%%\nEmail {0}\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "coalesce_search_results_5:custom_function_result.data.items.*.item.email"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_2")

    code_9(container=container)

    return


def mv2list_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("mv2list_6() called")

    passthrough_3_data = phantom.collect2(container=container, datapath=["passthrough_3:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'mv2list_6' call
    for passthrough_3_data_item in passthrough_3_data:
        parameters.append({
            "mvfield": passthrough_3_data_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="phantom_pb_templates/mv2list", parameters=parameters, name="mv2list_6", callback=mv2list_6_callback)

    return


def mv2list_6_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("mv2list_6_callback() called")

    
    debug_7(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    format_3(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


def format_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_3() called")

    template = """%%\n{0}\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "mv2list_6:custom_function_result.data.outlist"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_3")

    ip_reputation_1(container=container)

    return


def ip_reputation_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("ip_reputation_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_3__as_list = phantom.get_format_data(name="format_3__as_list")

    parameters = []

    # build parameters list for 'ip_reputation_1' call
    for format_3__item in format_3__as_list:
        if format_3__item is not None:
            parameters.append({
                "ip": format_3__item,
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("ip reputation", parameters=parameters, name="ip_reputation_1", assets=["vtotalv2"])

    return


def debug_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_7() called")

    mv2list_6__result = phantom.collect2(container=container, datapath=["mv2list_6:custom_function_result.data.outlist"])

    mv2list_6_data_outlist = [item[0] for item in mv2list_6__result]

    parameters = []

    parameters.append({
        "input_1": mv2list_6_data_outlist,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_7")

    return


def get_all_notes_8(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_all_notes_8() called")

    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "container": id_value,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="phantom_pb_templates/get_all_notes", parameters=parameters, name="get_all_notes_8", callback=get_all_notes_8_callback)

    return


def get_all_notes_8_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_all_notes_8_callback() called")

    
    code_10(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    format_4(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


def code_10(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_10() called")

    get_all_notes_8__result = phantom.collect2(container=container, datapath=["get_all_notes_8:custom_function_result.data.items"])

    get_all_notes_8_data_items = [item[0] for item in get_all_notes_8__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'Notes:  {json.dumps(get_all_notes_8_data_items, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def format_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_4() called")

    template = """%%\n{0}\n{1}\n=====================================\n%%\n"""

    # parameter list for template variable replacement
    parameters = [
        "get_all_notes_8:custom_function_result.data.items.*.item.title",
        "get_all_notes_8:custom_function_result.data.items.*.item.content"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_4")

    code_11(container=container)

    return


def code_11(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_11() called")

    format_4 = phantom.get_format_data(name="format_4")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(format_4)

    ################################################################################
    ## Custom Code End
    ################################################################################

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