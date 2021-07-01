import React,{useState} from 'react'
import './PostWrite.css'
import { Button } from '@material-ui/core';
import {useHistory} from 'react-router'
import { Postwrite } from 'api';

const PostWrite = () => {
/*
const [post, setPost] =useState({
  title:'',
  content:''
})
  const {title, content} = post
  const handleClick = e => {
    e.preventDefault()
  }
  const handleSubmit = e => {
    e.preventDefault()
  }
  const handleChange = e => {
    const {name: name, value:value} = e.target
    setPost({
      ..post,
      [name] : value
    })
  }*/

  const history = useHistory()
  const [userInfo, setUserInfo] = useState({
    title: '',
    content: ''
  })

  const {title,content} = userInfo


  
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
    Postwrite({...userInfo})
    .then(res=>{
      alert(`전송완료:${res.data.result}`)
      // history.push('login')
    }) //성공
    .catch(err=>{
      alert(`전송 실패:${err}`)
    }) //실패

  }

  const handleClick = e => {
    e.preventDefault()
    alert('취소 클릭')
  }
    return (<>
        <div className="Posts">
        <form onSubmit={handleSubmit} method="post" style={{border:"1px solid #ccc"}}>
          <div className="container">
            <h1>게시글 기</h1>
            <p>Please fill in this form to create an account.</p>
            <hr/>
    
            <label for="title"><b>title</b></label>
            <input type="text" placeholder="Enter title" onChange={handleChange}   name="title" value={title}/>
            <label for="content"><b>content</b></label>
            <input type="text" placeholder="Enter content" onChange={handleChange}  name="content" value={content} />
    
            <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>
    
            <div class="clearfix">
              <button type="submit" className="signupbtn">Sign Up</button>
              <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
              
            </div>
          </div>
      </form>
    </div>
    </>)

   
}

export default PostWrite