# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Schedule'
        db.create_table('scheduler_schedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('breakLength', self.gf('django.db.models.fields.IntegerField')()),
            ('ring', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horseshow.Ring'], unique=True)),
        ))
        db.send_create_signal('scheduler', ['Schedule'])

        # Adding M2M table for field timeSlots on 'Schedule'
        db.create_table('scheduler_schedule_timeSlots', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('schedule', models.ForeignKey(orm['scheduler.schedule'], null=False)),
            ('timeslot', models.ForeignKey(orm['scheduler.timeslot'], null=False))
        ))
        db.create_unique('scheduler_schedule_timeSlots', ['schedule_id', 'timeslot_id'])

        # Adding model 'TimeSlot'
        db.create_table('scheduler_timeslot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('startTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('endTime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('scheduler', ['TimeSlot'])

        # Adding M2M table for field riders on 'TimeSlot'
        db.create_table('scheduler_timeslot_riders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('timeslot', models.ForeignKey(orm['scheduler.timeslot'], null=False)),
            ('rider', models.ForeignKey(orm['horseshow.rider'], null=False))
        ))
        db.create_unique('scheduler_timeslot_riders', ['timeslot_id', 'rider_id'])


    def backwards(self, orm):
        # Deleting model 'Schedule'
        db.delete_table('scheduler_schedule')

        # Removing M2M table for field timeSlots on 'Schedule'
        db.delete_table('scheduler_schedule_timeSlots')

        # Deleting model 'TimeSlot'
        db.delete_table('scheduler_timeslot')

        # Removing M2M table for field riders on 'TimeSlot'
        db.delete_table('scheduler_timeslot_riders')


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
        'scheduler.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'breakLength': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'ring': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horseshow.Ring']", 'unique': 'True'}),
            'timeSlots': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scheduler.TimeSlot']", 'symmetrical': 'False'})
        },
        'scheduler.timeslot': {
            'Meta': {'object_name': 'TimeSlot'},
            'endTime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Rider']", 'symmetrical': 'False'}),
            'startTime': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['scheduler']