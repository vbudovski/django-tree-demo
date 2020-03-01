# Generated by Django 2.2.10 on 2020-02-29 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='tree_demo.Category')),
                ('previous', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='next', to='tree_demo.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
