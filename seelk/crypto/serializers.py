from rest_framework             import serializers

from django.contrib.auth.models import User 
from .models                    import Alert, Rule


class AlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alert
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})

    # We rewrite create and update to hash the password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for f in UserSerializer.Meta.fields:
            setattr(instance, f, validated_data[f])
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rule
        fields = ('__all__')
