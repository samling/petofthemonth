import { createStore } from "vuex";

import pets from './modules/pets'

export default createStore({
    modules: {
        pets,
    }
});