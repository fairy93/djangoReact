import React from 'react'
import { Redirect, Route } from "react-router-dom"
import { MemberDelete, MemberDetail, MemberList, MemberModify, MemberRegister, MemberLogin} from 'member'
import { Home, Member} from 'templates'
import { BrowserRouter as Router } from 'react-router-dom'
import Blog from 'templates/Blog'


const App = () => {
  return (<div>
    <Router>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/member' component={Member}/>
        <Route exact path='/member-delete' component={MemberDelete}/>
        <Route exact path='/member-detail' component={MemberDetail}/>
        <Route exact path='/member-list' component={MemberList}/>
        <Route exact path='/member-modify' component={MemberModify}/>
        <Route exact path='/member-register' component={MemberRegister}/>
        <Route exact path='/member-login' component={MemberLogin}/>

        <Route exact path='/blog' component={Blog}/>

    </Router>
  </div>)
}

export default App