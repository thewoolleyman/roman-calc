import subprocess, unittest
from hamcrest import assert_that, equal_to

@given(u'that I have the Roman Calculator installed')
def step_impl(context):
    pass

# @when(u'I run "python rome_calc.py I + I"')
# def step_impl(context):
#     context.output = subprocess.check_output(["python", "rome_calc.py", "I", "+", "I"])
#
# @then(u'I should get "II"')
# def step_impl(context):
#     assert context.output.strip() == "II"

@when(u'I run "python rome_calc.py {arguments}')
def step_impl(context, arguments):
    split_arguments = arguments.split(" ")
    split_arguments.insert(0, "rome_calc.py")
    split_arguments.insert(0, "python")
    context.output = subprocess.check_output(split_arguments)


@then(u'I should get "{result}"')
def step_impl(context, result):
    assert_that(context.output.strip(), equal_to(result.strip()))

# @when(u'I run "python rome_calc.py I + I + I"')
# def step_impl(context):
#     context.output = subprocess.check_output(["python", "rome_calc.py", "I", "+",
#     "I", "+", "I"])

# @then(u'I should get "III"')
# def step_impl(context):
#     assert context.output.strip() == "III"

# @when(u'I run "python rome_calc.py I + III"')
# def step_impl(context):
#     context.output = subprocess.check_output(["python", "rome_calc.py", "I", "+",
#     "III"])

# @then(u'I should get "IV"')
# def step_impl(context):
#     assert context.output.strip() == "IV"
    # assertEquals(context.output.strip(), "IV")
