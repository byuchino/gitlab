"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'get_data_2' block
    get_data_2(container=container)

    return

@phantom.playbook_block()
def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("run_query_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "query": "index=_internal | head 1",
        "command": "search",
        "display": "source",
        "parse_only": False,
        "search_mode": "smart",
        "attach_result": False,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("run query", parameters=parameters, name="run_query_1", assets=["splunk_dev_asset"])

    return


@phantom.playbook_block()
def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("get_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "location": "/services/authentication/users/testuser1",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_data_1", assets=["http to splunk 138"], callback=code_1)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    get_data_1_result_data = phantom.collect2(container=container, datapath=["get_data_1:action_result.data.*.parsed_response_body"], action_results=results)

    get_data_1_result_item_0 = [item[0] for item in get_data_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    prb = get_data_1_result_item_0[0]
    phantom.debug(f'parsed response body:  {json.dumps(prb, indent=4)}')
    
    propslist = prb.get("feed",{}).get("entry",{}).get("content",{}).get("s:dict",{}).get("s:key",[])
    
    roles = []
    for prop in propslist:
        if prop.get("@name","") == "roles":
            roles = prop.get("s:list",{}).get("s:item",[])
            break
            
    phantom.debug(f'roles:  {json.dumps(roles, indent=4)}')


    ################################################################################
    ## Custom Code End
    ################################################################################

    post_data_1(container=container)

    return


@phantom.playbook_block()
def post_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("post_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "body": "roles=user",
        "location": "/services/authentication/users/testuser1",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("post data", parameters=parameters, name="post_data_1", assets=["http to splunk 138"], callback=code_2)

    return


@phantom.playbook_block()
def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_2() called")

    post_data_1_result_data = phantom.collect2(container=container, datapath=["post_data_1:action_result.data.*.parsed_response_body"], action_results=results)

    post_data_1_result_item_0 = [item[0] for item in post_data_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    prb = post_data_1_result_item_0[0]
    #phantom.debug(f'parsed response body:  {json.dumps(prb, indent=4)}')
    
    propslist = prb.get("feed",{}).get("entry",{}).get("content",{}).get("s:dict",{}).get("s:key",[])
    
    roles = []
    for prop in propslist:
        if prop.get("@name","") == "roles":
            roles = prop.get("s:list",{}).get("s:item",[])
            break
            
    phantom.debug(f'roles:  {json.dumps(roles, indent=4)}')


    ################################################################################
    ## Custom Code End
    ################################################################################

    send_email_1(container=container)

    return


@phantom.playbook_block()
def send_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("send_email_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "to": "brian@10thframe.com",
        "body": "Did this work",
        "from": "playbook@frame10.com",
        "subject": "test email",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("send email", parameters=parameters, name="send_email_1", assets=["smtp"])

    return


@phantom.playbook_block()
def get_data_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("get_data_2() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "headers": "",
        "location": "/services/authentication/users?search=nobody",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_data_2", assets=["http to splunk 138"], callback=code_3)

    return


@phantom.playbook_block()
def code_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_3() called")

    get_data_2_result_data = phantom.collect2(container=container, datapath=["get_data_2:action_result.data.*.parsed_response_body"], action_results=results)

    get_data_2_result_item_0 = [item[0] for item in get_data_2_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    prb = get_data_2_result_item_0[0]
    phantom.debug(f'parsed response body:  {json.dumps(prb, indent=4)}')

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