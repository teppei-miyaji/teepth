import logging
from django.core.mail import send_mail

logger = logging.getLogger(__name__)

def notify_ticket_update(ticket, user):
    message = f"チケット『{ticket.title}』が{user}により更新されました。"
    logger.info(message)
    send_mail(
        subject="チケット更新通知",
        message=message,
        from_email="noreply@teepth.local",
        recipient_list=["admin@example.com"],
        fail_silently=True
    )
