from rest_framework import serializers

from core.models import Project, ProjectMember
from user.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    creator_id = serializers.IntegerField(write_only=True)
    creator_name = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'creator_name', 'creator_id')

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return ''


class ProjectMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    project = ProjectSerializer()

    class Meta:
        model = ProjectMember
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = ProjectMember
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    executor = UserSerializer()

    class Meta:
        model = ProjectMember
        fields = '__all__'


class TaskDocumentSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    creator = UserSerializer(read_only=True)

    class Meta:
        model = ProjectMember
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    creator = UserSerializer(read_only=True)

    class Meta:
        model = ProjectMember
        fields = '__all__'



