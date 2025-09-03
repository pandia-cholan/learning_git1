from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from restapi.models import ComputerHardwareModel
from restapi.serializers import ComputerHardwareSerializer

class DeleteByComputerHardwareIdView(CreateAPIView):
    serializer_class = ComputerHardwareSerializer

    def post(self, request, *args, **kwargs):
        try:
            pk = request.data.get('id')
            hardware = ComputerHardwareModel.objects.get(pk = pk)
            hardware.delete()
            return Response({
                'response_code': 204,
                'message': "Successfully Deleted",
                'statusFlag': True,
                'status': "SUCCESS",
                'errorDetails': None,
                'data': None
            }, status=204)
        except ComputerHardwareModel.DoesNotExist as e:
            return Response({
                'response_code': 404,
                'message': "Not Found Record",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': str(e),
                'data': None
            })
        except Exception as e:
            return Response({
                'response_code': 500,
                'message': "Internal Error",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': str(e),
                'data': None
            }, status=500)