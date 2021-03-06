import django_tables2 as tables
from .models import Transaction


class TransactionTable(tables.Table):
    class Meta:
        model = Transaction
        fields = (
            "type",
            "due_date",
            "description",
            "estimate",
            "paid",
            "total",
        )
        attrs = {"class": "table table-striped table-bordered"}
        empty_text = "There are no transactions matching the search criteria..."


class ChapterBalanceTable(tables.Table):
    class Meta:
        model = Transaction
        fields = (
            "chapter",
            "region",
            "balance",
        )
