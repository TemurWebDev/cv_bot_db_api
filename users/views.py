from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Users,AdminT,Channel,CV,Skill,UserEducation,UserPersonalInfo,WorkExperience,LanguageCv
from .serializers import UserSerializer,AdminSerializers,ChannelSerializzers,CV_serializers,Skill_serializers,Education_serializers,Personal_serializers,Work_serializers,Language_serializers

from rest_framework.views import APIView
from rest_framework.response import Response



class UserApiView(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer



class UserView(APIView):
    def get(self, request, user_id):
        user = Users.objects.get(user_id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id,format=None):
        user = Users.objects.get(user_id=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AdminView(ListCreateAPIView):
    queryset = AdminT.objects.all()
    serializer_class = AdminSerializers


class AdminUpdateView(APIView):
    def delete(self, request, user_id, format=None):
        admin = AdminT.objects.get(user_id=user_id)
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ChannelView(ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializzers


class ChannelUpdateView(APIView):
    def delete(self, request, channel_id, format=None):
        channel = Channel.objects.get(channel_id=channel_id)
        channel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CvView(ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CV_serializers



class CV_View(APIView):
    def get(self, request, user_id):
        user = CV.objects.get(user__user_id=user_id)
        serializer = CV_serializers(user)
        return Response(serializer.data)

    def put(self, request, user_id,format=None):
        user = CV.objects.get(user__user_id=user_id)
        serializer = CV_serializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class SkillApiView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = Skill_serializers



class SkillView(APIView):
    def get(self, request, user_id):
        user = Skill.objects.get(user_id=user_id)
        serializer = Skill_serializers(user)
        return Response(serializer.data)

    def put(self, request, user_id,format=None):
        user = Skill.objects.get(user_id=user_id)
        serializer = Skill_serializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationApiView(ListCreateAPIView):
    queryset = UserEducation.objects.all()
    serializer_class = Education_serializers


class EducationView(APIView):
    def get(self, request, user_id):
        user = UserEducation.objects.filter(user_id=user_id)
        serializer = Education_serializers(user,many=True)
        return Response(serializer.data)

    def put(self, request, user_id,format=None):
        user = UserEducation.objects.filter(user_id=user_id)
        serializer = Education_serializers(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Educationedit(APIView):

    def get(self, request, user_id,id):
        user = UserEducation.objects.get(user_id=user_id,id=id)
        serializer = Education_serializers(user)
        return Response(serializer.data)


    def put(self, request, user_id,id,format=None):
        user = UserEducation.objects.get(user_id=user_id,id=id)
        serializer = Education_serializers(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PersonalApiView(ListCreateAPIView):
    queryset = UserPersonalInfo.objects.all()
    serializer_class = Personal_serializers



class PersonalView(APIView):
    def get(self, request, user_id):
        user = UserPersonalInfo.objects.get(user_id=user_id)
        serializer = Personal_serializers(user)
        return Response(serializer.data)

    def put(self, request, user_id,format=None):
        user = UserPersonalInfo.objects.get(user_id=user_id)
        serializer = Personal_serializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WorkApiView(ListCreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = Work_serializers


class WorkView(APIView):
    def get(self, request, user_id):
        user = WorkExperience.objects.get(user_id=user_id)
        serializer = Work_serializers(user)
        return Response(serializer.data)

    def put(self, request, user_id,format=None):
        user = WorkExperience.objects.get(user_id=user_id)
        serializer = Work_serializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LanguageApiView(ListCreateAPIView):
    queryset = LanguageCv.objects.all()
    serializer_class = Language_serializers



class LanguageView(APIView):
    def get(self, request, pk):
        user = LanguageCv.objects.get(user_id=pk)
        serializer = Language_serializers(user)
        return Response(serializer.data)

    def put(self, request, pk,format=None):
        user = LanguageCv.objects.get(user_id=pk)
        serializer = Language_serializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)