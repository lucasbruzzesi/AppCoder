from django.db import models
from .models import Avatar
from .forms import AvatarForm
from typing import Any, Dict

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.http import HttpResponse
# from django.db.models.query import QuerySet
# from django.views.generic import ListView, FormView, DetailView
# from .forms import MensajeForm, ConversacionForm

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(user = request.user, imagen = request.FILES['imagen'])
            avatar_anterior = Avatar.objects.filter(user = request.user)
            if len(avatar_anterior)>0:
                avatar_anterior[0].delete()
            avatar.save()
            return render(request, 'AppProyecto/home.html', {'mensaje' : f'Tu avatar ha sido agregado', 'avatar' : obtener_avatar(request)})
        else:
            return render(request, 'AppProyecto/agregar_avatar.html', {'form' : form, 'usuario' : request.user, 'mensaje' : 'Error agregando el avatar',  'avatar' : obtener_avatar(request)})
    else:
        form=AvatarForm()
        return render(request, 'AppProyecto/agregar_avatar.html', {'form' : form, 'usuario' : request.user, 'avatar' : obtener_avatar(request)})

def obtener_avatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return '/media/avatares/defaultavatar.png'



# class ConversacionListView(LoginRequiredMixin, ListView):
    model = Conversacion
    template_name = 'AppProyecto/messages.html'
    context_object_name = 'conversaciones'

    def get_queryset(self):
        return Conversacion.objects.filter(participantes = self.request.user).order_by('fecha_creacion_conversacion')

# class ConversacionDetailView(LoginRequiredMixin, DetailView):
    model = Conversacion
    template_name = 'AppProyecto/detalle_mensajes.html'
    context_object_name = 'conversacion'

    def get_queryset(self):
        return Conversacion.objects.filter(participantes = self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conversacion'] = self.objects.conversacion.all().order_by('fecha_mensaje')
        return context

#class IniciarConversacionView(LoginRequiredMixin, FormView):
    form_class = ConversacionForm
    template_name = 'AppProyecto/add_conversation.html'
    success_url = reverse_lazy('AppProyecto/messages.html')

    def form_valid(self, form):
        participantes = form.cleaned_data['participantes']
        conversacion = Conversacion.objects.create()
        conversacion.participantes.add(self.request.user)
        conversacion.participantes.add(*participantes)
        return super().form_valid(form)

#class ChatListView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'AppProyecto/messages.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        self.conversacion = get_object_or_404(Conversacion, pk = self.kwargs['pk'])
        return Mensaje.objects.filter(conversacion = self.conversacion)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conversacion'] = self.conversacion
        return context

#class ChatView(LoginRequiredMixin, FormView):
    form_class = MensajeForm
    template_name = 'AppProyecto/write_message.html'
    success_url = reverse_lazy('AppProyecto/messages.html')

    def form_valid(self, form):
        conversacion_id = self.kwargs['pk']
        conversacion = get_object_or_404(Conversacion, id = conversacion_id)
        mensaje = form.save(commit=False)
        mensaje.conversacion = conversacion
        mensaje.remitente = self.request.user
        mensaje.save()
        return super().form_valid(form)