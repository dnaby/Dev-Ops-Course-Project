from devops_backend.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from devops_backend.serializers import UserSerializer


@api_view(["GET"])
def getUsers(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def count_visits(request):
    if request.method == "GET":
        # Get the current visit count from the session,
        # or set it to 0 if it doesn't exist
        visit_count = request.session.get("visit_count", 0)
        # Increment the visit count
        visit_count += 1
        # Update the session with the new count
        request.session["visit_count"] = visit_count
        # Return the visit count as JSON
        return JsonResponse({"visit_count": visit_count})
