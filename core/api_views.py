from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Ticket

@require_GET
def ticket_list_api(request):
    tickets = Ticket.objects.all().values('id', 'title', 'status', 'created_at')
    return JsonResponse(list(tickets), safe=False)
