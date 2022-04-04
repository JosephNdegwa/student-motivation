import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminDashboardComponent } from './admin-dashboard/admin-dashboard.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { SingleMotivationComponent } from './single-motivation/single-motivation.component';

const routes: Routes = [
  {path: '', component:HomeComponent},
  {path: 'login', component:LoginComponent},
  {path: 'register', component:RegisterComponent},
<<<<<<< HEAD
=======
  {path: 'landing', component:LandingComponent},
  {path: 'motivation', component:MotivationComponent},
  {path: 'single-motivation', component:SingleMotivationComponent},
  {path: 'admin-dashboard', component:AdminDashboardComponent}
>>>>>>> b38a996604f13451e641b087784f3ca0c536d2d8

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
