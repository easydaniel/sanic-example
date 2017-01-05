import React, { Component } from 'react'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import injectTapEventPlugin from 'react-tap-event-plugin'

import AppBar from 'material-ui/AppBar'
import FlatButton from 'material-ui/FlatButton'
import Dialog from 'material-ui/Dialog'
import TextField from 'material-ui/TextField'

import * as Action from '../actions/Base'

class Base extends Component {

    componentWillMount () {
        injectTapEventPlugin()
        this.state = {
            loginOpen: false
        }
    }

    handleLogin () {
        let payload = {
            username: this.refs.username.getValue(),
            password: this.refs.password.getValue()
        }
        this.props.login(payload)
        this.setState({ loginOpen: false })
    }

    handleSignUp () {
        let payload = {
            username: this.refs.username.getValue(),
            password: this.refs.password.getValue()
        }
        console.log(payload)
        this.setState({ loginOpen: false })
    }

    render () {
        let {loginOpen} = this.state
        const actions = [
            <FlatButton
              label="Cancel"
              secondary={true}
              onTouchTap={() => this.setState({ loginOpen: false })}
            />,
            <FlatButton
              label="Login"
              primary={true}
              onTouchTap={() => this.handleLogin()}
            />,
            <FlatButton
              label="Sign Up"
              primary={true}
              onTouchTap={() => this.handleSignUp()}
            />
        ]
        return (
            <MuiThemeProvider>
              <div>
                <AppBar
                  title='Loan System'
                  iconElementRight={<FlatButton
                                    onTouchTap={() => this.setState({ loginOpen: true })}
                                    label="Login" />}
                />
                <Dialog
                  title="Login"
                  actions={actions}
                  modal={false}
                  open={loginOpen}
                  onRequestClose={() => this.setState({ loginOpen: false })}
                >
                  <TextField
                    ref="username"
                    hintText="Username"
                  /><br/>
                  <TextField
                    ref="password"
                    type="password"
                    hintText="Password"
                  />
                </Dialog>
              </div>
            </MuiThemeProvider>
        )
    }
}

const mapStateToProps = (state) => ({
    base: state.base
})

const mapDispatchToProps = (dispatch) => bindActionCreators({...Action}, dispatch)

export default connect(mapStateToProps, mapDispatchToProps)(Base)
