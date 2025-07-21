from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import User, Payment, Subscribe


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "phone", "city", "avatar")


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class SubscribeSerializer(ModelSerializer):
    subscribe_check = SerializerMethodField()

    def get_subscribe_check(self, instance):
        if instance.subscribe_course.all().first():
            return instance.subscribe_course.all().first().course
        return 0

    class Meta:
        model = Subscribe
        fields = '__all__'
