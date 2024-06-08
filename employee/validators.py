from django.core.validators import RegexValidator

mobile_number_regex = RegexValidator(
    regex=r"^01\d{9}$",
    message="Mobile number must be entered in the format: '01xxxxxxxxx'",
)
