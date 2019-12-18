import {
  Count,
  CountSchema,
  Filter,
  repository,
  Where,
} from '@loopback/repository';
import {
  post,
  param,
  get,
  getFilterSchemaFor,
  getModelSchemaRef,
  getWhereSchemaFor,
  patch,
  put,
  del,
  requestBody,
} from '@loopback/rest';
import {Point} from '../models';
import {PointRepository} from '../repositories';

export class PointControllerController {
  constructor(
    @repository(PointRepository)
    public pointRepository : PointRepository,
  ) {}

  @post('/points', {
    responses: {
      '200': {
        description: 'Point model instance',
        content: {'application/json': {schema: getModelSchemaRef(Point)}},
      },
    },
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Point, {
            title: 'NewPoint',
            exclude: ['id'],
          }),
        },
      },
    })
    point: Omit<Point, 'id'>,
  ): Promise<Point> {
    return this.pointRepository.create(point);
  }

  @get('/points/count', {
    responses: {
      '200': {
        description: 'Point model count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async count(
    @param.query.object('where', getWhereSchemaFor(Point)) where?: Where<Point>,
  ): Promise<Count> {
    return this.pointRepository.count(where);
  }

  @get('/points', {
    responses: {
      '200': {
        description: 'Array of Point model instances',
        content: {
          'application/json': {
            schema: {
              type: 'array',
              items: getModelSchemaRef(Point, {includeRelations: true}),
            },
          },
        },
      },
    },
  })
  async find(
    @param.query.object('filter', getFilterSchemaFor(Point)) filter?: Filter<Point>,
  ): Promise<Point[]> {
    return this.pointRepository.find(filter);
  }

  @patch('/points', {
    responses: {
      '200': {
        description: 'Point PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Point, {partial: true}),
        },
      },
    })
    point: Point,
    @param.query.object('where', getWhereSchemaFor(Point)) where?: Where<Point>,
  ): Promise<Count> {
    return this.pointRepository.updateAll(point, where);
  }

  @get('/points/{id}', {
    responses: {
      '200': {
        description: 'Point model instance',
        content: {
          'application/json': {
            schema: getModelSchemaRef(Point, {includeRelations: true}),
          },
        },
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.query.object('filter', getFilterSchemaFor(Point)) filter?: Filter<Point>
  ): Promise<Point> {
    return this.pointRepository.findById(id, filter);
  }

  @patch('/points/{id}', {
    responses: {
      '204': {
        description: 'Point PATCH success',
      },
    },
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Point, {partial: true}),
        },
      },
    })
    point: Point,
  ): Promise<void> {
    await this.pointRepository.updateById(id, point);
  }

  @put('/points/{id}', {
    responses: {
      '204': {
        description: 'Point PUT success',
      },
    },
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() point: Point,
  ): Promise<void> {
    await this.pointRepository.replaceById(id, point);
  }

  @del('/points/{id}', {
    responses: {
      '204': {
        description: 'Point DELETE success',
      },
    },
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.pointRepository.deleteById(id);
  }
}
