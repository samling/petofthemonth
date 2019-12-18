import {DefaultCrudRepository} from '@loopback/repository';
import {Point, PointRelations} from '../models';
import {MariadbDataSource} from '../datasources';
import {inject} from '@loopback/core';

export class PointRepository extends DefaultCrudRepository<
  Point,
  typeof Point.prototype.id,
  PointRelations
> {
  constructor(
    @inject('datasources.mariadb') dataSource: MariadbDataSource,
  ) {
    super(Point, dataSource);
  }
}
