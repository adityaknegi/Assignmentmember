from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from Utilities.getUserId import getUserId
from Utilities.utilities import generate_user_hash
from Utilities.validateUser import validate_user
from usertracker.serializers import *


@api_view(['POST'])
def user_validator(request):
    if request.method == 'POST':
        user_email = request.data.get("user_email")
        user_data = getUserId(user_email)
        if user_data is not None:
            user_serializer = UserSerializer(user_data)
            return JsonResponse(user_serializer.data,status=status.HTTP_409_CONFLICT)
        else:
            user_serializer = UserSerializer(data=request.data)
            if user_serializer.is_valid():
                user_serializer.save(user_hash=generate_user_hash())
                return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_activity(request, user_email, user_hash):
    if request.method == 'POST' and validate_user(user_email, user_hash):
        user = User.objects.get(user_email=user_email)
        if user is not None:
            activity_p_serializer = ActivityPSerializer(data=request.data)
            if activity_p_serializer.is_valid():
                activity_p_serializer.save(user=user)
                return JsonResponse(activity_p_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(activity_p_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'1': 1}, status=status.HTTP_401_UNAUTHORIZED)
        return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def get_members(request):
    """ members detail"""
    json_str = {"ok": False, "members": []}

    if request.method == 'GET':
        json_str["ok"] = True
        user = User.objects.all()

        """ user detail """
        user_str = {"id": None, "real_name": None, "tz": None,"activity_periods": [] }

        """ user activity period """
        user_act = {"start_time": None,"end_time": None}

        """Add one by one users"""
        for user_i in user:
            user_str["id"] = user_i.id
            user_str["real_name"] = user_i.user_first_name + ' ' + user_i.user_last_name
            user_str["tz"] = user_i.time_zone
            user_str["activity_periods"] = []
            """ All activity of user_i"""
            activity = Activity.objects.filter(user_id=user_i.id)
            for activity_i in activity:
                user_act["start_time"] = activity_i.start_time
                user_act["end_time"] = activity_i.end_time
                user_str["activity_periods"].append(user_act.copy())
            json_str['members'].append(user_str.copy())
        return JsonResponse(json_str, status=status.HTTP_200_OK)
    return JsonResponse(json_str, status=status.HTTP_400_BAD_REQUEST)


