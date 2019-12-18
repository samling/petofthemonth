import {DefaultCrudRepository} from '@loopback/repository';
import {Group, GroupRelations} from '../models';
import {MariadbDataSource} from '../datasources';
import {inject} from '@loopback/core';

export class GroupRepository extends DefaultCrudRepository<
  Group,
  typeof Group.prototype.id,
  GroupRelations
> {
  constructor(
    @inject('datasources.mariadb') dataSource: MariadbDataSource,
  ) {
    super(Group, dataSource);
  }
}
