"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_get_user_email_1' block
    playbook_get_user_email_1(container=container)

    return

@phantom.playbook_block()
def ad_get_user_properties(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ad_get_user_properties() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    filtered_artifact_0_data_fl_user_email_event = phantom.collect2(container=container, datapath=["filtered-data:fl_user_email_event:condition_1:artifact:*.cef.user_email","filtered-data:fl_user_email_event:condition_1:artifact:*.id","filtered-data:fl_user_email_event:condition_1:artifact:*.external_id"], scope="all")

    parameters = []

    # build parameters list for 'ad_get_user_properties' call
    for filtered_artifact_0_item_fl_user_email_event in filtered_artifact_0_data_fl_user_email_event:
        parameters.append({
            "user_id": filtered_artifact_0_item_fl_user_email_event[0],
            "context": {'artifact_id': filtered_artifact_0_item_fl_user_email_event[1], 'artifact_external_id': filtered_artifact_0_item_fl_user_email_event[2]},
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("list user attributes", parameters=parameters, name="ad_get_user_properties", assets=["production ad graph"], callback=db_is_get_user_attributes_success)

    return


@phantom.playbook_block()
def db_check_user_email_exist(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("db_check_user_email_exist() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["artifact:*.cef.user_email", "!=", ""]
        ],
        scope="all",
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        fl_user_email_event(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    user_email_not_exist(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def user_email_not_exist(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("user_email_not_exist() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, note_format="markdown", note_type="general", title="User Email Doesn't Exist in the Incident")

    return


@phantom.playbook_block()
def mc_add_incident_note_user_details(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_add_incident_note_user_details() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    title_formatted_string = phantom.format(
        container=container,
        template="""User Details for {0}\n""",
        parameters=[
            "ad_get_user_properties:action_result.parameter.user_id"
        ])
    content_formatted_string = phantom.format(
        container=container,
        template="""{0}\n""",
        parameters=[
            "fb_incident_note_user_details:formatted_data"
        ])

    external_id_value = container.get("external_id", None)
    ad_get_user_properties_result_data = phantom.collect2(container=container, datapath=["ad_get_user_properties:action_result.parameter.user_id","ad_get_user_properties:action_result.parameter.context.artifact_id","ad_get_user_properties:action_result.parameter.context.artifact_external_id"], action_results=results, scope="all")
    fb_incident_note_user_details = phantom.get_format_data(name="fb_incident_note_user_details")

    parameters = []

    # build parameters list for 'mc_add_incident_note_user_details' call
    for ad_get_user_properties_result_item in ad_get_user_properties_result_data:
        if external_id_value is not None and title_formatted_string is not None and content_formatted_string is not None:
            parameters.append({
                "id": external_id_value,
                "title": title_formatted_string,
                "content": content_formatted_string,
                "context": {'artifact_id': ad_get_user_properties_result_item[1], 'artifact_external_id': ad_get_user_properties_result_item[2]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add incident note", parameters=parameters, name="mc_add_incident_note_user_details", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def fb_incident_note_user_details(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("fb_incident_note_user_details() called")

    template = """| Field                   | Value  |\n|-------------------------|--------|\n| Email:                  | {0}    |\n| Display Name:           | {1}    |\n| Department:             | {2}    |\n| Employee ID:            | {3}    |\n| User Type:              | {4}    |\n| Account Enabled:        | {5}    |\n| Job Title:              | {6}    |\n| Usage Location:         | {7}    |\n| Created DateTime:       | {8}    |\n| Last Direct Sync Time:  | {9}    |\n| Direct Sync Enabled:    | {10}   |\n| User Principal Name:    | {11}   |\n| Manager Name:           | {12}   |\n| Manager Email:          | {13}   |\n| User Office:            | {14}   |"""

    # parameter list for template variable replacement
    parameters = [
        "ad_get_user_properties:action_result.data.*.mail",
        "ad_get_user_properties:action_result.data.*.displayName",
        "ad_get_user_properties:action_result.data.*.department",
        "ad_get_user_properties:action_result.data.*.employeeId",
        "ad_get_user_properties:action_result.data.*.userType",
        "ad_get_user_properties:action_result.data.*.accountEnabled",
        "ad_get_user_properties:action_result.data.*.jobTitle",
        "ad_get_user_properties:action_result.data.*.usageLocation",
        "ad_get_user_properties:action_result.data.*.accountEnabled",
        "ad_get_user_properties:action_result.data.*.createdDateTime",
        "ad_get_user_properties:action_result.data.*.lastDirSyncTime",
        "ad_get_user_properties:action_result.data.*.dirSyncEnabled",
        "ad_get_manager_attributes:action_result.data.*.displayName",
        "ad_get_manager_attributes:action_result.data.*.mail",
        "ad_get_user_properties:action_result.data.*.physicalDeliveryOfficeName",
        "",
        ""
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="fb_incident_note_user_details", scope="all")

    mc_add_incident_note_user_details(container=container)

    return


@phantom.playbook_block()
def ad_get_manager_attributes(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ad_get_manager_attributes() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    user_id_formatted_string = phantom.format(
        container=container,
        template="""{0}/manager""",
        parameters=[
            "ad_get_user_properties:action_result.parameter.user_id"
        ])

    ad_get_user_properties_result_data = phantom.collect2(container=container, datapath=["ad_get_user_properties:action_result.parameter.user_id","ad_get_user_properties:action_result.parameter.context.artifact_id","ad_get_user_properties:action_result.parameter.context.artifact_external_id"], action_results=results, scope="all")

    parameters = []

    # build parameters list for 'ad_get_manager_attributes' call
    for ad_get_user_properties_result_item in ad_get_user_properties_result_data:
        parameters.append({
            "user_id": user_id_formatted_string,
            "context": {'artifact_id': ad_get_user_properties_result_item[1], 'artifact_external_id': ad_get_user_properties_result_item[2]},
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("list user attributes", parameters=parameters, name="ad_get_manager_attributes", assets=["production ad graph"], callback=ad_get_manager_attributes_callback)

    return


@phantom.playbook_block()
def ad_get_manager_attributes_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ad_get_manager_attributes_callback() called")

    
    fb_incident_note_user_details(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    create_mc_events_user_manager_information(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


@phantom.playbook_block()
def db_is_get_user_attributes_success(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("db_is_get_user_attributes_success() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["ad_get_user_properties:action_result.status", "==", "success"]
        ],
        scope="all",
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        ad_get_user_member_groups(action=action, success=success, container=container, results=results, handle=handle)
        ad_get_manager_attributes(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    mc_add_incident_note_get_user_details_failed(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def mc_add_incident_note_get_user_details_failed(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_add_incident_note_get_user_details_failed() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    content_formatted_string = phantom.format(
        container=container,
        template="""Failed to get the attributes of user: {0} from azure active directory\n\nMessage: {1}""",
        parameters=[
            "ad_get_user_properties:action_result.parameter.user_id",
            "ad_get_user_properties:action_result.message"
        ])

    external_id_value = container.get("external_id", None)
    ad_get_user_properties_result_data = phantom.collect2(container=container, datapath=["ad_get_user_properties:action_result.parameter.user_id","ad_get_user_properties:action_result.message","ad_get_user_properties:action_result.parameter.context.artifact_id","ad_get_user_properties:action_result.parameter.context.artifact_external_id"], action_results=results, scope="all")

    parameters = []

    # build parameters list for 'mc_add_incident_note_get_user_details_failed' call
    for ad_get_user_properties_result_item in ad_get_user_properties_result_data:
        if external_id_value is not None and content_formatted_string is not None:
            parameters.append({
                "id": external_id_value,
                "title": "Failed to Get User details from AD",
                "content": content_formatted_string,
                "context": {'artifact_id': ad_get_user_properties_result_item[2], 'artifact_external_id': ad_get_user_properties_result_item[3]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add incident note", parameters=parameters, name="mc_add_incident_note_get_user_details_failed", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def create_mc_events_user_manager_information(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("create_mc_events_user_manager_information() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    external_id_value = container.get("external_id", None)
    ad_get_user_properties_result_data = phantom.collect2(container=container, datapath=["ad_get_user_properties:action_result.data","ad_get_user_properties:action_result.parameter.user_id","ad_get_user_properties:action_result.parameter.context.artifact_id","ad_get_user_properties:action_result.parameter.context.artifact_external_id"], action_results=results, scope="all")

    parameters = []

    # build parameters list for 'create_mc_events_user_manager_information' call
    for ad_get_user_properties_result_item in ad_get_user_properties_result_data:
        if external_id_value is not None:
            parameters.append({
                "pairs": [
                    { "name": "user", "value": ad_get_user_properties_result_item[0] },
                    { "name": "manager", "value": ad_get_user_properties_result_item[1] },
                ],
                "incident_id": external_id_value,
                "context": {'artifact_id': ad_get_user_properties_result_item[2], 'artifact_external_id': ad_get_user_properties_result_item[3]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("create events", parameters=parameters, name="create_mc_events_user_manager_information", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def playbook_get_user_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_get_user_email_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Get User Email", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Get User Email", container=container, name="playbook_get_user_email_1", callback=db_check_user_email_exist, inputs=inputs)

    return


@phantom.playbook_block()
def ad_get_user_member_groups(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ad_get_user_member_groups() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    user_id_formatted_string = phantom.format(
        container=container,
        template="""{0}/memberOf""",
        parameters=[
            "ad_get_user_properties:action_result.parameter.user_id"
        ])

    ad_get_user_properties_result_data = phantom.collect2(container=container, datapath=["ad_get_user_properties:action_result.parameter.user_id","ad_get_user_properties:action_result.parameter.context.artifact_id","ad_get_user_properties:action_result.parameter.context.artifact_external_id"], action_results=results, scope="all")

    parameters = []

    # build parameters list for 'ad_get_user_member_groups' call
    for ad_get_user_properties_result_item in ad_get_user_properties_result_data:
        parameters.append({
            "user_id": user_id_formatted_string,
            "context": {'artifact_id': ad_get_user_properties_result_item[1], 'artifact_external_id': ad_get_user_properties_result_item[2]},
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("list user attributes", parameters=parameters, name="ad_get_user_member_groups", assets=["production ad graph"], callback=mc_add_incident_note_user_groups)

    return


@phantom.playbook_block()
def mc_add_incident_note_user_groups(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("mc_add_incident_note_user_groups() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    title_formatted_string = phantom.format(
        container=container,
        template="""User Groups for {0}""",
        parameters=[
            "ad_get_user_properties:action_result.parameter.user_id"
        ])
    content_formatted_string = phantom.format(
        container=container,
        template="""{0}""",
        parameters=[
            "ad_get_user_member_groups:action_result.data.*.displayName"
        ])

    external_id_value = container.get("external_id", None)
    ad_get_user_properties_result_data = phantom.collect2(container=container, datapath=["ad_get_user_properties:action_result.parameter.user_id","ad_get_user_properties:action_result.parameter.context.artifact_id","ad_get_user_properties:action_result.parameter.context.artifact_external_id"], action_results=results, scope="all")
    ad_get_user_member_groups_result_data = phantom.collect2(container=container, datapath=["ad_get_user_member_groups:action_result.data.*.displayName","ad_get_user_member_groups:action_result.parameter.context.artifact_id","ad_get_user_member_groups:action_result.parameter.context.artifact_external_id"], action_results=results, scope="all")

    parameters = []

    # build parameters list for 'mc_add_incident_note_user_groups' call
    for ad_get_user_properties_result_item in ad_get_user_properties_result_data:
        for ad_get_user_member_groups_result_item in ad_get_user_member_groups_result_data:
            if external_id_value is not None and title_formatted_string is not None and content_formatted_string is not None:
                parameters.append({
                    "id": external_id_value,
                    "title": title_formatted_string,
                    "content": content_formatted_string,
                    "context": {'artifact_id': ad_get_user_member_groups_result_item[1], 'artifact_external_id': ad_get_user_member_groups_result_item[2]},
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add incident note", parameters=parameters, name="mc_add_incident_note_user_groups", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def fl_user_email_event(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("fl_user_email_event() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.cef.user_email", "!=", ""]
        ],
        name="fl_user_email_event:condition_1",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        ad_get_user_properties(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

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