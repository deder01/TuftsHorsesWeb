# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field barns on 'HorseShowDay'
        db.create_table('horseshow_horseshowday_barns', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshowday', models.ForeignKey(orm['horseshow.horseshowday'], null=False)),
            ('barn', models.ForeignKey(orm['horseshow.barn'], null=False))
        ))
        db.create_unique('horseshow_horseshowday_barns', ['horseshowday_id', 'barn_id'])


    def backwards(self, orm):
        # Removing M2M table for field barns on 'HorseShowDay'
        db.delete_table('horseshow_horseshowday_barns')


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
            'barns': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Barn']", 'symmetrical': 'False'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
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