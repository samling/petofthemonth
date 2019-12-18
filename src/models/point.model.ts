import {Entity, model, property, belongsTo} from '@loopback/repository';
import {Pet} from './pet.model';

@model()
export class Point extends Entity {
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
  description: string;

  @property({
    type: 'date',
    required: true,
  })
  date: string;

  @belongsTo(() => Pet)
  petId: number;

  constructor(data?: Partial<Point>) {
    super(data);
  }
}

export interface PointRelations {
  // describe navigational properties here
}

export type PointWithRelations = Point & PointRelations;
