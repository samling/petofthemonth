import {DefaultCrudRepository} from '@loopback/repository';
import {Pet, PetRelations} from '../models';
import {MariadbDataSource} from '../datasources';
import {inject} from '@loopback/core';

export class PetRepository extends DefaultCrudRepository<
  Pet,
  typeof Pet.prototype.id,
  PetRelations
> {
  constructor(
    @inject('datasources.mariadb') dataSource: MariadbDataSource,
  ) {
    super(Pet, dataSource);
  }
}
