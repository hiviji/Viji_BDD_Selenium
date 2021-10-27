# from behave import *

# @given('we have behave installed')
# def step_impl(context):
#     pass

# @when('we implement a test')
# def step_impl(context):
#     assert True is not False

# @then('behave will test it for us!')
# def step_impl(context):
#     assert context.failed is False

import re

from pytest_bdd import given, then, scenario

@scenario(
    'multiline.feature',
    'Multiline step using sub indentation',
)
def test_multiline():
    pass


@given(parsers.parse("I have a step with:\n{text}"), target_fixture="i_have_text")
def i_have_text(text):
    return text


@then("the text should be parsed with correct indentation")
def text_should_be_correct(i_have_text, text):
    assert i_have_text == text == 'Some\nExtra\nLines'
