import { Component, OnInit } from '@angular/core';
import axiosInstance from 'src/app/axiosApi';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username:string
  password:string
  constructor() { }

  ngOnInit(): void {
  }
  async login(){
    const data = new FormData();
    data.append("loginusername",this.username);
    data.append("loginpassword",this.password);
    try {
      const response = await axiosInstance.post("/login",data);
    console.log(response.data.access)
    axiosInstance.defaults.headers['Authorization'] = "Bearer " + response.data.access;
    localStorage.setItem('access_token', response.data.access);
    localStorage.setItem('refresh_token', response.data.refresh);
    if (response.data.access) {
      const stresponse = await axiosInstance.get("/studentapi");
      console.log(stresponse.data)
    }
    } catch (error) {
      console.log(error)
    }
}
}
