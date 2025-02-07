from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todo_items = TodoItem.objects.all()
        todoitem_serializer = TodoItemSerializer(todo_items, many=True)
        return JsonResponse(todoitem_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    if request.method == 'POST':
        todoitem_data = JSONParser().parse(request)
        todoitem_serializer = TodoItemSerializer(data=todoitem_data)
        print(todoitem_serializer.is_valid())
        if not todoitem_serializer.is_valid():
            return JsonResponse(todoitem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        todoitem_serializer.save()
        return JsonResponse(todoitem_serializer.data, status=status.HTTP_201_CREATED) 
 
 
@api_view(['PUT', 'DELETE'])
def todo_item(request, pk):
    print("tutorial detail")
    # try: 
    #     tutorial = TodoItem.objects.get(pk=pk) 
    # except TodoItem.DoesNotExist: 
    #     return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # if request.method == 'PUT': 
    #     tutorial_data = JSONParser().parse(request) 
    #     tutorial_serializer = TodoItemSerializer(tutorial, data=tutorial_data) 
    #     if tutorial_serializer.is_valid(): 
    #         tutorial_serializer.save() 
    #         return JsonResponse(tutorial_serializer.data) 
    #     return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    # elif request.method == 'DELETE': 
    #     tutorial.delete() 
    #     return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)