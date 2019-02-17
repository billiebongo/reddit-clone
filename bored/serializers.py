
import logging

logger = logging.getLogger(__name__)
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from bored.models import (User, Location)

import datetime
from django.contrib.auth.password_validation import validate_password

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'lat', 'lon')

class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'dp', 'name', 'username', 'location', 'is_verified')
        extra_kwargs = {'password': {'write_only': True}, }

    # supports changing DP, username, password, location
    def update(self, instance, validated_data):
        print(validated_data)

        if 'dp' in validated_data:
            instance.dp = validated_data.pop('dp')
        else:
            if 'name' in validated_data:
                instance.name = validated_data.pop('name')
            if 'username' in validated_data:
                # check if email alr exists
                domain = "{}{}".format(self.context['request'].build_absolute_uri().split("api/user")[0], "user/")

                user_set = User.objects.filter(username=validated_data["username"])
                print(user_set)
                if user_set:
                    if user_set[0].username == instance.username:
                        raise serializers.ValidationError('This is already your current email')

                else:
                    instance.username = validated_data["username"]
                    # Unactivate account and send activation username
                    instance.is_verified = False
                    task = send_verification_email.apply_async([validated_data["username"], instance.id, domain],
                                                               routing_key='normal',
                                                               queue="normal")
            if (validated_data['password'] != None):
                try:
                    # if instance.password_recently_reset == False:

                    validate_password(validated_data["password"])
                    instance.set_password(validated_data.pop('password'))
                except Exception as e:
                    raise serializers.ValidationError(e)

                # instance.password_recently_reset = True
            if (validated_data['lat'] != None) and (validated_data['lon'] != None):  # assumes lon is in too
                lat = validated_data.pop('lat')
                lon = validated_data.pop('lon')
                location = Location.objects.create(address=find_mrt(float(lat), float(lon)), lat=lat,
                                                   lon=lon)  # new location created FOR NOW
                instance.location = location

        instance.save()
        return instance

    def to_internal_value(self, data):
        print(data)

        internal_value = super(UserSerializer, self).to_internal_value(data)
        lat = data.get("lat")
        password = data.get("password")
        lon = data.get("lon")
        internal_value.update({
            "lat": lat,
            "lon": lon,
            "expo": expo,
            "verify_pw": verify_pw,
            "password": password
        })

        # print(internal_value)

        return internal_value
