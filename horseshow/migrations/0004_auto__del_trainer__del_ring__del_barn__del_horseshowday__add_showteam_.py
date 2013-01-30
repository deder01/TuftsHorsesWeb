# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Trainer'
        db.delete_table('horseshow_trainer')

        # Removing M2M table for field riders on 'Trainer'
        db.delete_table('horseshow_trainer_riders')

        # Deleting model 'Ring'
        db.delete_table('horseshow_ring')

        # Removing M2M table for field divisions on 'Ring'
        db.delete_table('horseshow_ring_divisions')

        # Deleting model 'Barn'
        db.delete_table('horseshow_barn')

        # Removing M2M table for field trainers on 'Barn'
        db.delete_table('horseshow_barn_trainers')

        # Removing M2M table for field riders on 'Barn'
        db.delete_table('horseshow_barn_riders')

        # Deleting model 'HorseShowDay'
        db.delete_table('horseshow_horseshowday')

        # Removing M2M table for field rings on 'HorseShowDay'
        db.delete_table('horseshow_horseshowday_rings')

        # Removing M2M table for field trainers on 'HorseShowDay'
        db.delete_table('horseshow_horseshowday_trainers')

        # Adding model 'ShowTeam'
        db.create_table('horseshow_showteam', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Team'])),
        ))
        db.send_create_signal('horseshow', ['ShowTeam'])

        # Adding M2M table for field riders on 'ShowTeam'
        db.create_table('horseshow_showteam_riders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('showteam', models.ForeignKey(orm['horseshow.showteam'], null=False)),
            ('rider', models.ForeignKey(orm['horseshow.rider'], null=False))
        ))
        db.create_unique('horseshow_showteam_riders', ['showteam_id', 'rider_id'])

        # Adding M2M table for field trainers on 'ShowTeam'
        db.create_table('horseshow_showteam_trainers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('showteam', models.ForeignKey(orm['horseshow.showteam'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horseshow_showteam_trainers', ['showteam_id', 'user_id'])

        # Adding model 'Membership'
        db.create_table('horseshow_membership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('horse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Horse'])),
            ('division', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Division'])),
            ('alternate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('able', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('horseshow', ['Membership'])

        # Adding model 'Team'
        db.create_table('horseshow_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=100)),
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

        # Deleting field 'HorseShow.travelTime'
        db.delete_column('horseshow_horseshow', 'travelTime')

        # Deleting field 'HorseShow.dateStart'
        db.delete_column('horseshow_horseshow', 'dateStart')

        # Deleting field 'HorseShow.dateEnd'
        db.delete_column('horseshow_horseshow', 'dateEnd')

        # Deleting field 'HorseShow.hostingBarn'
        db.delete_column('horseshow_horseshow', 'hostingBarn_id')

        # Adding field 'HorseShow.date'
        db.add_column('horseshow_horseshow', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 30, 0, 0)),
                      keep_default=False)

        # Adding field 'HorseShow.hostingTeam'
        db.add_column('horseshow_horseshow', 'hostingTeam',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Team'], null=True),
                      keep_default=False)

        # Removing M2M table for field horseShowDays on 'HorseShow'
        db.delete_table('horseshow_horseshow_horseShowDays')

        # Adding M2M table for field divisions on 'HorseShow'
        db.create_table('horseshow_horseshow_divisions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshow', models.ForeignKey(orm['horseshow.horseshow'], null=False)),
            ('division', models.ForeignKey(orm['horseshow.division'], null=False))
        ))
        db.create_unique('horseshow_horseshow_divisions', ['horseshow_id', 'division_id'])

        # Adding M2M table for field teams on 'HorseShow'
        db.create_table('horseshow_horseshow_teams', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshow', models.ForeignKey(orm['horseshow.horseshow'], null=False)),
            ('showteam', models.ForeignKey(orm['horseshow.showteam'], null=False))
        ))
        db.create_unique('horseshow_horseshow_teams', ['horseshow_id', 'showteam_id'])

        # Adding field 'Rider.division'
        db.add_column('horseshow_rider', 'division',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horseshow.Division'], null=True),
                      keep_default=False)

        # Adding field 'Rider.place'
        db.add_column('horseshow_rider', 'place',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Deleting field 'Horse.wins'
        db.delete_column('horseshow_horse', 'wins')

        # Deleting field 'Horse.losses'
        db.delete_column('horseshow_horse', 'losses')

        # Adding field 'Horse.weight'
        db.add_column('horseshow_horse', 'weight',
                      self.gf('django.db.models.fields.CharField')(default='1000', max_length=10),
                      keep_default=False)

        # Adding field 'Horse.gender'
        db.add_column('horseshow_horse', 'gender',
                      self.gf('django.db.models.fields.CharField')(default='gelding', max_length=20),
                      keep_default=False)

        # Adding field 'Horse.height_limit'
        db.add_column('horseshow_horse', 'height_limit',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'Horse.weight_limit'
        db.add_column('horseshow_horse', 'weight_limit',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'Division.order'
        db.add_column('horseshow_division', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Division.eventLength'
        db.add_column('horseshow_division', 'eventLength',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)

        # Removing M2M table for field riders on 'Division'
        db.delete_table('horseshow_division_riders')


    def backwards(self, orm):
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

        # Adding model 'Ring'
        db.create_table('horseshow_ring', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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

        # Adding model 'Barn'
        db.create_table('horseshow_barn', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ownerBarn', to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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

        # Adding model 'HorseShowDay'
        db.create_table('horseshow_horseshowday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('startTime', self.gf('django.db.models.fields.TimeField')()),
            ('day', self.gf('django.db.models.fields.IntegerField')(default=1)),
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

        # Deleting model 'ShowTeam'
        db.delete_table('horseshow_showteam')

        # Removing M2M table for field riders on 'ShowTeam'
        db.delete_table('horseshow_showteam_riders')

        # Removing M2M table for field trainers on 'ShowTeam'
        db.delete_table('horseshow_showteam_trainers')

        # Deleting model 'Membership'
        db.delete_table('horseshow_membership')

        # Deleting model 'Team'
        db.delete_table('horseshow_team')

        # Removing M2M table for field captains on 'Team'
        db.delete_table('horseshow_team_captains')

        # Removing M2M table for field trainers on 'Team'
        db.delete_table('horseshow_team_trainers')

        # Removing M2M table for field riders on 'Team'
        db.delete_table('horseshow_team_riders')


        # User chose to not deal with backwards NULL issues for 'HorseShow.travelTime'
        raise RuntimeError("Cannot reverse this migration. 'HorseShow.travelTime' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'HorseShow.dateStart'
        raise RuntimeError("Cannot reverse this migration. 'HorseShow.dateStart' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'HorseShow.dateEnd'
        raise RuntimeError("Cannot reverse this migration. 'HorseShow.dateEnd' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'HorseShow.hostingBarn'
        raise RuntimeError("Cannot reverse this migration. 'HorseShow.hostingBarn' and its values cannot be restored.")
        # Deleting field 'HorseShow.date'
        db.delete_column('horseshow_horseshow', 'date')

        # Deleting field 'HorseShow.hostingTeam'
        db.delete_column('horseshow_horseshow', 'hostingTeam_id')

        # Adding M2M table for field horseShowDays on 'HorseShow'
        db.create_table('horseshow_horseshow_horseShowDays', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('horseshow', models.ForeignKey(orm['horseshow.horseshow'], null=False)),
            ('horseshowday', models.ForeignKey(orm['horseshow.horseshowday'], null=False))
        ))
        db.create_unique('horseshow_horseshow_horseShowDays', ['horseshow_id', 'horseshowday_id'])

        # Removing M2M table for field divisions on 'HorseShow'
        db.delete_table('horseshow_horseshow_divisions')

        # Removing M2M table for field teams on 'HorseShow'
        db.delete_table('horseshow_horseshow_teams')

        # Deleting field 'Rider.division'
        db.delete_column('horseshow_rider', 'division_id')

        # Deleting field 'Rider.place'
        db.delete_column('horseshow_rider', 'place')

        # Adding field 'Horse.wins'
        db.add_column('horseshow_horse', 'wins',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Horse.losses'
        db.add_column('horseshow_horse', 'losses',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Horse.weight'
        db.delete_column('horseshow_horse', 'weight')

        # Deleting field 'Horse.gender'
        db.delete_column('horseshow_horse', 'gender')

        # Deleting field 'Horse.height_limit'
        db.delete_column('horseshow_horse', 'height_limit')

        # Deleting field 'Horse.weight_limit'
        db.delete_column('horseshow_horse', 'weight_limit')

        # Deleting field 'Division.order'
        db.delete_column('horseshow_division', 'order')

        # Deleting field 'Division.eventLength'
        db.delete_column('horseshow_division', 'eventLength')

        # Adding M2M table for field riders on 'Division'
        db.create_table('horseshow_division_riders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('division', models.ForeignKey(orm['horseshow.division'], null=False)),
            ('rider', models.ForeignKey(orm['horseshow.rider'], null=False))
        ))
        db.create_unique('horseshow_division_riders', ['division_id', 'rider_id'])


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'horseshow.horse': {
            'Meta': {'object_name': 'Horse'},
            'gender': ('django.db.models.fields.CharField', [], {'default': "'gelding'", 'max_length': '20'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5'}),
            'height_limit': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'weight': ('django.db.models.fields.CharField', [], {'default': "'1000'", 'max_length': '10'}),
            'weight_limit': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        'horseshow.horseshow': {
            'Meta': {'object_name': 'HorseShow'},
            'admin': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 30, 0, 0)'}),
            'divisions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.Division']", 'symmetrical': 'False'}),
            'hostingTeam': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Team']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horseshow.ShowTeam']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'horseshow.membership': {
            'Meta': {'object_name': 'Membership'},
            'able': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alternate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Division']"}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Horse']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'horseshow.rider': {
            'Meta': {'object_name': 'Rider'},
            'details': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Division']", 'null': 'True'}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horseshow.Horse']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
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
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'riderTeam'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'trainers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'trainerTeam'", 'symmetrical': 'False', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['horseshow']