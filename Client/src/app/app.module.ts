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
import { WishlistComponent } from './wishlist/wishlist.component';
import { ClipboardModule } from 'ngx-clipboard';
import { InterceptorInterceptor } from './Auth/interceptor.interceptor';
import { NgHttpLoaderModule } from 'ng-http-loader';
//import { AuthInterceptor } from './services/authconfig.interceptors';
import { TruncateModule } from 'ng2-truncate';

import { HttpClientModule , HTTP_INTERCEPTORS} from '@angular/common/http';


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
    WishlistComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    NgHttpLoaderModule.forRoot(),
    TruncateModule,
    ClipboardModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: InterceptorInterceptor,
      //useClass: AuthInterceptor,
      multi: true
    },
    // provideCloudinary(require('cloudinary-core'), { cloud_name: 'kenya12254' } as CloudinaryConfiguration)


  ],

  bootstrap: [AppComponent]
})
export class AppModule { }
