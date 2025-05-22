from .models import Ticket

def serialize_ticket(ticket):
    return {
        'id': ticket.id,
        'title': ticket.title,
        'status': ticket.status,
        'created_at': ticket.created_at.isoformat(),
    }
