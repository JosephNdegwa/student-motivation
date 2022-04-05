import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Post } from '../models/post';
import { AuthenticationService } from '../services/authentication.service';
import { MotivationService } from '../services/motivation.service';

@Component({
  selector: 'app-client',
  templateUrl: './motivation.component.html',
  styleUrls: ['./motivation.component.css']
})
export class MotivationComponent implements OnInit {

 
  posts!:Post[]
  error: any;
  wishlist:any;


  constructor(
    private http: HttpClient,
    private motivationService: MotivationService,
    private authService: AuthenticationService,
    private wishlistService: MotivationService,
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
        // console.log(response)
        resolve()
      },
      (error:string) => {

      })

    })
  }



  addWishlist(id: any){
    console.log(this.wishlist)
    this.motivationService.addToWishlist(this.wishlist, id).subscribe( response => {
      // console.log(response)


      alert('This motivation post has been added to wishlist'),
      this.router.navigate(['landing'])

    },

    error => {
      this.error = error
      console.log('error',error)
    }
    );
  }


  goToUrl(id: any){
    console.log("post_id",id)
    this.router.navigate([`/post/${id}`])
  }


  copyUrl(){
    alert("Motivation link has been copied. Share with your friends!")
  }


}
