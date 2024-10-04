from . import models
from . import serializers
from . import views

class TestService:

    @classmethod
    def finish_test(cls, user, points, test):
        if not user.is_anonymous and user not in test.users.all():
            user.points = points
            test.users.add(user)
            user.save()
            
        serialized_data = {
            "title": f"{test.title}",
            "photo": f"{test.photo.url}",
            "points": f"{points}/{test.questions.count()}",
        }
        return serialized_data
