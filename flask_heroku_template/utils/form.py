from flask import json
from flask_wtf import FlaskForm
from werkzeug.datastructures import MultiDict
from wtforms import SelectMultipleField, widgets

from flask_heroku_template.utils import LayoutPI


class FormPI(LayoutPI):
    def __init__(self, form, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form = form
        self.errors = []
        for field in form:
            self.errors += field.errors


def form_open(form_name, f_id=None, enctype=None, f_action="", f_class="form-horizontal"):
    f_open = """<form action="%s" method="post" name="%s" """ % (f_action, form_name,)

    if f_id:
        f_open += """ id="%s" """ % (f_id,)
    if enctype:
        f_open += """ enctype="%s" """ % (enctype,)

    f_open += """class="%s">""" % (f_class,)

    return f_open


def form_close():
    return """</form>"""


class CustomFlaskForm(FlaskForm):
    def __init__(self, form_title='Form', form_name='form', form_id='form', *args, **kwargs):
        self.form_title = form_title
        self.open = form_open(form_name=form_name, f_id=form_id)
        self.close = form_close()
        super().__init__(*args, **kwargs)


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


def flask_form_to_dict(request_form: MultiDict, exclude=None, boolean_fields=None, json_fields=None):
    if json_fields is None:
        json_fields = []
    if exclude is None:
        exclude = []
    if boolean_fields is None:
        boolean_fields = []

    result = {
        key: request_form.getlist(key)[0] if len(request_form.getlist(key)) == 1 else request_form.getlist(key)
        for key in request_form
        if key not in exclude and not (len(request_form.getlist(key)) == 1 and request_form.getlist(key)[0] == "")
    }
    for i in boolean_fields:
        if result.get(i):
            result[i] = True
        else:
            result[i] = False

    for i in json_fields:
        if result.get(i):
            result[i] = json.loads(result[i])

    result.pop('submit', None)
    result.pop('csrf_token', None)

    return result
