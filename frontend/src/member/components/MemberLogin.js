import { memberLogin } from 'api'
import React,{useState} from 'react'
import { Button } from '@material-ui/core';


const MemberLogin = () => {
  const [userInfo, setUserInfo] = useState({
    username: '',
    password: '',
  })

  const {username, password} = `userInfo`

  const handleSubmit = e => {
    e.preventDefault()
    let handleErrors = response => {
      if (!response.ok) {
        throw Error(response.statusText);
      }
      return response;
    }
    
    memberLogin({...userInfo})
    .then(res => {
      alert(`로그인 성공`)
    })
    .catch(err => {
      alert(`로그인 실패 ${err} `)
    })
  }

  const handleClick = e => {
    e.preventDefault()
    alert('취소 클릭')
  }

  const handleChange = e => {
    const { name, value } = e.target
    setUserInfo({
      ...userInfo,
      [name]: value
    })
  }
  
    return (<>
    <h2>Login Form</h2>

    <form onSubmit={handleSubmit} action="/action_page.php" method="post">
      <div className="imgcontainer">
        <img src="https://www.w3schools.com/howto/img_avatar2.png" style={{width: "300px"}} alt="Avatar" className="avatar"/>
      </div>

      <div className="container">
        <label labelFor="uname"><b>UserID</b></label>
        <input type="text" placeholder="Enter ID" onChange={handleChange}   name="username" value={username}/>


        <label labelFor="psw"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" onChange={handleChange}  name="password" value={password}/>
            
        <button type="submit">Login</button>
        <label>
          <input type="checkbox" checked="checked" name="remember"/> Remember me
        </label>
      </div>

      <div className="container" style={{backgroundColor: "#f1f1f1"}}>
        <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
        <span className="psw">Forgot <a href="#">password?</a></span>
      </div>
    </form>
  </>)
}

export default MemberLogin