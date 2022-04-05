import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminDashboardComponent } from './admin-dashboard/admin-dashboard.component';
import { HomeComponent } from './home/home.component';
import { LandingComponent } from './landing/landing.component';
import { LoginComponent } from './login/login.component';
import { MotivationComponent } from './motivation/motivation.component';
import { ProfileComponent } from './profile/profile.component';
import { RegisterComponent } from './register/register.component';
import { ReviewThreadComponent } from './review-thread/review-thread.component';
import { SingleMotivationComponent } from './single-motivation/single-motivation.component';
import { AuthGuard } from './authguard/auth.guard';

const routes: Routes = [
  {path: '', component:HomeComponent},
  {path: 'login', component:LoginComponent},
  {path: 'register', component:RegisterComponent},
  {path: 'landing', component:LandingComponent},
  {path: 'motivation', component:MotivationComponent},
  {path: 'single-motivation', component:SingleMotivationComponent},
  {path: 'admin-dashboard', component:AdminDashboardComponent},
  {path: 'profile', component:ProfileComponent},
  {path: 'review/:id', component:ReviewThreadComponent,canActivate: [AuthGuard] },

  { path: 'post/:id', component: SingleMotivationComponent,canActivate: [AuthGuard] },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
