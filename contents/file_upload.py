from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class CSVFile(FlaskForm):
    file = FileField(validators=[FileRequired(), FileAllowed(['csv'])])

