"""
Retrieves all notes from container using REST, then builds and sends an email body with the notes as the content.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'format_1' block
    format_1(container=container)

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_1() called")

    template = """/container_note?_filter_container_id={0}\n"""

    # parameter list for template variable replacement
    parameters = [
        "container:id"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    get_container_notes(container=container)

    return


def get_container_notes(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_container_notes() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_1 = phantom.get_format_data(name="format_1")

    parameters = []

    if format_1 is not None:
        parameters.append({
            "location": format_1,
            "verify_certificate": False,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_container_notes", assets=["local rest"], callback=decision_3)

    return


def format_email_body(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_email_body() called")

    template = """Link to Container: {2}\n\n%%\n{0}\n{1}\n=====================================\n%%\n"""

    # parameter list for template variable replacement
    parameters = [
        "get_container_notes:action_result.data.*.response_body.data.*.title",
        "get_container_notes:action_result.data.*.response_body.data.*.content",
        "container:url"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_email_body")

    join_route_formatted_body(container=container)

    return


def send_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("send_email_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    subject_formatted_string = phantom.format(
        container=container,
        template="""ioc report - container id {0}\n""",
        parameters=[
            "container:id"
        ])

    get_email_recipients_data = phantom.collect2(container=container, datapath=["get_email_recipients:custom_function_result.data.*.column_0"])
    route_formatted_body__body = json.loads(phantom.get_run_data(key="route_formatted_body:body"))

    parameters = []

    # build parameters list for 'send_email_1' call
    for get_email_recipients_data_item in get_email_recipients_data:
        if get_email_recipients_data_item[0] is not None and route_formatted_body__body is not None:
            parameters.append({
                "to": get_email_recipients_data_item[0],
                "body": route_formatted_body__body,
                "from": "",
                "subject": subject_formatted_string,
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("send email", parameters=parameters, name="send_email_1", assets=["wpoven"])

    return


def get_email_recipients(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_email_recipients() called")

    parameters = []

    parameters.append({
        "custom_list": "bulk ioc recipient",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/custom_list_enumerate", parameters=parameters, name="get_email_recipients", callback=decision_1)

    return


def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["get_email_recipients:custom_function_result.data.*.column_0", "!=", ""]
        ])

    # call connected blocks if condition 1 matched
    if found_match_1:
        send_email_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    recipients_list_empty_comment(action=action, success=success, container=container, results=results, handle=handle)

    return


def build_container_link(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("build_container_link() called")

    build_container_link__link = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    id_value  = container.get("id", None)
    base_url  = phantom.build_phantom_rest_url('container')
    total_url = base_url + "/{0}".format(str(id_value))
    phantom.debug(f'container url:  {json.dumps(total_url, indent=4)}')
    code_9__link = total_url

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="build_container_link:link", value=json.dumps(build_container_link__link))

    return


def recipients_list_empty_comment(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("recipients_list_empty_comment() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="The recipients list is empty - check the custom list")

    return


def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_1() called")

    url_value = container.get("url", None)

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'container url:  {json.dumps(url_value, indent=4)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def decision_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_3() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        logical_operator="and",
        conditions=[
            ["get_container_notes:action_result.data.*.response_body.data.*.title", "!=", ""],
            ["get_container_notes:action_result.data.*.response_body.data.*.content", "!=", ""]
        ])

    # call connected blocks if condition 1 matched
    if found_match_1:
        format_email_body(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    format_email_no_content(action=action, success=success, container=container, results=results, handle=handle)

    return


def format_email_no_content(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_email_no_content() called")

    template = """Link to Container: {0}\n\nThere are no notes present in container {1}\n"""

    # parameter list for template variable replacement
    parameters = [
        "container:url",
        "container:id"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_email_no_content")

    join_route_formatted_body(container=container)

    return


def join_route_formatted_body(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("join_route_formatted_body() called")

    if phantom.completed(action_names=["get_container_notes"]):
        # call connected block "route_formatted_body"
        route_formatted_body(container=container, handle=handle)

    return


def route_formatted_body(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("route_formatted_body() called")

    format_email_body = phantom.get_format_data(name="format_email_body")
    format_email_no_content = phantom.get_format_data(name="format_email_no_content")

    route_formatted_body__body = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'Notes present: {json.dumps(format_email_body, indent=4)}')
    phantom.debug(f'No notes: {json.dumps(format_email_no_content, indent=4)}')
    
    route_formatted_body__body = format_email_body if format_email_body else format_email_no_content

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="route_formatted_body:body", value=json.dumps(route_formatted_body__body))

    get_email_recipients(container=container)

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