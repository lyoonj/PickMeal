from django.core.exceptions import ValidationError 

def validate_score(value):
    """평점(score)이 5보다 크면 Validation Error 를 일으킨다."""
    if value > 5:
        msg = u"'평점은 5 이하로 매겨주세요."
        raise ValidationError(msg)
