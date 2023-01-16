import { Component, OnInit } from '@angular/core';
import axiosInstance from 'src/app/axiosApi';
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  username:string
  fname:string
  lname:string
  email:string
  password:string
  cpassword:string
  files:any[]
  constructor() { }

  ngOnInit(): void {
  }
  async addStudent(){
    const formdata = new FormData();
    formdata.append("username",this.username);
    formdata.append("firstname",this.fname);
    formdata.append("lastname",this.lname);
    formdata.append("email",this.email);
    formdata.append("password",this.password);
    formdata.append("cpassword",this.cpassword);
    formdata.append("image",this.files[0]);
        try {
          const response = await axiosInstance.post('/signup',formdata);
          console.log(response.data.access)
          axiosInstance.defaults.headers['Authorization'] = "Bearer " + response.data.access;
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
        } catch (error) {
          console.log(error)
        }
  }
  onFileChange(event){
    this.files = event.target.files;
    console.log(event);
  }
}


