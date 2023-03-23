from wtforms import SubmitField

from flask_template.utils.forms import CustomFlaskForm


class ExampleForm(CustomFlaskForm):
    submit = SubmitField(label="Kaydet")

    def __init__(self, form_title='Example form', f_class="form-validation", *args, **kwargs):
        super().__init__(
            form_title=form_title,
            f_class=f_class,
            *args, **kwargs
        )
