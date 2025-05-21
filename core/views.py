from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Project, Comment, Attachment
from .forms import TicketForm, CommentForm, AttachmentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

@login_required
def ticket_list(request):
    query = request.GET.get('q')
    tickets = Ticket.objects.select_related('project').all()
    if query:
        tickets = tickets.filter(Q(title__icontains=query) | Q(project__name__icontains=query))
    return render(request, 'tickets/index.html', {'tickets': tickets})

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    comments = ticket.comments.all().order_by('created_at')
    attachments = ticket.attachments.all()
    comment_form = CommentForm()
    attachment_form = AttachmentForm()
    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.ticket = ticket
                comment.author = request.user.username
                comment.save()
                return redirect('ticket_detail', pk=pk)
        elif 'attachment_submit' in request.POST:
            attachment_form = AttachmentForm(request.POST, request.FILES)
            if attachment_form.is_valid():
                attachment = attachment_form.save(commit=False)
                attachment.ticket = ticket
                attachment.save()
                return redirect('ticket_detail', pk=pk)
    return render(request, 'tickets/detail.html', {
        'ticket': ticket,
        'comments': comments,
        'attachments': attachments,
        'comment_form': comment_form,
        'attachment_form': attachment_form,
    })

@login_required
def ticket_add(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            form.save_m2m()
            return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'tickets/add.html', {'form': form})

@login_required
def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_detail', pk=pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/edit.html', {'form': form, 'ticket': ticket})

@login_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')
    return render(request, 'tickets/delete.html', {'ticket': ticket})
