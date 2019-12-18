import {Entity, model, property} from '@loopback/repository';

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


  constructor(data?: Partial<Point>) {
    super(data);
  }
}

export interface PointRelations {
  // describe navigational properties here
}

export type PointWithRelations = Point & PointRelations;
