import React,{useState} from 'react'
import '../styles/MemberRegister.css'
import { memberRegister } from 'api'
import { Button } from '@material-ui/core';

const MemberRegister = () => {
  const [userInfo, setUserInfo] = useState({
    email: '',
    username: '',
    password: ''
  })

  const {email, username, password} = `userInfo`

  const handleChange = e => {
    const { name, value } = e.target
    setUserInfo({
      ...userInfo,
      [name]: value
    })

  }

  const handleSubmit = e => {
    e.preventDefault()
    alert(`전송 클릭: ${JSON.stringify({...userInfo})}`)
    memberRegister({...userInfo})
    .then(res=>{
      alert(`회원가입 완료`)
    }) 
    .catch(err=>{
      alert(`회원가입 실패 ${err}`)
    }) 
    
  }

  const handleClick = e => {
    e.preventDefault()
    alert('취소 클릭')
  }
    return (<>
    <div className="Signup">
    <form onSubmit={handleSubmit} method="post" style={{border:"1px solid #ccc"}}>
      <div className="container">
        <h1>Sign Up</h1>
        <p>Please fill in this form to create an account.</p>
        <hr/>

        <label for="email"> <b>Email</b></label>
        <input type="text" placeholder="Enter ID" onChange={handleChange}   name="email" value={email}/>

        <label for="password"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" onChange={handleChange}  name="password" value={password}/>

        <label for="username"><b>Username</b></label>
        <input type="text" placeholder="Enter Your Name" onChange={handleChange}  name="username" value={username}/>

        <div class="clearfix">
          <button type="submit" className="signupbtn">Sign Up</button>
          <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button> 
        </div>
      </div>
  </form>
</div>
</>)
}

export default MemberRegister