# Generated by Django 4.2.1 on 2023-05-30 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0006_statut"),
        ("epicevents", "0002_alter_statut_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="status",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="authentication.statut",
            ),
        ),
        migrations.DeleteModel(
            name="Statut",
        ),
    ]
