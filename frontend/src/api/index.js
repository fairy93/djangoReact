import axios from 'axios'

const SERVER = 'http://127.0.0.1:8000/'
const headers = {'Content-Type':'application/json'}

export const Postwrite = body => axios.post(`${SERVER}board/blog`,{headers,body})
export const memberDetail = body => axios.post(`${SERVER}api/member/detail`,{headers, body})
export const memberDelete = body => axios.delete(`${SERVER}api/member/delete`,{headers, body})
export const memberList = () => axios.get(`${SERVER}adm/member/list`)
export const memberModify = body => axios.post(`${SERVER}api/member/modify`,{headers, body})
export const memberRegister = body => axios.post(`${SERVER}api/member/register`,{headers, body})
export const memberRetrieve = body => axios.post(`${SERVER}adm/member/retrieve`,{headers, body})
export const memberLogin = body => axios.post(`${SERVER}api/member/login`,{headers, body})