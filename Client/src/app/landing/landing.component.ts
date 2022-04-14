import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import {Post } from 'src/app/models/post';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { MotivationService } from 'src/app/services/motivation.service';
import { Router } from '@angular/router';
import * as $ from 'jquery';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css'],
})
export class LandingComponent implements OnInit {

  posts!:Post[]
  categories:any
  error: any;

  constructor(
    private http: HttpClient,
    private motivationService: MotivationService,
    private authService: AuthenticationService,
    private router: Router,

  )

  { }

  ngOnInit(){
    let promise = new Promise <void> ((resolve,reject)=>{
      // motivations
      this.motivationService.getAllPosts().toPromise().then(
        (response:any) => {
        // console.log(response)
        this.posts = response;
        resolve()
      },
      (error:string) => {

      })
        // categories
      this.motivationService.getAllCategories().toPromise().then(
        (response:any) => {
          // console.log(response)
        this.categories = response;
        resolve()
      },
      (error:string) => {

      })
    })
  }

  goToCategory(id: any){
    this.router.navigate(['/category',id])
  }
}