from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

def validate_email(value):
        email = value
        if '.edu' in email:
            raise ValidationError('we do not accept edu emails')


CATEGORIES = ['Mexican','Asian','American','Whatever']


def validate_category(value):
    cat = value.capitalize()
    print(cat)
    if not cat in CATEGORIES:
        raise  ValidationError("{value} is not a valid category".format(value=value))