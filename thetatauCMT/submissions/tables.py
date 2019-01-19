import django_tables2 as tables
from django_tables2.utils import A
from googleapiclient.http import HttpError
from .models import Submission


class FileURLColumn(tables.LinkColumn):
    def compose_url(self, record, *args, **kwargs):
        out_url = ""
        try:
            out_url = record.file.url
        except TimeoutError:
            pass  # Really want to remove all file uploads, ignore for now
        except HttpError:
            pass  # Really want to remove all file uploads, ignore for now
        return out_url


class SubmissionTable(tables.Table):
    name = tables.LinkColumn('submissions:update',
                             args=[A('pk')])
    file = FileURLColumn()

    class Meta:
        model = Submission
        fields = ('name', 'date',
                  'type', 'score', 'file')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no submissions matching the search criteria..."
