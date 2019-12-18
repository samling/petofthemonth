import {DefaultCrudRepository, repository, HasManyRepositoryFactory} from '@loopback/repository';
import {Group, GroupRelations, Pet} from '../models';
import {MariadbDataSource} from '../datasources';
import {inject, Getter} from '@loopback/core';
import {PetRepository} from './pet.repository';

export class GroupRepository extends DefaultCrudRepository<
  Group,
  typeof Group.prototype.id,
  GroupRelations
> {

  public readonly pets: HasManyRepositoryFactory<Pet, typeof Group.prototype.id>;

  constructor(
    @inject('datasources.mariadb') dataSource: MariadbDataSource, @repository.getter('PetRepository') protected petRepositoryGetter: Getter<PetRepository>,
  ) {
    super(Group, dataSource);
    this.pets = this.createHasManyRepositoryFactoryFor('pets', petRepositoryGetter,);
    this.registerInclusionResolver('pets', this.pets.inclusionResolver);
  }
}
