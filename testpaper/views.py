from .models import exam, TestPaper, questions, TestIndex, UserAnswers, UserResult, flag, timer
from .serializers import examSerializer, TestPaperSerializer, questionsSerializer, TestIndexSerializer, UserAnswersSerializer, UserResultSerializer, flagSerializer, timerSerializer
from rest_framework import generics
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import filters


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listexam(generics.ListCreateAPIView):
    queryset = exam.objects.all()
    serializer_class = examSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detailexam(generics.RetrieveUpdateDestroyAPIView):
    queryset = exam.objects.all()
    serializer_class = examSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class ListTestPaper(generics.ListCreateAPIView):
    queryset = TestPaper.objects.all()
    serializer_class = TestPaperSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class DetailTestPaper(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestPaper.objects.all()
    serializer_class = TestPaperSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listquestions(generics.ListCreateAPIView):
    queryset = questions.objects.all()
    serializer_class = questionsSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detailquestions(generics.RetrieveUpdateDestroyAPIView):
    queryset = questions.objects.all()
    serializer_class = questionsSerializer


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class ListTestIndex(generics.ListCreateAPIView):
    queryset = TestIndex.objects.all()
    serializer_class = TestIndexSerializer
    filterset_fields = ('sheet_name', 'level',
                        'subject', 'topic', 'sheet_type')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class DetailTestIndex(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestIndex.objects.all()
    serializer_class = TestIndexSerializer


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
class ListUserResult(generics.ListCreateAPIView):
    queryset = UserResult.objects.all()
    serializer_class = UserResultSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class DetailUserResult(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserResult.objects.all()
    serializer_class = UserResultSerializer


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


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Listtimer(generics.ListCreateAPIView):
    queryset = timer.objects.all()
    serializer_class = timerSerializer
    filterset_fields = ('__all__')


@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class Detailtimer(generics.RetrieveUpdateDestroyAPIView):
    queryset = timer.objects.all()
    serializer_class = timerSerializer
