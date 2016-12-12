from django import forms
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def start_session(self):

        print()
        pass
        # user = authenticate(user_name=self.user_name, password=self.password)
        # if user is not None:
        #     print('inicio session')
        # else:
        #     print('No inicio session')
