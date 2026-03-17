from django import forms


def check_name(value) :
    if value == "テスト":
        raise forms.ValidationError("テストではダメだよ")