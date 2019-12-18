import {
  repository,
} from '@loopback/repository';
import {
  param,
  get,
  getModelSchemaRef,
} from '@loopback/rest';
import {
  Pet,
  Group,
} from '../models';
import {PetRepository} from '../repositories';

export class PetGroupController {
  constructor(
    @repository(PetRepository)
    public petRepository: PetRepository,
  ) { }

  @get('/pets/{id}/group', {
    responses: {
      '200': {
        description: 'Group belonging to Pet',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Group)},
          },
        },
      },
    },
  })
  async getGroup(
    @param.path.number('id') id: typeof Pet.prototype.id,
  ): Promise<Group> {
    return this.petRepository.group(id);
  }
}
