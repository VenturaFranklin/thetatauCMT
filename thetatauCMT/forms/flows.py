import datetime
from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.compat import _
from viewflow.flow import views as flow_views
from core.models import forever
from .models import PrematureAlumnus
from .views import PrematureAlumnusCreateView
from users.models import User, UserStatusChange


@frontend.register
class PrematureAlumnusFlow(Flow):
    process_class = PrematureAlumnus
    process_title = _('Premature Alumnus Process')
    process_description = _('This process is for premature alumnus processing.')

    start = (
        flow.Start(
            PrematureAlumnusCreateView,
            task_title=_('Request Premature Alumnus'))
        .Permission(auto_create=True)
        .Next(this.pending_status)
    )

    pending_status = (
        flow.Handler(
            this.set_status_email,
            task_title=_('Set pending status, send email.'),
        )
        .Next(this.exec_approve)
    )

    exec_approve = (
        flow.View(
            flow_views.UpdateProcessView, fields=['approved_exec', 'exec_comments'],
            task_title=_('Executive Director Review'),
            task_description=_("Pre Alumn Executive Director Review"),
            task_result_summary=_("Messsage was {{ process.approved_exec|yesno:'Approved,Rejected' }}"))
        .Assign(lambda act: User.objects.get(username="venturafranklin@gmail.com"))
        .Next(this.check_approve)
    )

    check_approve = (
        flow.If(
            cond=lambda act: act.process.approved_exec,
            task_title=_('Premature Alumnus Approvement check'),
        )
        .Then(this.alumni_status)
        .Else(this.pending_undo)
    )

    alumni_status = (
        flow.Handler(
            this.set_alumni_status,
            task_title=_('Set status alumni'),
        )
        .Next(this.send)
    )

    pending_undo = (
        flow.Handler(
            this.pending_undo,
            task_title=_('Set status active'),
        )
        .Next(this.send)
    )

    send = (
        flow.Handler(
            this.send_approval_complete,
            task_title=_('Send request complete message'),
        )
        .Next(this.complete)
    )

    complete = flow.End(
        task_title=_('Complete'),
        task_result_summary=_("Request was {{ process.approved_exec|yesno:'Approved,Rejected' }}")
    )

    def set_status_email(self, activation):
        """
        Need to set the pending status
        Email the user the form was received
        :param activation:
        :return:
        """
        user = activation.process.user
        created = activation.process.created
        active = user.status.order_by('-end').filter(status='active').first()
        if not active:
            print(f"There was no active status for user {self.user}")
            UserStatusChange(
                user=user,
                status='active',
                created=created,
                start=created - datetime.timedelta(days=365),
                end=created,
            ).save()
        else:
            active.end = created
            active.created = created
            active.save()
        alumnipends = user.status.filter(status='alumnipend')
        if alumnipends:
            alumnipend = alumnipends[0]
            alumnipend.start = created
            alumnipend.end = forever()
            alumnipend.created = created
            alumnipend.save()
            for alumnipend in alumnipends[1:]:
                alumnipend.delete()
        else:
            UserStatusChange(
                user=user,
                created=created,
                status='alumnipend',
                start=created,
                end=forever(),
            ).save()

    def pending_undo(self, activation):
        user = activation.process.user
        alumnipends = user.status.filter(status='alumnipend')
        if alumnipends:
            for alumnipend in alumnipends:
                alumnipend.delete()

    def set_alumni_status(self, activation):
        user = activation.process.user
        alumnipend = user.status.order_by('-end').filter(status='alumnipend').first()
        created = activation.task.created
        if not alumnipend:
            print(f"There was no alumnipend status for user {self.user}")
            UserStatusChange(
                user=user,
                status='alumnipend',
                created=created,
                start=created - datetime.timedelta(days=365),
                end=created,
            ).save()
        else:
            alumnipend.end = created
            alumnipend.save()
        alumnis = user.status.filter(status='alumni')
        if alumnis:
            alumni = alumnis[0]
            alumni.start = created
            alumni.end = forever()
            alumni.created = created
            alumni.save()
            for alumni in alumnis[1:]:
                alumni.delete()
        else:
            UserStatusChange(
                user=user,
                created=created,
                status='alumni',
                start=created,
                end=forever(),
            ).save()

    def send_approval_complete(self, activation):
        print(activation.process.created_by)
