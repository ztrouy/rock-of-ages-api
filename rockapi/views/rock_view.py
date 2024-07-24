from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rockapi.models import Rock, Type

class RockView(ViewSet):
    """Rock view set"""

    
    def list(self, request):
        """Handle GET requests for all items
        
        Returns:
            Response -- JSON serialized array
        """

        try:
            rocks = Rock.objects.all()
            serialized = RockSerializer(rocks, many=True)
            
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """Handle POST operations
        
        Returns:
            Response -- JSON serialized instance
        """

        # You will implement this feature in a future chapter
        return Response("", status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RockTypeSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = Type
        fields = ( 'label', )


class RockSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    type = RockTypeSerializer(many=False)
    
    class Meta:
        model = Rock
        fields = ( 'id', 'name', 'weight', 'user', 'type' )
