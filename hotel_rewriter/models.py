from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=[
        ('country', 'Country'),
        ('state', 'State'),
        ('city', 'City'),
    ])
    latitude = models.FloatField()
    longitude = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'admin_panel_location'


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'admin_panel_amenity'


class Property(models.Model):
    property_id = models.IntegerField()
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    locations = models.ManyToManyField(Location, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'admin_panel_property'


class PropertySummary(models.Model):
    property = models.OneToOneField(
        Property, on_delete=models.CASCADE, related_name='summary')
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hotel_rewriter_propertysummary'

    def __str__(self):
        return f"Summary for {self.property.title}"
