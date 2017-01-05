import React, { Component } from 'react'
import { Router, Route, IndexRoute, browserHistory } from 'react-router'
import Main from './components/Main'
import Base from './components/Base'
import NotFound from './components/NotFound'
import store from './stores/Store'
import { syncHistoryWithStore } from 'react-router-redux'

const history = syncHistoryWithStore(browserHistory, store)

export default class Root extends Component {
    render () {
        return (
            <Router history={history}>
                <Route path="/" component={Main}>
                    <IndexRoute component={Base} />
                    <Route path="*" component={NotFound} />
                </Route>
            </Router>
        )
    }
}
