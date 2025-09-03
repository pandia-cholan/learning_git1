from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from restapi.models import ComputerHardwareModel
from restapi.serializers import ComputerHardwareSerializer


class SearchFilterByIdOrNameView(GenericAPIView):
    serializer_class = ComputerHardwareSerializer

    def post(self, request, *args, **kwargs):
        try:
            print(request)
            print(dir(request))
            id = request.data.get('id', None)
            name = request.data.get('name', None)

            if not name and not id:
                return Response({
                        'response_code': 400,
                        'message': "Required Query Params",
                        'statusFlag': False,
                        'status': "FAILED",
                        'errorDetails': "Required Name or Id of the Computer Hardware Record",
                        'data': None
                    }, status = 400)

            hardwares = None

            if id:
                hardwares = ComputerHardwareModel.objects.filter(id = id)
            else:
                hardwares = ComputerHardwareModel.objects.filter(name__icontains = name)

            return Response({
                'response_code': 200,
                'message': "Successfully Fetched",
                'statusFlag': True,
                'status': "SUCCESS",
                'errorDetails': None,
                'data': ComputerHardwareSerializer(hardwares, many=True).data
            })
        except ComputerHardwareModel.DoesNotExist as e:
            return Response({
                'response_code': 404,
                'message': "Not Found",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': str(e),
                'data': None
            }, status=404)
        except Exception as e:
            return Response({
                'response_code': 500,
                'message': "Internal Error",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': str(e),
                'data': None
            }, status=500)
