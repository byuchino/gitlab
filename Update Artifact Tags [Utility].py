"""
Utility playbook to modify the tags for artifacts specified by ID.\nSupported operations are tag removal and tag addition.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'modify_artifact_tags' block
    modify_artifact_tags(container=container)

    return

@phantom.playbook_block()
def modify_artifact_tags(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("modify_artifact_tags() called")

    ################################################################################
    # Modifies the tags for passed artifact IDs.
    # First parameter is the artifact id list
    # Second parameter is the operation to be performed, in the following form:
    # <oper> = <tag>
    # where:
    #  <oper> is either "tag_to_remove" or "tag_to_add", and
    # <tag> is the tag either remove or add
    # The second parameter is also a list and so multiple operations may be specified
    ################################################################################

    playbook_input_artifact_id = phantom.collect2(container=container, datapath=["playbook_input:artifact_id"])
    playbook_input_artifact_op = phantom.collect2(container=container, datapath=["playbook_input:artifact_op"])

    playbook_input_artifact_id_values = [item[0] for item in playbook_input_artifact_id]
    playbook_input_artifact_op_values = [item[0] for item in playbook_input_artifact_op]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for art_id in playbook_input_artifact_id_values:
        phantom.debug(f'artifact id:  {art_id}')
        total_url = phantom.build_phantom_rest_url('artifact', str(art_id))

        response  = phantom.requests.get(total_url, verify=False)

        if response.status_code == 200:
            art_json = response.json()
            tags     = art_json['tags']
            phantom.debug(f'tags before:  {tags}')
            for op_request in playbook_input_artifact_op_values:
                art_oper = str(op_request).split("=")[0].lstrip().rstrip()
                art_tag  = str(op_request).split("=")[1].lstrip().rstrip()
                if "remove" in art_oper:
                    if art_tag in tags:
                        tags.remove(art_tag)
                elif "add" in art_oper:
                    if art_tag not in tags:
                        tags.append(art_tag)
            phantom.debug(f'tags after:  {tags}')
        else:
            phantom.error(response.text)

        response  = phantom.requests.post(total_url, json=art_json, verify=False)

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