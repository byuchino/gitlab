"""
Parent playbook that gets triggered as and when there is a new email ingested from the mailbox into SOAR. This playbook calls every other playbook in this use case.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_exclude_unwanted_iocs_1' block
    playbook_exclude_unwanted_iocs_1(container=container)
    # call 'playbook_mark_internal_iocs_1' block
    playbook_mark_internal_iocs_1(container=container)
    # call 'playbook_mark_public_ip_artifacts_1' block
    playbook_mark_public_ip_artifacts_1(container=container)
    # call 'playbook_mark_the_phishing_email_artifact_1' block
    playbook_mark_the_phishing_email_artifact_1(container=container)
    # call 'playbook_extract_email_data_1' block
    playbook_extract_email_data_1(container=container)

    return

@phantom.playbook_block()
def playbook_exclude_unwanted_iocs_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_exclude_unwanted_iocs_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Exclude Unwanted IOCs", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Exclude Unwanted IOCs", container=container, name="playbook_exclude_unwanted_iocs_1", callback=join_playbook_add_benign_tag_to_all_artifacts_1, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_mark_internal_iocs_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_mark_internal_iocs_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Mark Internal IOCs", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Mark Internal IOCs", container=container, name="playbook_mark_internal_iocs_1", callback=join_playbook_add_benign_tag_to_all_artifacts_1, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_mark_public_ip_artifacts_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_mark_public_ip_artifacts_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Mark Public IP artifacts", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Mark Public IP artifacts", container=container, name="playbook_mark_public_ip_artifacts_1", callback=join_playbook_add_benign_tag_to_all_artifacts_1, inputs=inputs)

    return


@phantom.playbook_block()
def join_playbook_add_benign_tag_to_all_artifacts_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("join_playbook_add_benign_tag_to_all_artifacts_1() called")

    if phantom.completed(playbook_names=["playbook_exclude_unwanted_iocs_1", "playbook_mark_internal_iocs_1", "playbook_mark_public_ip_artifacts_1", "playbook_mark_the_phishing_email_artifact_1", "playbook_extract_email_data_1"]):
        # call connected block "playbook_add_benign_tag_to_all_artifacts_1"
        playbook_add_benign_tag_to_all_artifacts_1(container=container, handle=handle)

    return


@phantom.playbook_block()
def playbook_add_benign_tag_to_all_artifacts_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_add_benign_tag_to_all_artifacts_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Add Benign Tag to all Artifacts", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Add Benign Tag to all Artifacts", container=container, name="playbook_add_benign_tag_to_all_artifacts_1", callback=playbook_add_benign_tag_to_all_artifacts_1_callback, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_add_benign_tag_to_all_artifacts_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_add_benign_tag_to_all_artifacts_1_callback() called")

    
    playbook_vt___urlscan___phishtank___investigate_url_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    playbook_vt___investigate_filehash_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    playbook_urlscan___vt___investigate_domains_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    playbook_urlscan___vt___investigate_ip_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    playbook_get_user_attributes_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


@phantom.playbook_block()
def playbook_vt___urlscan___phishtank___investigate_url_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_vt___urlscan___phishtank___investigate_url_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/VT - URLscan - PhishTank - Investigate URL", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/VT - URLscan - PhishTank - Investigate URL", container=container, name="playbook_vt___urlscan___phishtank___investigate_url_1", callback=join_db_is_artifact_malicious, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_vt___investigate_filehash_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_vt___investigate_filehash_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/VT - Investigate FileHash", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/VT - Investigate FileHash", container=container, name="playbook_vt___investigate_filehash_1", callback=join_db_is_artifact_malicious, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_urlscan___vt___investigate_domains_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_urlscan___vt___investigate_domains_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/URLscan - VT - Investigate Domains", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/URLscan - VT - Investigate Domains", container=container, name="playbook_urlscan___vt___investigate_domains_1", callback=join_db_is_artifact_malicious, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_urlscan___vt___investigate_ip_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_urlscan___vt___investigate_ip_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/URLscan - VT - Investigate IP", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/URLscan - VT - Investigate IP", container=container, name="playbook_urlscan___vt___investigate_ip_1", callback=join_db_is_artifact_malicious, inputs=inputs)

    return


@phantom.playbook_block()
def join_db_is_artifact_malicious(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("join_db_is_artifact_malicious() called")

    if phantom.completed(playbook_names=["playbook_vt___urlscan___phishtank___investigate_url_1", "playbook_vt___investigate_filehash_1", "playbook_urlscan___vt___investigate_domains_1", "playbook_urlscan___vt___investigate_ip_1", "playbook_get_user_attributes_1"]):
        # call connected block "db_is_artifact_malicious"
        db_is_artifact_malicious(container=container, handle=handle)

    return


@phantom.playbook_block()
def db_is_artifact_malicious(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("db_is_artifact_malicious() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["malicious", "in", "artifact:*.tags"]
        ])

    # call connected blocks if condition 1 matched
    if found_match_1:
        api_tag_malicious(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    api_tag_benign(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def playbook_push_results_back_to_splunk_es_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_push_results_back_to_splunk_es_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Push Results back to Splunk ES", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Push Results back to Splunk ES", container=container, name="playbook_push_results_back_to_splunk_es_1", callback=playbook_push_results_back_to_splunk_es_1_callback, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_push_results_back_to_splunk_es_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_push_results_back_to_splunk_es_1_callback() called")

    
    # Downstream End block cannot be called directly, since execution will call on_finish automatically.
    # Using placeholder callback function so child playbook is run synchronously.


    return


@phantom.playbook_block()
def playbook_get_user_attributes_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_get_user_attributes_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Get User Attributes", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Get User Attributes", container=container, name="playbook_get_user_attributes_1", callback=join_db_is_artifact_malicious, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_mark_the_phishing_email_artifact_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_mark_the_phishing_email_artifact_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Mark the Phishing Email Artifact", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Mark the Phishing Email Artifact", container=container, name="playbook_mark_the_phishing_email_artifact_1", callback=join_playbook_add_benign_tag_to_all_artifacts_1, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_extract_email_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_extract_email_data_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Extract Email Data", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Extract Email Data", container=container, name="playbook_extract_email_data_1", callback=join_playbook_add_benign_tag_to_all_artifacts_1, inputs=inputs)

    return


@phantom.playbook_block()
def api_tag_benign(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("api_tag_benign() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_tags(container=container, tags="benign")

    container = phantom.get_container(container.get('id', None))

    return


@phantom.playbook_block()
def api_tag_malicious(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("api_tag_malicious() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_tags(container=container, tags="malicious")

    container = phantom.get_container(container.get('id', None))

    playbook_push_results_back_to_splunk_es_1(container=container)

    return


@phantom.playbook_block()
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