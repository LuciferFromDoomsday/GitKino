from django.contrib import admin

from movies.models import Movie, Comment, Cities , Cinema , Ticket, Sessions


admin.site.register(Movie)
admin.site.register(Comment)

admin.site.register(Cities)
admin.site.register(Cinema)
admin.site.register(Ticket)
admin.site.register(Sessions)

