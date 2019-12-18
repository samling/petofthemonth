import {
  repository,
} from '@loopback/repository';
import {
  param,
  get,
  getModelSchemaRef,
} from '@loopback/rest';
import {
  Point,
  Pet,
} from '../models';
import {PointRepository} from '../repositories';

export class PointPetController {
  constructor(
    @repository(PointRepository)
    public pointRepository: PointRepository,
  ) { }

  @get('/points/{id}/pet', {
    responses: {
      '200': {
        description: 'Pet belonging to Point',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Pet)},
          },
        },
      },
    },
  })
  async getPet(
    @param.path.number('id') id: typeof Point.prototype.id,
  ): Promise<Pet> {
    return this.pointRepository.pet(id);
  }
}
