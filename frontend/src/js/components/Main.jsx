import React, { Component } from 'react'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import DevTools from './DevTools'

class Main extends Component {

    render () {
        return (
            <div>
              { this.props.children }
              { process.env.NODE_ENV !== 'production' ? <DevTools/> : null }
            </div>
        )
    }
}

const mapStateToProps = (state) => ({
})

const mapDispatchToProps = (dispatch) => bindActionCreators({}, dispatch)

export default connect(mapStateToProps, mapDispatchToProps)(Main)
