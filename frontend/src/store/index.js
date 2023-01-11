import { createStore } from "vuex";

import pets from './modules/pets'
import points from './modules/points'
import users from './modules/users'
import groups from './modules/groups'

export default createStore({
    modules: {
        pets,
        points,
        users,
        groups
    }
});