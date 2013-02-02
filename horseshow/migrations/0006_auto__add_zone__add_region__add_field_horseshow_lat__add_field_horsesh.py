# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Zone'
        db.create_table('horseshow_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('horseshow', ['Zone'])

        # Adding M2M table for field regions on 'Zone'
        db.create_table('horseshow_zone_regions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('zone', models.ForeignKey(orm['horseshow.zone'], null=False)),
            ('region', models.ForeignKey(orm['horseshow.region'], null=False))
        ))
        db.create_unique('horseshow_zone_regions', ['zone_id', 'region_id'])

        # Adding M2M table for field admin on 'Zone'
        db.create_table('horseshow_zone_admin', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('zone', models.ForeignKey(orm['horseshow.zone'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_zone_admin', ['zone_id', 'user_id'])

        # Adding model 'Region'
        db.create_table('horseshow_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('horseshow', ['Region'])

        # Adding M2M table for field teams on 'Region'
        db.create_table('horseshow_region_teams', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('region', models.ForeignKey(orm['horseshow.region'], null=False)),
            ('team', models.ForeignKey(orm['horseshow.team'], null=False))
        ))
        db.create_unique('horseshow_region_teams', ['region_id', 'team_id'])

        # Adding M2M table for field admin on 'Region'
        db.create_table('horseshow_region_admin', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('region', models.ForeignKey(orm['horseshow.region'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_region_admin', ['region_id', 'user_id'])

        # Adding field 'HorseShow.lat'
        db.add_column('horseshow_horseshow', 'lat',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HorseShow.lng'
        db.add_column('horseshow_horseshow', 'lng',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HorseShow.maxriders'
        db.add_column('horseshow_horseshow', 'maxriders',
                      self.gf('django.db.models.fields.IntegerField')(default=15),
                      keep_default=False)

        # Deleting field 'Rider.division'
        db.delete_column('horseshow_rider', 'division_id')

        # Deleting field 'Horse.height_limit'
        db.delete_column('horseshow_horse', 'height_limit')

        # Deleting field 'Horse.weight_limit'
        db.delete_column('horseshow_horse', 'weight_limit')

        # Adding M2M table for field riders on 'Division'
        db.create_table('horseshow_division_riders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('division', models.ForeignKey(orm['horseshow.division'], null=False)),
            ('rider', models.ForeignKey(orm['horseshow.rider'], null=False))
        ))
        db.create_unique('horseshow_division_riders', ['division_id', 'rider_id'])

        # Adding field 'Membership.height_limit'
        db.add_column('horseshow_membership', 'height_limit',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'Membership.weight_limit'
        db.add_column('horseshow_membership', 'weight_limit',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'Team.lat'
        db.add_column('horseshow_team', 'lat',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Team.lng'
        db.add_column('horseshow_team', 'lng',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Zone'
        db.delete_table('horseshow_zone')

        # Removing M2M table for field regions on 'Zone'
        db.delete_table('horseshow_zone_regions')

        # Removing M2M table for field admin on 'Zone'
        db.delete_table('horseshow_zone_admin')

        # Deleting model 'Region'
        db.delete_table('horseshow_region')

        # Removing M2M table for field teams on 'Region'
        db.delete_table('horseshow_region_teams')

        # Removing M2M table for field admin on 'Region'
        db.delete_table('horseshow_region_admin')

        # Deleting field 'HorseShow.lat'
        db.delete_column('horseshow_horseshow', 'lat')

        # Deleting field 'HorseShow.lng'
        db.delete_column('horseshow_horseshow', 'lng')

        # Deleting field 'HorseShow.maxriders'
        db.delete_column('horseshow_horseshow', 'maxriders')

        # Adding field 'Rider.division'
        db.add_column('horseshow_rider', 'division',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Division'], null=True),
                      keep_default=False)

        # Adding field 'Horse.height_limit'
        db.add_column('horseshow_horse', 'height_limit',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'Horse.weight_limit'
        db.add_column('horseshow_horse', 'weight_limit',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Removing M2M table for field riders on 'Division'
        db.delete_table('horseshow_division_riders')

        # Deleting field 'Membership.height_limit'
        db.delete_column('horseshow_membership', 'height_limit')

        # Deleting field 'Membership.weight_limit'
        db.delete_column('horseshow_membership', 'weight_limit')

        # Deleting field 'Team.lat'
        db.delete_column('horseshow_team', 'lat')

        # Deleting field 'Team.lng'
        db.delete_column('horseshow_team', 'lng')


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
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 31, 0, 0)'}),
            'divisions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Division']", 'symmetrical': 'False'}),
            'hostingTeam': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Team']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'maxriders': ('django.db.models.fields.IntegerField', [], {'default': '15'}),
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
        'horseshow.region': {
            'Meta': {'object_name': 'Region'},
            'admin': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Team']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'riderTeam'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'trainers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'trainerTeam'", 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'horseshow.zone': {
            'Meta': {'object_name': 'Zone'},
            'admin': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'regions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Region']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['horseshow']