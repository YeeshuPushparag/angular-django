import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './MyComponents/about/about.component';
import { AddStudentComponent } from './MyComponents/add-student/add-student.component';
import { LoginComponent } from './MyComponents/login/login.component';
import { SignupComponent } from './MyComponents/signup/signup.component';
import { TodosComponent } from './MyComponents/todos/todos.component';

const routes: Routes = [
  {path:"",component: TodosComponent},
  {path:"about",component: AboutComponent},
  {path:"login",component: LoginComponent},
  {path:"signup",component: SignupComponent},
  {path:"student",component: AddStudentComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
