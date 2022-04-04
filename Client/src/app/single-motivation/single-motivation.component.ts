import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Post } from 'src/app/models/post';
import { MotivationService } from 'src/app/services/motivation.service';
import { ReviewService } from 'src/app/services/review.service';

@Component({
  selector: 'app-single-motivation',
  templateUrl: './single-motivation.component.html',
  styleUrls: ['./single-motivation.component.css']
})
export class SingleMotivationComponent implements OnInit {


  posts!:Post[]
  error: any;
  post!:any;
  reviewPost:any;
  reviews: any;
  thread:any;
  hideme!: {};




  constructor(
    private http: HttpClient,
    private motivationService: MotivationService,
    private reviewService: ReviewService,
    private route:ActivatedRoute,
    private router: Router,

  )

  { }

  ngOnInit(){

    this.reviewPost = {};


    let id = this.route.snapshot.paramMap.get('id');

    let promise = new Promise <void> ((resolve,reject)=>{
      this.motivationService.getSinglePost(id).toPromise().then(
        (response:any) => {
          // console.log(response)
        this.post = response;
        resolve()
      },

      (error:string) => {

      })
          // Reviews
      this.reviewService.getAllPostReviews(id).toPromise().then(
        (response:any) => {
        this.reviews = response;
        // console.log(response)

        resolve()
      },
      (error:string) => {

      })


    })



    // Jquery
     

   







  }

  toForm(){
    document.getElementById("review-list")?.scrollIntoView({behavior:'smooth', block:'start'});
  }


  postReview(id:any){
    console.log(this.reviewPost)
    this.reviewService.postReview(this.reviewPost, id).subscribe( response => {
      // console.log(response)
      // this.loggedIn.next(true);
      this.router.navigate([`post/${id}`])

    },

    error => {
      this.error = error
      // console.log('error',error)
    }
    );
  }

  showThread(id: any){
  this.reviewService.getReviewThread(id).toPromise().then(
    (response:any) => {
    this.thread = response;
    console.log(response)
  },
  (error:string) => {

  })
}


  threadReview(id:any){
    console.log(this.reviewPost)
    this.reviewService.postReviewThread(this.reviewPost, id).subscribe( response => {
      console.log(response)
      // this.loggedIn.next(true);
      this.router.navigate([`motivation/${id}`])

    },

    error => {
      this.error = error
      console.log('error',error)
    }
    );
  }

  refresh(): void {
    window.location.reload();
  }

  goToUrl(id: any){
    this.router.navigate(['/review',id])
  }

  togglePanel: any = {};

  show = -1;
  toggle (index:any) {

  this.show = index;
}
  isShowComment = true;
  isShowThread = true;


  toggleComment() {
    this.isShowComment = !this.isShowComment;
  }

  toggleThread(id:any) {
    this.isShowThread = !this.isShowThread;
  }


}
