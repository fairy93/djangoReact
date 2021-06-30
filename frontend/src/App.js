import React from 'react'
import { Redirect, Route } from "react-router-dom"
import { Login, Signup, UserDetail, UserEdit,UserList  } from 'user'
import { Home, User} from 'templates'
import { Nav } from 'common'
import { BrowserRouter as Router } from 'react-router-dom'
import { Link } from 'react-router-dom'
import { PostWrite } from 'board'
import Blog from 'templates/Blog'
const App = () => {
  return (<div>
    <Router>
        <Nav/>
        {/* <nav style={{width: '500px', margin:'0 auto'}}>
          <ol>
              <li><Link to='/home'>Home</Link></li>
              <li><Link to='/counter'>Counter</Link></li>
              <li><Link to='/todos'>Todos</Link></li>
              <li><Link to='/user'>User</Link></li>
          </ol>
      </nav> */}
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/user' component={User}/>
        <Route exact path='/blog' component={Blog}/>
        <Route exact path='/login' component={Login}/>
        <Route exact path='/post-register' component={PostWrite}/>
        <Route exact path='/signup-form' component={Signup}/>
        <Route exact path='/user-detail' component={UserDetail}/>
        
        <Route exact path='/user-edit' component={UserEdit}/>
        <Route exact path='/user-list' component={UserList}/>
    </Router>
  </div>)
}
// boadd 6°³ ´Ù³Ö¾î³ö ´Ù postwite·Î ÇØ³ö
export default App