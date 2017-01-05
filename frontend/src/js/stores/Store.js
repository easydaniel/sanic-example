import { createStore, compose, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'
import promiseMiddleware from 'redux-promise'
import rootReducer from '../reducers'
import DevTools from '../components/DevTools'

function configureStore () {
    const middleware = [thunk, promiseMiddleware]

    const finalCreateStore = compose(
        applyMiddleware(...middleware),
        DevTools.instrument(),
        window.devToolsExtensio ? window.devToolsExtension() : f => f
    )(createStore)

    const store = finalCreateStore(rootReducer)

    if (module.hot) {
        module.hot.accept('../reducers', () => {
            const nextRootReducer = require('../reducers')
            store.replaceReducer(nextRootReducer)
        })
    }

    return store
}

export default configureStore()
