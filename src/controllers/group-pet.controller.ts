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
  Group,
  Pet,
} from '../models';
import {GroupRepository} from '../repositories';

export class GroupPetController {
  constructor(
    @repository(GroupRepository) protected groupRepository: GroupRepository,
  ) { }

  @get('/groups/{id}/pets', {
    responses: {
      '200': {
        description: 'Array of Pet\'s belonging to Group',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Pet)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<Pet>,
  ): Promise<Pet[]> {
    return this.groupRepository.pets(id).find(filter);
  }

  @post('/groups/{id}/pets', {
    responses: {
      '200': {
        description: 'Group model instance',
        content: {'application/json': {schema: getModelSchemaRef(Pet)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Group.prototype.id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Pet, {
            title: 'NewPetInGroup',
            exclude: ['id'],
            optional: ['groupId']
          }),
        },
      },
    }) pet: Omit<Pet, 'id'>,
  ): Promise<Pet> {
    return this.groupRepository.pets(id).create(pet);
  }

  @patch('/groups/{id}/pets', {
    responses: {
      '200': {
        description: 'Group.Pet PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Pet, {partial: true}),
        },
      },
    })
    pet: Partial<Pet>,
    @param.query.object('where', getWhereSchemaFor(Pet)) where?: Where<Pet>,
  ): Promise<Count> {
    return this.groupRepository.pets(id).patch(pet, where);
  }

  @del('/groups/{id}/pets', {
    responses: {
      '200': {
        description: 'Group.Pet DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(Pet)) where?: Where<Pet>,
  ): Promise<Count> {
    return this.groupRepository.pets(id).delete(where);
  }
}
