from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@login_required
def home(request):
    messages = Message.objects.filter(receiver=request.user)
    context = {'msg': messages}
    return render(request, 'message/home.html', context)


@login_required
def create_message(request):
    if request.method == 'GET':
        context = {'form': MessageForm()}
        return render(request,'message/message_form.html',context)
    
    elif request.method == 'POST':
        receiver_name = request.POST.get("receiver")
        form = MessageForm(request.POST)

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT id, username FROM auth_user WHERE username= '{receiver_name}'")
            #cursor.execute("SELECT id, username FROM auth_user WHERE username=  %s", [receiver_name])
            receiver = cursor.fetchone()

            if receiver:
                if form.is_valid():
                    message = form.save(commit=False)
                    message.sender = request.user
                    message.receiver = User.objects.get(id = receiver[0])
                    message.save()

                    messages.success(request,  f'The message has been sent to {receiver[1]} successfully.')
                    return redirect('message')
                else:
                    messages.error(request, 'Please correct the following errors:')
                    return render(request,'message/message_form.html',{'form':form})
            else:
                messages.error(request, f'The user {receiver_name} does not exist.')
                return render(request,'message/message_form.html',{'form':form})


@login_required   
@csrf_exempt     
def delete_message(request, id):
    message = get_object_or_404(Message, pk=id)
    context = {'message': message}    
    
    if request.method == 'GET':
        return render(request, 'message/message_confirm_delete.html',context)
    elif request.method == 'POST':
        message.delete()
        messages.success(request,  'The message has been deleted successfully.')
        return redirect('message')
