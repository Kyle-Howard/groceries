# Generated by Django 2.2.3 on 2019-08-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipefinder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_id', models.IntegerField(null=True)),
                ('amount', models.FloatField(null=True)),
                ('unit', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_required',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipefinder.Ingredient'),
        ),
    ]