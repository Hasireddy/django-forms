from django import forms

class RegisterForm(forms.Form):
    firstname = forms.CharField(
        min_length=1,
        label="First name",
        max_length=10,
        error_messages={
            "required":"First name should not be empty",
            "max_length":"Maximum characters allowed are 10"

        }
       )
    lastname = forms.CharField(min_length=1,
                               label="Last name",
                               max_length=10,
                                error_messages={
            "required":"First name should not be empty",
            "max_length":"Maximum characters allowed are 10"

        }
        )

         # error_class="errors-class"