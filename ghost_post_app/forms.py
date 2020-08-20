from django import forms


class AddPost(forms.Form):
    # BOAST = "B"
    # ROAST = "R"
    post = forms.CharField(max_length=180, required=True,
                           strip=True, label="Post")
    # choices = [("", "------"), (BOAST, "Boast"), (ROAST, "Roast")]
    # boast_or_roast_choice = forms.ChoiceField(choices=choices)
    boast = forms.BooleanField(required=False)
