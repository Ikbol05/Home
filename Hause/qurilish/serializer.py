from rest_framework import serializers
from . models import Region, Organizaytion, Building


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class OrganizationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    deskription = serializers.CharField()
    since = serializers.IntegerField()
    region_id = serializers.IntegerField()

    def create(self, validated_data):
        return Organizaytion.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.deskription = validated_data.get('deskription', instance.deskription)
        instance.since = validated_data.get('since', instance.since)
        instance.region = validated_data.get('region', instance.region)



class BuildingSerializer(serializers.Serializer):
    organization_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    field = serializers.IntegerField()
    floor = serializers.IntegerField()
    parkovka = serializers.BooleanField()
    playground = serializers.BooleanField()
    lift = serializers.BooleanField()

    def create(self, validated_data):
        return Building.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.organization = validated_data.get('organization', instance.organization)
        instance.region = validated_data.get('region', instance.region)
        instance.name = validated_data.get('name', instance.name)
        instance.field = validated_data.get('field', instance.field)
        instance.floor = validated_data.get('floor', instance.floor)
        instance.parkovka = validated_data.get('parkovka', instance.parkovka)
        instance.playground = validated_data.get('playground', instance.playground)
        instance.lift = validated_data.get('lift', instance.lift)