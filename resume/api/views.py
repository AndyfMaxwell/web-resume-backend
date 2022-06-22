from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.models import Project
from .serializers import ProjectSerializer

@api_view(["GET"])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
