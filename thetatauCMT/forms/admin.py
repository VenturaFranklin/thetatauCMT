from django.contrib import admin
from .models import Badge, Guard, Initiation, Depledge, StatusChange,\
    PledgeForm, RiskManagement, PledgeProgram, Audit, Pledge, ChapterReport
from core.admin import user_chapter


admin.site.register(Badge)
admin.site.register(Guard)


class ChapterReportAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'year', 'term', )
    list_filter = ['chapter', 'year', ]
    ordering = ['-year', ]


admin.site.register(ChapterReport, ChapterReportAdmin)


class PledgeProgramAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'manual', 'year', 'term', )
    list_filter = ['chapter', 'manual', 'year', ]
    ordering = ['-year', ]


admin.site.register(PledgeProgram, PledgeProgramAdmin)


class RiskManagementAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ('user', 'date', 'year', 'term', )
    list_filter = ['user__chapter', 'year', 'term', ]
    ordering = ['-date', ]
    search_fields = ['user__name', ]


admin.site.register(RiskManagement, RiskManagementAdmin)


class AuditAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ('user', 'created', 'year', 'term', )
    list_filter = ['user__chapter', 'year', 'term', ]
    ordering = ['-created', ]
    search_fields = ['user__name', ]


admin.site.register(Audit, AuditAdmin)


class PledgeFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'chapter', 'created', )
    list_filter = ['chapter', 'created', ]
    ordering = ['-created', ]
    search_fields = ['name', ]


admin.site.register(PledgeForm, PledgeFormAdmin)


class InitiationAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ('user', 'date', 'created', user_chapter)
    list_filter = ['date', 'created', 'user__chapter']
    ordering = ['-created',]
    search_fields = ['user__username', 'user__name']


admin.site.register(Initiation, InitiationAdmin)


class DepledgeAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ('user', 'reason', 'date', 'created', user_chapter)
    list_filter = ['reason', 'date', 'created', 'user__chapter']
    ordering = ['-created',]
    search_fields = ['user__username', 'user__name']


admin.site.register(Depledge, DepledgeAdmin)


class StatusChangeAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ('user', 'reason', 'date_start', 'date_end', 'created', user_chapter)
    list_filter = ['reason', 'date_start', 'date_end', 'user__chapter']
    ordering = ['-created',]
    search_fields = ['user__username', 'user__name']


admin.site.register(StatusChange, StatusChangeAdmin)


class PledgeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'school_name',
                    'email_school', 'email_personal', 'created')
    list_filter = ['school_name', 'created', ]
    ordering = ['-created', ]
    search_fields = ['first_name', 'last_name']


admin.site.register(Pledge, PledgeAdmin)
