import {Entity, model, property, belongsTo, hasMany} from '@loopback/repository';
import {Group} from './group.model';
import {Point} from './point.model';

@model()
export class Pet extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  id?: number;

  @property({
    type: 'string',
    required: true,
  })
  name: string;

  @property({
    type: 'string',
  })
  description?: string;

  @property({
    type: 'number',
  })
  age?: number;

  @property({
    type: 'string',
  })
  image?: string;

  @belongsTo(() => Group)
  groupId: number;

  @hasMany(() => Point)
  points: Point[];

  constructor(data?: Partial<Pet>) {
    super(data);
  }
}

export interface PetRelations {
  // describe navigational properties here
}

export type PetWithRelations = Pet & PetRelations;
