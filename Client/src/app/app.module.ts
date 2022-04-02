import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AdminDashboardComponent } from './admin-dashboard/admin-dashboard.component';
import { FilterCategoryComponent } from './filter-category/filter-category.component';
import { LandingComponent } from './landing/landing.component';
import { MotivationComponent } from './motivation/motivation.component';
import { ProfileComponent } from './profile/profile.component';
import { ReviewThreadComponent } from './review-thread/review-thread.component';
import { SingleMotivationComponent } from './single-motivation/single-motivation.component';
import { WishlistComponent } from './wishlist/wishlist.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    HomeComponent,
    NavbarComponent,
    AdminDashboardComponent,
    FilterCategoryComponent,
    LandingComponent,
    MotivationComponent,
    ProfileComponent,
    ReviewThreadComponent,
    SingleMotivationComponent,
    WishlistComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
