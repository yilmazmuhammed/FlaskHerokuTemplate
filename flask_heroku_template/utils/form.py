from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, widgets


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
