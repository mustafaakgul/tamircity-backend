from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comments.models import Comment
from reservations.models import Reservation


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created_date',]

    # def validate(self, attrs):
    #     if(attrs["parent"]):
    #         if attrs["parent"].post != attrs["post"]:
    #             raise serializers.ValidationError("something went wrong")
    #     return attrs


class UserSerializer(ModelSerializer):


    class Meta:
        model = User
        fields = ('first_name','last_name','id','email')


class ReservationCommentSerializer(ModelSerializer):


    class Meta:
        model = Reservation
        fields = ('full_name', 'slug', 'id', 'description', 'created_date')


class CommentListSerializer(ModelSerializer):
    queryset = Comment.objects.all()
    # replies = SerializerMethodField()
    user = UserSerializer()
    reservation = ReservationCommentSerializer()
    # depth = 1 # 1 level of depth


    class Meta:
        model = Comment
        fields = '__all__'

    # def get_replies(self, obj):
    #     if obj.any_children:
    #         return CommentListSerializer(obj.children(), many=True).data

    # def get_queryset(self):
    #     return Comment.objects.filter(parent = None)


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]