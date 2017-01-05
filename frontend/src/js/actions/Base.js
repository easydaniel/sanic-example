import { createAction } from 'redux-actions'
import { Login } from '../api/Requests'

export const action = createAction('ACTION')

export const login = createAction('LOGIN', Login)
