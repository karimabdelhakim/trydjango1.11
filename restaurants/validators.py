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


CATEGORIES = ['mexican','asian','american','whatever']


def validate_category(value):
    if not value in CATEGORIES:
        raise  ValidationError("{value} is not a valid category".format(value=value))  