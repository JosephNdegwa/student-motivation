import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminDashboardComponent } from './admin-dashboard/admin-dashboard.component';
import { HomeComponent } from './home/home.component';
import { LandingComponent } from './landing/landing.component';
import { LoginComponent } from './login/login.component';
import { MotivationComponent } from './motivation/motivation.component';
import { RegisterComponent } from './register/register.component';
import { SingleMotivationComponent } from './single-motivation/single-motivation.component';

const routes: Routes = [
  {path: '', component:HomeComponent},
  {path: 'login', component:LoginComponent},
  {path: 'register', component:RegisterComponent},
  {path: 'landing', component:LandingComponent},
  {path: 'motivation', component:MotivationComponent},
  {path: 'single-motivation', component:SingleMotivationComponent},
  {path: 'admin-dashboard', component:AdminDashboardComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
