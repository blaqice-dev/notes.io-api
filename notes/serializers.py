from django.utils import timezone
from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    text = serializers.CharField(allow_null=True, allow_blank=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'created', 'updated')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)

        updated = timezone.now()
        instance.updated = updated
        instance.save()

        return instance
