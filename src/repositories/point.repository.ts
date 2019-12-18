import {DefaultCrudRepository, repository, BelongsToAccessor} from '@loopback/repository';
import {Point, PointRelations, Pet} from '../models';
import {MariadbDataSource} from '../datasources';
import {inject, Getter} from '@loopback/core';
import {PetRepository} from './pet.repository';

export class PointRepository extends DefaultCrudRepository<
  Point,
  typeof Point.prototype.id,
  PointRelations
> {

  public readonly pet: BelongsToAccessor<Pet, typeof Point.prototype.id>;

  constructor(
    @inject('datasources.mariadb') dataSource: MariadbDataSource, @repository.getter('PetRepository') protected petRepositoryGetter: Getter<PetRepository>,
  ) {
    super(Point, dataSource);
    this.pet = this.createBelongsToAccessorFor('pet', petRepositoryGetter,);
    this.registerInclusionResolver('pet', this.pet.inclusionResolver);
  }
}
