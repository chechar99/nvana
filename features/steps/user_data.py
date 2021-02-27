import json

from behave import given, then, when

from src.script_sync import main


@given('we have the user Peter with member id "{member_id}"')
def step_impl(context, member_id):
    context.member_id = int(member_id)


@when('we request consolidated data')
def step_impl(context):
    context.result = main(context.member_id)


@then('we get this json data')
def step_impl(context):
    step_json = json.loads(context.text)
    assert step_json == context.result
