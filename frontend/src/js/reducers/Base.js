import { handleActions } from 'redux-actions'

const initialState = {}

export default handleActions({

    LOGIN: (state, action) => {
        console.log(action.payload)
        return {
            ...state
        }
    },

    default: (state, action) => {
        return {
            ...state
        }
    }
}, initialState)
