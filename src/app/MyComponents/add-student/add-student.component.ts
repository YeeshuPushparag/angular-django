import { Component, OnInit } from '@angular/core';
import axiosInstance from 'src/app/axiosApi';
@Component({
  selector: 'app-add-student',
  templateUrl: './add-student.component.html',
  styleUrls: ['./add-student.component.css']
})
export class AddStudentComponent implements OnInit {

  name:string
  email:string
  city:string
  phone:string
  files:any[]
  constructor() { }

  ngOnInit(): void {
  }
  async addStudent(){
    const formdata = new FormData();
    formdata.append("name",this.name);
    formdata.append("email",this.email);
    formdata.append("phone",this.phone);
    formdata.append("city",this.city);
    formdata.append("image",this.files[0]);
        try {
          const response = await axiosInstance.post('/studentapi/',formdata);
          console.log(response)
        } catch (error) {
          console.log(error)
        }
  }
  onFileChange(event){
    this.files = event.target.files;
    console.log(event);
  }
}

