from typing import TypedDict
from tortoise import fields, models

class Users(models.Model):
    id          = fields.IntField(pk=True)
    username    = fields.CharField(max_length=20, unique=True)
    email       = fields.CharField(max_length=50, unique=True)
    fullname    = fields.CharField(max_length=50, null=True)
    password    = fields.CharField(max_length=128, null=True)
    created_at  = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    is_active   = fields.BooleanField(default=True)

    pets: fields.ManyToManyRelation["Pets"] = fields.ManyToManyField("models.Pets", related_name="users", through="user_pets")

    groups: fields.ManyToManyRelation["Groups"] = fields.ManyToManyField("models.Groups", related_name="users", through="user_groups")

class Groups(models.Model):
    id          = fields.IntField(pk=True)
    name        = fields.CharField(max_length=128, null=True)
    created_at  = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    description = fields.TextField()

    users       = fields.ManyToManyRelation[Users]

    pets: fields.ManyToManyRelation["Pets"] = fields.ManyToManyField("models.Pets", related_name="groups", through="group_pets")

class Pets(models.Model):
    id          = fields.IntField(pk=True)
    name        = fields.CharField(max_length=50, null=True)
    created_at  = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    description = fields.TextField()
    age         = fields.IntField()
    height      = fields.IntField()
    weight      = fields.IntField()
    dob         = fields.DatetimeField()

    users       = fields.ManyToManyRelation[Users]

    groups      = fields.ManyToManyRelation[Groups]

class Points(models.Model):
    id          = fields.IntField(pk=True)
    created_at  = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    description = fields.TextField()
    pet         = fields.ForeignKeyField("models.Pets", related_name="points")