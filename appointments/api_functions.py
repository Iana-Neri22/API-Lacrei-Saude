from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


def entity_manager(request: Request, url_parameter, model, object_serializer, id_field):

    if request.method == 'GET':
        return get_method(request, url_parameter, model, object_serializer)

    if request.method == 'POST':
        return post_method(request, object_serializer)
    
    if request.method == 'PUT':
        return put_method(request, id_field, model, object_serializer)
    
    if request.method == 'DELETE':
        return delete_method(request, id_field, model)
  

def get_method(request, url_parameter, model, object_serializer):
 
    try:
        if request.GET[url_parameter]:

            entity_id = request.GET[url_parameter]
 
            try:
                entity = model.objects.get(pk=entity_id)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = object_serializer(entity)
            return Response(serializer.data)
            
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

def post_method(request, object_serializer):
    new_entity = request.data

    serializer = object_serializer(data=new_entity)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)


def put_method(request, id_field, model, object_serializer):
    entity = request.data[id_field]

    try:
        updated_entity = model.objects.get(pk=entity)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = object_serializer(updated_entity, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


def delete_method(request, id_field, model):
    entity = request.data[id_field]

    try:
        entity_to_delete = model.objects.get(pk=entity)
        entity_to_delete.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST) 