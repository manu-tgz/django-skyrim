# Generated by Django 4.0.5 on 2022-06-20 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage_point', models.IntegerField(verbose_name='damage point')),
            ],
        ),
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('time', models.TimeField(verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=30, unique=True, verbose_name='character name')),
                ('health_points', models.IntegerField(verbose_name='health points')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user id')),
            ],
        ),
        migrations.CreateModel(
            name='DamageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15, unique=True, verbose_name='damage type')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30, unique=True, verbose_name='place type')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_name', models.CharField(max_length=30, unique=True, verbose_name='race name')),
                ('weakness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.damagetype', verbose_name='weakness')),
            ],
        ),
        migrations.CreateModel(
            name='Blow',
            fields=[
                ('id_blow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.attack', verbose_name='blow id')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerRace',
            fields=[
                ('id_race', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.race', verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('spell_name', models.CharField(max_length=30, unique=True, verbose_name='attack name')),
                ('id_spell', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.attack', verbose_name='spell id')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.character', verbose_name='Character id')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=30, unique=True, verbose_name='place name')),
                ('place_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.placetype', verbose_name='place type')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_event', models.IntegerField(verbose_name='event id')),
                ('health_points_before', models.IntegerField(verbose_name='health point before')),
                ('health_points_after', models.IntegerField(verbose_name='health point after')),
                ('id_attack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.attack', verbose_name='attack id')),
                ('id_attacker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attacker', to='data.character', verbose_name='attacker id')),
                ('id_battle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.battle', verbose_name='battle id')),
                ('id_damaged', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='damaged', to='data.character', verbose_name='damaged id')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='race_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.race', verbose_name='race type'),
        ),
        migrations.CreateModel(
            name='Beast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.character', verbose_name='character id')),
                ('place', models.ManyToManyField(to='data.place', verbose_name='place id')),
            ],
        ),
        migrations.CreateModel(
            name='BattleCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.battle', verbose_name='battle id')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.character', verbose_name='character')),
            ],
        ),
        migrations.AddField(
            model_name='battle',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.place', verbose_name='place'),
        ),
        migrations.AddField(
            model_name='attack',
            name='attack_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.damagetype', verbose_name='attack type'),
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id_battle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.battle', verbose_name='battle id')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.character', verbose_name='winner')),
            ],
        ),
        migrations.CreateModel(
            name='KnownSpell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell_used', models.BooleanField(verbose_name='spell used')),
                ('id_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.player', verbose_name='player id')),
                ('id_spell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.spell', verbose_name='spell id')),
            ],
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('health_points_before__gt', 0)), name='health point before constraint'),
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.UniqueConstraint(fields=('id_event', 'id_battle'), name='event constraint'),
        ),
        migrations.AddConstraint(
            model_name='character',
            constraint=models.CheckConstraint(check=models.Q(('health_points__gt', 0)), name='health point constraint'),
        ),
        migrations.AddField(
            model_name='beast',
            name='id_attack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.blow', verbose_name='attack id'),
        ),
        migrations.AddConstraint(
            model_name='battlecharacter',
            constraint=models.UniqueConstraint(fields=('battle', 'character'), name='battle character constraint'),
        ),
        migrations.AddConstraint(
            model_name='battle',
            constraint=models.UniqueConstraint(fields=('place', 'date', 'time'), name='battle constraint'),
        ),
        migrations.AddConstraint(
            model_name='attack',
            constraint=models.CheckConstraint(check=models.Q(('damage_point__gt', 0)), name='damage attack point'),
        ),
        migrations.AddConstraint(
            model_name='attack',
            constraint=models.UniqueConstraint(fields=('damage_point', 'attack_type'), name='unique attack id'),
        ),
        migrations.AddConstraint(
            model_name='knownspell',
            constraint=models.UniqueConstraint(fields=('id_player', 'id_spell'), name='know constraint'),
        ),
    ]
