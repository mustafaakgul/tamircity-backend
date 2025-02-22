from django.contrib import admin
from .models import ExpertiseTV, ExpertiseWatch, ExpertiseConsole, ExpertisePhone, ExpertisePc


@admin.register(ExpertiseTV)
class ExpertiseTVdAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExpertiseTV._meta.fields]
    list_display_links = ["reservation"]
    search_fields = ["reservation"]
    list_filter = ["created_date"]

    class Meta:
        model = ExpertiseTV


@admin.register(ExpertiseWatch)
class ExpertiseWatchAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExpertiseWatch._meta.fields]
    list_display_links = ["reservation"]
    search_fields = ["reservation"]
    list_filter = ["created_date"]

    class Meta:
        model = ExpertiseWatch


@admin.register(ExpertiseConsole)
class ExpertiseConsoledAdmin(admin.ModelAdmin):
     list_display = [field.name for field in ExpertiseConsole._meta.fields]
     list_display_links = ["reservation"]
     search_fields = ["reservation"]
     list_filter = ["created_date"]

     class Meta:
         model = ExpertiseConsole

@admin.register(ExpertisePhone)
class ExpertisePhoneAdmin(admin.ModelAdmin):
     list_display = [field.name for field in ExpertisePhone._meta.fields]
     list_display_links = ["reservation"]
     search_fields = ["reservation"]
     list_filter = ["created_date"]

     class Meta:
         model = ExpertisePhone


@admin.register(ExpertisePc)
class ExpertisePcAdmin(admin.ModelAdmin):
     list_display = [field.name for field in ExpertisePc._meta.fields]
     list_display_links = ["reservation"]
     search_fields = ["reservation"]
     list_filter = ["created_date"]

     class Meta:
         model = ExpertisePc
