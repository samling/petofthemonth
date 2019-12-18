import {
  Count,
  CountSchema,
  Filter,
  repository,
  Where,
} from '@loopback/repository';
import {
  del,
  get,
  getModelSchemaRef,
  getWhereSchemaFor,
  param,
  patch,
  post,
  requestBody,
} from '@loopback/rest';
import {
  Pet,
  Point,
} from '../models';
import {PetRepository} from '../repositories';

export class PetPointController {
  constructor(
    @repository(PetRepository) protected petRepository: PetRepository,
  ) { }

  @get('/pets/{id}/points', {
    responses: {
      '200': {
        description: 'Array of Point\'s belonging to Pet',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Point)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<Point>,
  ): Promise<Point[]> {
    return this.petRepository.points(id).find(filter);
  }

  @post('/pets/{id}/points', {
    responses: {
      '200': {
        description: 'Pet model instance',
        content: {'application/json': {schema: getModelSchemaRef(Point)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Pet.prototype.id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Point, {
            title: 'NewPointInPet',
            exclude: ['id'],
            optional: ['petId']
          }),
        },
      },
    }) point: Omit<Point, 'id'>,
  ): Promise<Point> {
    return this.petRepository.points(id).create(point);
  }

  @patch('/pets/{id}/points', {
    responses: {
      '200': {
        description: 'Pet.Point PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Point, {partial: true}),
        },
      },
    })
    point: Partial<Point>,
    @param.query.object('where', getWhereSchemaFor(Point)) where?: Where<Point>,
  ): Promise<Count> {
    return this.petRepository.points(id).patch(point, where);
  }

  @del('/pets/{id}/points', {
    responses: {
      '200': {
        description: 'Pet.Point DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(Point)) where?: Where<Point>,
  ): Promise<Count> {
    return this.petRepository.points(id).delete(where);
  }
}
