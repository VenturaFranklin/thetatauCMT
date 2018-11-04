# Generated by Django 2.0.3 on 2018-06-15 18:31
import os
import datetime
from django.utils import timezone
from django.conf import settings
from django.db import migrations
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
# result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
#                                                  range=RANGE_NAME).execute()
# values = result.get('values', [])
# print(values)
# for id_obj, row in enumerate(values):
#     if id_obj == 0:
#         continue

    # start_index = 11
    # end_index = 12
    # if len(row) > 10:
    #     # There is a role, but maybe no dates
    #     if len(row) > 11:
    #         # There is a role, with start, but maybe no end date
    #         start = row[start_index]
    #         if len(row) > 12:
    #             end = row[end_index]
    #             print(start, end)
    #             start = datetime.datetime.strptime(start, '%m/%d/%Y')
    #             end = datetime.datetime.strptime(end, '%m/%d/%Y')
    #             print(start, end)



def load_users(apps, schema_editor):
    return
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    id_file = os.path.join(settings.ROOT_DIR.root, r'secrets/GoogleSheetsClient_id.json')
    id_file_out = os.path.join(settings.ROOT_DIR.root, r'secrets/GoogleSheetsClient_id_out.json')
    # print(id_file)
    store = file.Storage(id_file_out)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(id_file, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    SPREADSHEET_ID = '1f3bklkSBhpwA29dnNHyH73l8JGIc7rF1YiBjGg6owUY'
    RANGE_NAME = 'Users!A1:M'
    user = apps.get_model("users", "User")
    chapter = apps.get_model("chapters", "Chapter")
    role = apps.get_model("users", "UserRoleChange")
    status = apps.get_model("users", "UserStatusChange")
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        raise ValueError('No data found.')
    first_name_index = 0
    last_name_index = 1
    email_index = 2
    name_index = 3
    badge_number_index = 4
    major_index = 5
    graduation_year_index = 6
    phone_number_index = 7
    chapter_index = 8
    status_index = 9
    role_index = 10
    start_index = 11
    end_index = 12
    for id_obj, row in enumerate(values):
        print(row)
        if id_obj == 0:
            continue
        chapter_obj = chapter.objects.get(name=row[chapter_index])
        badge_number_val = row[badge_number_index]
        if badge_number_val != "":
            badge_number_val = int(badge_number_val)
        else:
            badge_number_val = None
        user_id = f"{chapter_obj.greek}{badge_number_val}"
        print("USERID: ", user_id)
        try:
            user_obj = user.objects.get(user_id=user_id)
        except user.DoesNotExist:
            user_obj = None
        if user_obj is None:
            phone_number_val = row[phone_number_index]
            if phone_number_val != "":
                phone_number_val = int(phone_number_val)
            graduation_year_val = int(row[graduation_year_index])
            user_obj = user(
                # id=id_obj,
                user_id=user_id,
                username=row[email_index],
                first_name=row[first_name_index],
                last_name=row[last_name_index],
                email=row[email_index],
                name=row[name_index],
                badge_number=badge_number_val,
                major=row[major_index],
                graduation_year=graduation_year_val,
                phone_number=phone_number_val,
                chapter=chapter_obj,
            )
            user_obj.save()
            status_obj = status(
                user=user_obj,
                status=row[status_index],
                start=timezone.now(),
                end=datetime.datetime(graduation_year_val, 7, 1)
            )
            status_obj.save()
        if len(row) > 10:
            # There is a role, but maybe no dates
            if len(row) > 11:
                start = datetime.datetime.strptime(row[start_index], '%m/%d/%Y')
            else:
                start = timezone.now()
            if len(row) > 12:
                end = datetime.datetime.strptime(row[end_index], '%m/%d/%Y')
            else:
                end = timezone.now() + timezone.timedelta(weeks=52)
            try:
                # We need to check if exact role already exists
                role.objects.get(user=user_obj, role=row[role_index],
                                 start=start, end=end)
            except role.DoesNotExist:
                role_obj = role(
                    user=user_obj,
                    role=row[role_index],
                    start=start,
                    end=end
                )
                role_obj.save()


def migrate_data_backward(apps, schema_editor):
    user = apps.get_model("users", "User")
    user.objects.all().delete()
    role = apps.get_model("users", "UserRoleChange")
    role.objects.all().delete()
    status = apps.get_model("users", "UserStatusChange")
    status.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180615_1337'),
        ('chapters', '0004_initial_chapters_data'),
    ]

    operations = [
        migrations.RunPython(load_users,
                             migrate_data_backward),
    ]
