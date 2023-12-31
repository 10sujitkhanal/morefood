# Generated by Django 4.2.7 on 2023-11-26 12:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_alter_menu_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menu')),
            ],
        ),
    ]
