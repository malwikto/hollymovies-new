from django.contrib.admin import ModelAdmin

class MovieAdmin(ModelAdmin):

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(queryset):
        queryset.update(description='')

    ordering = ['id']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_display_links = ['id', 'title']
    list_per_page = 10
    list_filter = ['genre']
    search_fields = ['title']
    actions = ['cleanup_description']

    fieldsets = [
        (None, {'fields': ['title', 'created']}),
        (
            'External Information',
            {
                'fields': ['genre', 'released'],
                'description': (
                    'These fields are going to be filled with data parsed '
                    'from external databases.'
                )
            }
        ),
        (
            'User Information',
            {
                'fields': ['rating', 'description'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]
    readonly_fields = ['created']

class GenreAdmin(ModelAdmin):

    @staticmethod
    def lower_name(obj):
        return obj.name.lower()

    ordering = ['id']
    list_display = ['id', 'lower_name']
    list_display_links = ['lower_name']
    search_fields = ['name']