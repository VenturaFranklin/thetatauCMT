from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig
from django.views.generic.edit import FormMixin
from scores.models import ScoreType


class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET,
                                        queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class TypeFieldFilteredChapterAdd(FormMixin):
    score_type = "Evt"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['type'].queryset = ScoreType.objects.filter(
            type=self.score_type).all()
        return form

    def form_valid(self, form):
        form.instance.chapter = self.request.user.chapter
        response = super().form_valid(form)
        return response
