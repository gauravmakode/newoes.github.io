from .models import level, subject, topic, sheet_name, questions, index, UserAnswers, flag
from .serializers import levelSerializer, subjectSerializer, topicSerializer, sheet_nameSerializer, questionsSerializer, indexSerializer, UserAnswersSerializer, flagSerializer
from rest_framework import generics
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import filters


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listlevel(generics.ListCreateAPIView):
    queryset = level.objects.all()
    serializer_class = levelSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detaillevel(generics.RetrieveUpdateDestroyAPIView):
    queryset = level.objects.all()
    serializer_class = levelSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listsubject(generics.ListCreateAPIView):
    queryset = subject.objects.all()
    serializer_class = subjectSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detailsubject(generics.RetrieveUpdateDestroyAPIView):
    queryset = subject.objects.all()
    serializer_class = subjectSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listtopic(generics.ListCreateAPIView):
    queryset = topic.objects.all()
    serializer_class = topicSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detailtopic(generics.RetrieveUpdateDestroyAPIView):
    queryset = topic.objects.all()
    serializer_class = topicSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listsheetname(generics.ListCreateAPIView):
    queryset = sheet_name.objects.all()
    serializer_class = sheet_nameSerializer
    filterset_fields = ('sheet_name', 'level',
                        'subject', 'topic', 'sheet_type')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detailsheetname(generics.RetrieveUpdateDestroyAPIView):
    queryset = sheet_name.objects.all()
    serializer_class = sheet_nameSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listquestions(generics.ListCreateAPIView):
    queryset = questions.objects.all()
    serializer_class = questionsSerializer
    filterset_fields = ('sheet_name', 'question_no', 'select_sheet_name')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detailquestions(generics.RetrieveUpdateDestroyAPIView):
    queryset = questions.objects.all()
    serializer_class = questionsSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listindex(generics.ListCreateAPIView):
    queryset = index.objects.all()
    serializer_class = indexSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detailindex(generics.RetrieveUpdateDestroyAPIView):
    queryset = index.objects.all()
    serializer_class = indexSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class ListUserAnswers(generics.ListCreateAPIView):
    queryset = UserAnswers.objects.all()
    serializer_class = UserAnswersSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class DetailUserAnswers(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnswers.objects.all()
    serializer_class = UserAnswersSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listflag(generics.ListCreateAPIView):
    queryset = flag.objects.all()
    serializer_class = flagSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detailflag(generics.RetrieveUpdateDestroyAPIView):
    queryset = flag.objects.all()
    serializer_class = flagSerializer
