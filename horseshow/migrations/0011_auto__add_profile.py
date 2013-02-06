# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table('horseshow_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('is_rider', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_trainer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_region_director', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_zone_director', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('horseshow', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('horseshow_profile')


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
            'eventLength': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'horses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Horse']", 'through': "orm['horseshow.Membership']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'judge': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Rider']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'horseshow.horse': {
            'Meta': {'object_name': 'Horse'},
            'gender': ('django.db.models.fields.CharField', [], {'default': "'gelding'", 'max_length': '20'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'weight': ('django.db.models.fields.CharField', [], {'default': "'1000'", 'max_length': '10'})
        },
        'horseshow.horseshow': {
            'Meta': {'object_name': 'HorseShow'},
            'admin': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 6, 0, 0)'}),
            'divisions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Division']", 'symmetrical': 'False'}),
            'hostingTeam': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Team']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'maxriders': ('django.db.models.fields.IntegerField', [], {'default': '15'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Region']", 'null': 'True'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.ShowTeam']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'horseshow.membership': {
            'Meta': {'object_name': 'Membership'},
            'able': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alternate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Division']"}),
            'height_limit': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Horse']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight_limit': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        'horseshow.profile': {
            'Meta': {'object_name': 'Profile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_region_director': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_rider': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_trainer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_zone_director': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'horseshow.region': {
            'Meta': {'object_name': 'Region'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Zone']", 'null': 'True'})
        },
        'horseshow.rider': {
            'Meta': {'object_name': 'Rider'},
            'details': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Horse']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'pointed': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'horseshow.showteam': {
            'Meta': {'object_name': 'ShowTeam'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Rider']", 'symmetrical': 'False'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Team']"}),
            'trainers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
        },
        'horseshow.team': {
            'Meta': {'object_name': 'Team'},
            'captains': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'captainTeam'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Region']", 'null': 'True'}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'riderTeam'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'trainers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'trainerTeam'", 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'horseshow.zone': {
            'Meta': {'object_name': 'Zone'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['horseshow']