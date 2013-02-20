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
            ('fences_division', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('flat_division', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('horseshow', ['Profile'])

        # Adding model 'HorseShow'
        db.create_table('horseshow_horseshow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 20, 0, 0))),
            ('hosting_team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Team'], null=True)),
            ('maxriders', self.gf('django.db.models.fields.IntegerField')(default=15)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Region'], null=True)),
            ('barn', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('horseshow', ['HorseShow'])

        # Adding M2M table for field admin on 'HorseShow'
        db.create_table('horseshow_horseshow_admin', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshow', models.ForeignKey(orm['horseshow.horseshow'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_horseshow_admin', ['horseshow_id', 'user_id'])

        # Adding M2M table for field classes on 'HorseShow'
        db.create_table('horseshow_horseshow_classes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshow', models.ForeignKey(orm['horseshow.horseshow'], null=False)),
            ('class', models.ForeignKey(orm['horseshow.class'], null=False))
        ))
        db.create_unique('horseshow_horseshow_classes', ['horseshow_id', 'class_id'])

        # Adding M2M table for field teams on 'HorseShow'
        db.create_table('horseshow_horseshow_teams', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshow', models.ForeignKey(orm['horseshow.horseshow'], null=False)),
            ('showteam', models.ForeignKey(orm['horseshow.showteam'], null=False))
        ))
        db.create_unique('horseshow_horseshow_teams', ['horseshow_id', 'showteam_id'])

        # Adding model 'Zone'
        db.create_table('horseshow_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('admin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
        ))
        db.send_create_signal('horseshow', ['Zone'])

        # Adding model 'Region'
        db.create_table('horseshow_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('admin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Zone'], null=True)),
        ))
        db.send_create_signal('horseshow', ['Region'])

        # Adding model 'Team'
        db.create_table('horseshow_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Region'], null=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('horseshow', ['Team'])

        # Adding M2M table for field captains on 'Team'
        db.create_table('horseshow_team_captains', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['horseshow.team'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_team_captains', ['team_id', 'user_id'])

        # Adding M2M table for field trainers on 'Team'
        db.create_table('horseshow_team_trainers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['horseshow.team'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_team_trainers', ['team_id', 'user_id'])

        # Adding M2M table for field riders on 'Team'
        db.create_table('horseshow_team_riders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['horseshow.team'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_team_riders', ['team_id', 'user_id'])

        # Adding model 'Horse'
        db.create_table('horseshow_horse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('height', self.gf('django.db.models.fields.CharField')(default='', max_length=5)),
            ('weight', self.gf('django.db.models.fields.CharField')(default='1000', max_length=10)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='gelding', max_length=20)),
        ))
        db.send_create_signal('horseshow', ['Horse'])

        # Adding model 'Rider'
        db.create_table('horseshow_rider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('showteam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.ShowTeam'])),
            ('horse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Horse'])),
            ('place', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('pointed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('class_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('horseshow', ['Rider'])

        # Adding model 'ShowTeam'
        db.create_table('horseshow_showteam', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Team'])),
        ))
        db.send_create_signal('horseshow', ['ShowTeam'])

        # Adding M2M table for field trainers on 'ShowTeam'
        db.create_table('horseshow_showteam_trainers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('showteam', models.ForeignKey(orm['horseshow.showteam'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_showteam_trainers', ['showteam_id', 'user_id'])

        # Adding model 'Class'
        db.create_table('horseshow_class', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('judge', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('division', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('eventLength', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('horseshow', ['Class'])

        # Adding M2M table for field riders on 'Class'
        db.create_table('horseshow_class_riders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['horseshow.class'], null=False)),
            ('rider', models.ForeignKey(orm['horseshow.rider'], null=False))
        ))
        db.create_unique('horseshow_class_riders', ['class_id', 'rider_id'])

        # Adding model 'Membership'
        db.create_table('horseshow_membership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('horse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Horse'])),
            ('event_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Class'])),
            ('alternate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('able', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('height_limit', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('weight_limit', self.gf('django.db.models.fields.IntegerField')(default=300)),
        ))
        db.send_create_signal('horseshow', ['Membership'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('horseshow_profile')

        # Deleting model 'HorseShow'
        db.delete_table('horseshow_horseshow')

        # Removing M2M table for field admin on 'HorseShow'
        db.delete_table('horseshow_horseshow_admin')

        # Removing M2M table for field classes on 'HorseShow'
        db.delete_table('horseshow_horseshow_classes')

        # Removing M2M table for field teams on 'HorseShow'
        db.delete_table('horseshow_horseshow_teams')

        # Deleting model 'Zone'
        db.delete_table('horseshow_zone')

        # Deleting model 'Region'
        db.delete_table('horseshow_region')

        # Deleting model 'Team'
        db.delete_table('horseshow_team')

        # Removing M2M table for field captains on 'Team'
        db.delete_table('horseshow_team_captains')

        # Removing M2M table for field trainers on 'Team'
        db.delete_table('horseshow_team_trainers')

        # Removing M2M table for field riders on 'Team'
        db.delete_table('horseshow_team_riders')

        # Deleting model 'Horse'
        db.delete_table('horseshow_horse')

        # Deleting model 'Rider'
        db.delete_table('horseshow_rider')

        # Deleting model 'ShowTeam'
        db.delete_table('horseshow_showteam')

        # Removing M2M table for field trainers on 'ShowTeam'
        db.delete_table('horseshow_showteam_trainers')

        # Deleting model 'Class'
        db.delete_table('horseshow_class')

        # Removing M2M table for field riders on 'Class'
        db.delete_table('horseshow_class_riders')

        # Deleting model 'Membership'
        db.delete_table('horseshow_membership')


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
        'horseshow.class': {
            'Meta': {'object_name': 'Class'},
            'division': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
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
            'barn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Class']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 20, 0, 0)'}),
            'hosting_team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Team']", 'null': 'True'}),
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
            'event_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Class']"}),
            'height_limit': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Horse']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight_limit': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        'horseshow.profile': {
            'Meta': {'object_name': 'Profile'},
            'fences_division': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'flat_division': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_region_director': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_rider': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_trainer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_zone_director': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'class_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Horse']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'pointed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'showteam': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.ShowTeam']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'horseshow.showteam': {
            'Meta': {'object_name': 'ShowTeam'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'show_team_riders'", 'symmetrical': 'False', 'through': "orm['horseshow.Rider']", 'to': "orm['auth.User']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Team']"}),
            'trainers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'show_team_trainers'", 'symmetrical': 'False', 'to': "orm['auth.User']"})
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