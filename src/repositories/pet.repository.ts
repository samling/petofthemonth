import {DefaultCrudRepository, repository, BelongsToAccessor, HasManyRepositoryFactory} from '@loopback/repository';
import {Pet, PetRelations, Group, Point} from '../models';
import {MariadbDataSource} from '../datasources';
import {inject, Getter} from '@loopback/core';
import {GroupRepository} from './group.repository';
import {PointRepository} from './point.repository';

export class PetRepository extends DefaultCrudRepository<
  Pet,
  typeof Pet.prototype.id,
  PetRelations
> {

  public readonly group: BelongsToAccessor<Group, typeof Pet.prototype.id>;

  public readonly points: HasManyRepositoryFactory<Point, typeof Pet.prototype.id>;

  constructor(
    @inject('datasources.mariadb') dataSource: MariadbDataSource, @repository.getter('GroupRepository') protected groupRepositoryGetter: Getter<GroupRepository>, @repository.getter('PointRepository') protected pointRepositoryGetter: Getter<PointRepository>,
  ) {
    super(Pet, dataSource);
    this.points = this.createHasManyRepositoryFactoryFor('points', pointRepositoryGetter,);
    this.registerInclusionResolver('points', this.points.inclusionResolver);
    this.group = this.createBelongsToAccessorFor('group', groupRepositoryGetter,);
    this.registerInclusionResolver('group', this.group.inclusionResolver);
  }
}
