from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(url):

    url_validator = URLValidator()
    url_1 = True
    url_2 = True

    try:
        url_validator(url)
    except:
        url_1 = False
        url = 'http://' + url
    try:
        url_validator(url)
    except:
        url_2 = False

    if url_1 == False and url_2 == False:
        raise ValidationError('Invalid URL')

    return url
