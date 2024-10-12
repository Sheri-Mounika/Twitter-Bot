from django.forms import Form, CharField

class InputForm(Form):

    followers_count=CharField(max_length=50)
    friends_count=CharField(max_length=50)
    listed_count=CharField(max_length=50)
    favourites_count=CharField(max_length=50)
    verified = CharField(max_length=50)
    statuses_count=CharField(max_length=50)
    default_profile=CharField(max_length=50)
    default_profile_image = CharField(max_length=50)