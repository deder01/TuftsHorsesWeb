# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HorseShow'
        db.create_table('horseshow_horseshow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dateStart', self.gf('django.db.models.fields.DateField')()),
            ('dateEnd', self.gf('django.db.models.fields.DateField')()),
            ('travelTime', self.gf('django.db.models.fields.IntegerField')()),
            ('hostingBarn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Barn'])),
        ))
        db.send_create_signal('horseshow', ['HorseShow'])

        # Adding M2M table for field admin on 'HorseShow'
        db.create_table('horseshow_horseshow_admin', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshow', models.ForeignKey(orm['horseshow.horseshow'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_horseshow_admin', ['horseshow_id', 'user_id'])

        # Adding M2M table for field horseShowDays on 'HorseShow'
        db.create_table('horseshow_horseshow_horseShowDays', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshow', models.ForeignKey(orm['horseshow.horseshow'], null=False)),
            ('horseshowday', models.ForeignKey(orm['horseshow.horseshowday'], null=False))
        ))
        db.create_unique('horseshow_horseshow_horseShowDays', ['horseshow_id', 'horseshowday_id'])

        # Adding model 'Barn'
        db.create_table('horseshow_barn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ownerBarn', to=orm['auth.User'])),
        ))
        db.send_create_signal('horseshow', ['Barn'])

        # Adding M2M table for field trainers on 'Barn'
        db.create_table('horseshow_barn_trainers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('barn', models.ForeignKey(orm['horseshow.barn'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_barn_trainers', ['barn_id', 'user_id'])

        # Adding M2M table for field riders on 'Barn'
        db.create_table('horseshow_barn_riders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('barn', models.ForeignKey(orm['horseshow.barn'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_barn_riders', ['barn_id', 'user_id'])

        # Adding model 'Horse'
        db.create_table('horseshow_horse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('wins', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('losses', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('horseshow', ['Horse'])

        # Adding model 'HorseShowDay'
        db.create_table('horseshow_horseshowday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('startTime', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('horseshow', ['HorseShowDay'])

        # Adding M2M table for field rings on 'HorseShowDay'
        db.create_table('horseshow_horseshowday_rings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshowday', models.ForeignKey(orm['horseshow.horseshowday'], null=False)),
            ('ring', models.ForeignKey(orm['horseshow.ring'], null=False))
        ))
        db.create_unique('horseshow_horseshowday_rings', ['horseshowday_id', 'ring_id'])

        # Adding M2M table for field trainers on 'HorseShowDay'
        db.create_table('horseshow_horseshowday_trainers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshowday', models.ForeignKey(orm['horseshow.horseshowday'], null=False)),
            ('trainer', models.ForeignKey(orm['horseshow.trainer'], null=False))
        ))
        db.create_unique('horseshow_horseshowday_trainers', ['horseshowday_id', 'trainer_id'])

        # Adding model 'Ring'
        db.create_table('horseshow_ring', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('eventLength', self.gf('django.db.models.fields.IntegerField')(default=20)),
        ))
        db.send_create_signal('horseshow', ['Ring'])

        # Adding M2M table for field divisions on 'Ring'
        db.create_table('horseshow_ring_divisions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ring', models.ForeignKey(orm['horseshow.ring'], null=False)),
            ('division', models.ForeignKey(orm['horseshow.division'], null=False))
        ))
        db.create_unique('horseshow_ring_divisions', ['ring_id', 'division_id'])

        # Adding model 'Trainer'
        db.create_table('horseshow_trainer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('details', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('barn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Barn'])),
        ))
        db.send_create_signal('horseshow', ['Trainer'])

        # Adding M2M table for field riders on 'Trainer'
        db.create_table('horseshow_trainer_riders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trainer', models.ForeignKey(orm['horseshow.trainer'], null=False)),
            ('rider', models.ForeignKey(orm['horseshow.rider'], null=False))
        ))
        db.create_unique('horseshow_trainer_riders', ['trainer_id', 'rider_id'])

        # Adding model 'Rider'
        db.create_table('horseshow_rider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('details', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('horse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Horse'])),
        ))
        db.send_create_signal('horseshow', ['Rider'])

        # Adding model 'Division'
        db.create_table('horseshow_division', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('judge', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('horseshow', ['Division'])

        # Adding M2M table for field riders on 'Division'
        db.create_table('horseshow_division_riders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('division', models.ForeignKey(orm['horseshow.division'], null=False)),
            ('rider', models.ForeignKey(orm['horseshow.rider'], null=False))
        ))
        db.create_unique('horseshow_division_riders', ['division_id', 'rider_id'])


    def backwards(self, orm):
        # Deleting model 'HorseShow'
        db.delete_table('horseshow_horseshow')

        # Removing M2M table for field admin on 'HorseShow'
        db.delete_table('horseshow_horseshow_admin')

        # Removing M2M table for field horseShowDays on 'HorseShow'
        db.delete_table('horseshow_horseshow_horseShowDays')

        # Deleting model 'Barn'
        db.delete_table('horseshow_barn')

        # Removing M2M table for field trainers on 'Barn'
        db.delete_table('horseshow_barn_trainers')

        # Removing M2M table for field riders on 'Barn'
        db.delete_table('horseshow_barn_riders')

        # Deleting model 'Horse'
        db.delete_table('horseshow_horse')

        # Deleting model 'HorseShowDay'
        db.delete_table('horseshow_horseshowday')

        # Removing M2M table for field rings on 'HorseShowDay'
        db.delete_table('horseshow_horseshowday_rings')

        # Removing M2M table for field trainers on 'HorseShowDay'
        db.delete_table('horseshow_horseshowday_trainers')

        # Deleting model 'Ring'
        db.delete_table('horseshow_ring')

        # Removing M2M table for field divisions on 'Ring'
        db.delete_table('horseshow_ring_divisions')

        # Deleting model 'Trainer'
        db.delete_table('horseshow_trainer')

        # Removing M2M table for field riders on 'Trainer'
        db.delete_table('horseshow_trainer_riders')

        # Deleting model 'Rider'
        db.delete_table('horseshow_rider')

        # Deleting model 'Division'
        db.delete_table('horseshow_division')

        # Removing M2M table for field riders on 'Division'
        db.delete_table('horseshow_division_riders')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'horseshow.barn': {
            'Meta': {'object_name': 'Barn'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ownerBarn'", 'to': "orm['auth.User']"}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'riderBarn'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'trainers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'trainerBarn'", 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'horseshow.division': {
            'Meta': {'object_name': 'Division'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'judge': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Rider']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'horseshow.horse': {
            'Meta': {'object_name': 'Horse'},
            'height': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'horseshow.horseshow': {
            'Meta': {'object_name': 'HorseShow'},
            'admin': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'dateEnd': ('django.db.models.fields.DateField', [], {}),
            'dateStart': ('django.db.models.fields.DateField', [], {}),
            'horseShowDays': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.HorseShowDay']", 'symmetrical': 'False'}),
            'hostingBarn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Barn']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'travelTime': ('django.db.models.fields.IntegerField', [], {})
        },
        'horseshow.horseshowday': {
            'Meta': {'object_name': 'HorseShowDay'},
            'day': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rings': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Ring']", 'symmetrical': 'False'}),
            'startTime': ('django.db.models.fields.TimeField', [], {}),
            'trainers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Trainer']", 'symmetrical': 'False'})
        },
        'horseshow.rider': {
            'Meta': {'object_name': 'Rider'},
            'details': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Horse']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'horseshow.ring': {
            'Meta': {'object_name': 'Ring'},
            'divisions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Division']", 'symmetrical': 'False'}),
            'eventLength': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'horseshow.trainer': {
            'Meta': {'object_name': 'Trainer'},
            'barn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Barn']"}),
            'details': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Rider']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['horseshow']