from rest_framework import decorators,filters ,response,status, viewsets,authentication, permissions
from .serializers import NameModel, NameSerializer


# IsAuthenticated Permissions
@decorators.api_view(['GET'])
@decorators.authentication_classes([authentication.BasicAuthentication])
@decorators.permission_classes([permissions.IsAuthenticated])
def is_auth (request) :


    names = NameModel.objects.all()
    serializer = NameSerializer(names,many=True)

    return response.Response(serializer.data,status=status.HTTP_200_OK)



# IsAdminUser Permissions
@decorators.api_view(['GET','POST'])
@decorators.authentication_classes([authentication.BasicAuthentication])
@decorators.permission_classes([permissions.IsAdminUser])
def is_admin (request) :
    
    if request.method == "POST" : 
        serializer = NameSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
    
        else :
            return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    names = NameModel.objects.all()
    serializer = NameSerializer(names,many=True)

    return response.Response(serializer.data,status=status.HTTP_200_OK)



# IsAuthentication Or Readonly Permissions
@decorators.api_view(['GET','POST'])
@decorators.authentication_classes([authentication.BasicAuthentication])
@decorators.permission_classes([permissions.IsAuthenticatedOrReadOnly])
def is_auth_or_readonly (request) :

    names = NameModel.objects.all()
    serializer = NameSerializer(names,many=True)

    return response.Response(serializer.data,status=status.HTTP_200_OK)


# Token Authentications
@decorators.api_view(['GET','POST'])
@decorators.authentication_classes([authentication.TokenAuthentication])
@decorators.permission_classes([permissions.IsAuthenticated])
def token_authentication (request) :

    names = NameModel.objects.all()
    serializer = NameSerializer(names,many=True)

    return response.Response(serializer.data,status=status.HTTP_200_OK)




# Token And Authentication using viewsets 
class NamesViewSet (viewsets.ModelViewSet) :
    
    queryset = NameModel.objects.all()
    serializer_class = NameSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']