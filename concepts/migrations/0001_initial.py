# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Card'
        db.create_table('concepts_card', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('picurl', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('concepts', ['Card'])

        # Adding model 'Player'
        db.create_table('concepts_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('concepts', ['Player'])

        # Adding M2M table for field cards on 'Player'
        db.create_table('concepts_player_cards', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['concepts.player'], null=False)),
            ('card', models.ForeignKey(orm['concepts.card'], null=False))
        ))
        db.create_unique('concepts_player_cards', ['player_id', 'card_id'])


    def backwards(self, orm):
        # Deleting model 'Card'
        db.delete_table('concepts_card')

        # Deleting model 'Player'
        db.delete_table('concepts_player')

        # Removing M2M table for field cards on 'Player'
        db.delete_table('concepts_player_cards')


    models = {
        'concepts.card': {
            'Meta': {'object_name': 'Card'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picurl': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'concepts.player': {
            'Meta': {'object_name': 'Player'},
            'cards': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['concepts.Card']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['concepts']