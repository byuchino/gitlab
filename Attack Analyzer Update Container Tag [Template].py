"""
Find all artifacts with tag, &quot;saa_pending&quot;.  If there are none, remove the CONTAINER tag, &quot;saa_pending&quot;.  Otherwise, add the CONTAINER tag, &quot;saa_pending&quot;
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'count_tags' block
    count_tags(container=container)

    return

@phantom.playbook_block()
def check_list_length(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("check_list_length() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["count_tags:custom_function:num_tags", "==", 0]
        ],
        scope="all",
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        code_3(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    code_1(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def code_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_3() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug('There are no pending artifacts')

    ################################################################################
    ## Custom Code End
    ################################################################################

    remove_tag_4(container=container)

    return


@phantom.playbook_block()
def remove_tag_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("remove_tag_4() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.remove_tags(container=container, tags="saa_pending")

    container = phantom.get_container(container.get('id', None))

    return


@phantom.playbook_block()
def count_tags(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("count_tags() called")

    input_parameter_0 = "saa_pending"

    count_tags__num_tags = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    check_tag = input_parameter_0
    
    id_value  = container.get("id", None)
    base_url  = phantom.build_phantom_rest_url('container')
    total_url = base_url + '/{0}/artifacts?_filter_tags__contains="{1}"'.format(str(id_value),check_tag)
    count     = 0
    
    response  = phantom.requests.get(total_url, verify=False)
    phantom.debug(f'response:  {json.dumps(response.json(), indent=4)}')
    
    if response.status_code == 200:
        count = response.json()['count']
    else:
        phantom.error(response.text)
    
    phantom.debug(f'There are {count} artifacts tagged {check_tag}')
    count_tags__num_tags = count
    
    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="count_tags:num_tags", value=json.dumps(count_tags__num_tags))

    check_list_length(container=container)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    count_tags__num_tags = json.loads(_ if (_ := phantom.get_run_data(key="count_tags:num_tags")) != "" else "null")  # pylint: disable=used-before-assignment

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'There are {count_tags__num_tags} pending artifacts')

    ################################################################################
    ## Custom Code End
    ################################################################################

    add_tag_1(container=container)

    return


@phantom.playbook_block()
def add_tag_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_tag_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_tags(container=container, tags="saa_pending")

    container = phantom.get_container(container.get('id', None))

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