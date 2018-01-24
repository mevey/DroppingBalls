from cw.models import *
from django.contrib import admin

class VotesAdmin(admin.ModelAdmin):
	list_display = ('nairobi', 'athens', 'bangkok', 'reykjavik','total')

admin.site.register(Votes, VotesAdmin)