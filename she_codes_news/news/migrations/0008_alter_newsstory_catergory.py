# Generated by Django 4.0.1 on 2022-02-19 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_newsstory_colors_newsstory_catergory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='catergory',
            field=models.CharField(choices=[('cat', 'CAT'), ('dog', 'DOG'), ('horse', 'HORSE'), ('duck', 'DUCK'), ('other', 'OTHER')], default='other', max_length=6),
        ),
    ]