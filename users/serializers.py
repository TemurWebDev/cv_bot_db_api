from rest_framework import serializers
from .models import Users,AdminT,Channel,CV,Skill,UserEducation,UserPersonalInfo,WorkExperience,LanguageCv

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminT
        fields = '__all__'


class ChannelSerializzers(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class CV_serializers(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'


class Skill_serializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class Education_serializers(serializers.ModelSerializer):
    class Meta:
        model = UserEducation
        fields = '__all__'


class Personal_serializers(serializers.ModelSerializer):
    class Meta:
        model = UserPersonalInfo
        fields = '__all__'


class Work_serializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'


class Language_serializers(serializers.ModelSerializer):
    class Meta:
        model = LanguageCv
        fields = '__all__'