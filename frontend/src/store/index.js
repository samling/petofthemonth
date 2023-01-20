import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import VuexPersistence from 'vuex-persist'

import pets from './modules/pets'
import points from './modules/points'
import users from './modules/users'
import groups from './modules/groups'

const vuexLocal = new VuexPersistence({
    storage: window.localStorage,
    reducer: (state) => ({
        users: {
            user: state.users.user
        }
    })
})

export default createStore({
    modules: {
        pets,
        points,
        users,
        groups,
    },
    plugins: [vuexLocal.plugin]
});