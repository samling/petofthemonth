from typing import TypedDict
from tortoise import fields, models

# user_groups = Table('user_groups', Base.metadata, \
#     Column('user_id', ForeignKey('users.id'), primary_key=True), \
#     Column('group_id', ForeignKey('groups.id'), primary_key=True)
# )

# user_pets = Table('user_pets', Base.metadata, \
#     Column('user_id', ForeignKey('users.id'), primary_key=True), \
#     Column('pet_id', ForeignKey('pets.id'), primary_key=True)
# )

# group_pets = Table('group_pets', Base.metadata, \
#     Column('group_id', ForeignKey('groups.id'), primary_key=True), \
#     Column('pet_id', ForeignKey('pets.id'), primary_key=True)
# )

class Users(models.Model):
    id          = fields.IntField(pk=True)
    username    = fields.CharField(max_length=20, unique=True)
    email       = fields.CharField(max_length=50, unique=True)
    fullname    = fields.CharField(max_length=50, null=True)
    password    = fields.CharField(max_length=128, null=True)
    created_at  = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    is_active   = fields.BooleanField(default=True)

    groups: fields.ManyToManyRelation["Groups"] = fields.ManyToManyField("models.Groups", related_name="users", through="user_groups")

    # pets = relationship("Pet", secondary='user_pets', back_populates="users")

class Groups(models.Model):
    id          = fields.IntField(pk=True)
    name        = fields.CharField(max_length=128, null=True)
    created_at  = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    description = fields.TextField()

    users       = fields.ManyToManyRelation[Users]

    
    # users = relationship("User", secondary='user_groups', back_populates="groups")

    # pets = relationship("Pet", secondary='group_pets', back_populates="groups")

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

    # points = relationship("Point", back_populates="pet")
    # groups = relationship("Group", secondary='group_pets', back_populates="pets")
    # users = relationship("User", secondary='user_pets', back_populates="pets")

class Points(models.Model):
    id          = fields.IntField(pk=True)
    created_at  = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    description = fields.TextField()
    pet         = fields.ForeignKeyField("models.Pets", related_name="point")