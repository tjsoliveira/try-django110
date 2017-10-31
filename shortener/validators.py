from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(url):

    validate = URLValidator()
    try:
        validate(url)
    except ValidationError as e:
        raise e
