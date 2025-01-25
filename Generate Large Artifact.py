"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'code_1' block
    code_1(container=container)

    return

@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    code_1__largestring = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    code_1__largestring = "Hello World! " * 100000
    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="code_1:largestring", value=json.dumps(code_1__largestring))

    artifact_create_1(container=container)

    return


@phantom.playbook_block()
def artifact_create_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_create_1() called")

    id_value = container.get("id", None)
    code_1__largestring = json.loads(_ if (_ := phantom.get_run_data(key="code_1:largestring")) != "" else "null")  # pylint: disable=used-before-assignment

    parameters = []

    parameters.append({
        "container": id_value,
        "name": "Large Art",
        "label": None,
        "severity": None,
        "cef_field": "largeString",
        "cef_value": code_1__largestring,
        "cef_data_type": None,
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

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_1", callback=code_2)

    return


@phantom.playbook_block()
def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_2() called")

    code_2__largelist = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    code_2__largelist = list(range(1, 1000001))

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="code_2:largelist", value=json.dumps(code_2__largelist))

    artifact_create_2(container=container)

    return


@phantom.playbook_block()
def artifact_create_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_create_2() called")

    id_value = container.get("id", None)
    code_2__largelist = json.loads(_ if (_ := phantom.get_run_data(key="code_2:largelist")) != "" else "null")  # pylint: disable=used-before-assignment

    parameters = []

    parameters.append({
        "container": id_value,
        "name": "Large Art 2",
        "label": None,
        "severity": None,
        "cef_field": "largeList",
        "cef_value": code_2__largelist,
        "cef_data_type": None,
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

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_2")

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