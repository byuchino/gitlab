"""
This playbook gets all notes from the current container, updates the SNOW ticket with those notes and then close the current container.
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'FB_REST_Notes_This_Container' block
    FB_REST_Notes_This_Container(container=container)

    return

def FB_REST_Notes_This_Container(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('FB_REST_Notes_This_Container() called')
    
    template = """/container_note?_filter_container_id={0}"""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="FB_REST_Notes_This_Container")

    HTTP_REST_Get_Container_Notes(container=container)

    return

def HTTP_REST_Get_Container_Notes(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('HTTP_REST_Get_Container_Notes() called')

    # collect data for 'HTTP_REST_Get_Container_Notes' call
    formatted_data_1 = phantom.get_format_data(name='FB_REST_Notes_This_Container')

    parameters = []
    
    # build parameters list for 'HTTP_REST_Get_Container_Notes' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=FL_Non_Null_Notes, name="HTTP_REST_Get_Container_Notes")

    return

def FL_Non_Null_Notes(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('FL_Non_Null_Notes() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["HTTP_REST_Get_Container_Notes:action_result.data.*.response_body.data.*.title", "!=", ""],
            ["HTTP_REST_Get_Container_Notes:action_result.data.*.response_body.data.*.content", "!=", ""],
        ],
        logical_operator='and',
        name="FL_Non_Null_Notes:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        FB_Container_Notes(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def FB_Container_Notes(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('FB_Container_Notes() called')
    
    template = """%%
{0}
{1}
=====================================
%%"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:FL_Non_Null_Notes:condition_1:HTTP_REST_Get_Container_Notes:action_result.data.*.response_body.data.*.title",
        "filtered-data:FL_Non_Null_Notes:condition_1:HTTP_REST_Get_Container_Notes:action_result.data.*.response_body.data.*.content",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="FB_Container_Notes")

    cf_General_PB_Custom_Functions_Just_Print_1(container=container)

    return

def cf_General_PB_Custom_Functions_Just_Print_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('cf_General_PB_Custom_Functions_Just_Print_1() called')
    
    formatted_data_0 = [
        [
            phantom.get_format_data(name="FB_Container_Notes"),
        ],
    ]

    parameters = []

    formatted_data_0_0 = [item[0] for item in formatted_data_0]

    parameters.append({
        'whatever_list2': formatted_data_0_0,
        'whatever_list3': None,
        'whatever_list4': None,
        'whatever_list5': None,
        'whatever_list6': None,
        'whatever_list7': None,
        'whatever_list8': None,
    })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "General_PB_Custom_Functions/Just_Print", returns the custom_function_run_id
    phantom.custom_function(custom_function='General_PB_Custom_Functions/Just_Print', parameters=parameters, name='cf_General_PB_Custom_Functions_Just_Print_1')

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return