from django.contrib import admin

from movies.models import Movie, Comment, City , Cinema , Ticket, Session


admin.site.register(Movie)
admin.site.register(Comment)

admin.site.register(City)
admin.site.register(Cinema)
admin.site.register(Ticket)
admin.site.register(Session)

