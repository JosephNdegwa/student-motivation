import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { Category } from 'src/app/models/category';
import { Post } from 'src/app/models/post';
import { StudentUser } from 'src/app/models/student-user';
import { Subscription } from 'src/app/models/subscription';
import { Wishlist } from 'src/app/models/wishlist';
import { BackupService } from 'src/app/services/backup.service';
import { MotivationService } from 'src/app/services/motivation.service';

import { CategoryService } from 'src/app/services/category.service';

@Component({
  selector: 'app-wishlist',
  templateUrl: './wishlist.component.html',
  styleUrls: ['./wishlist.component.css']
})
export class WishlistComponent implements OnInit {

  wishlist!:Wishlist[];




  constructor(
    private http: HttpClient,
    private wishlistService: MotivationService,
    private route:ActivatedRoute,
    private router: Router,


  )

  { }

  ngOnInit(){
    let promise = new Promise <void> ((resolve,reject)=>{
      this.wishlistService.getWishlistPost().toPromise().then(
        (response:any) => {
        this.wishlist = response;
        resolve()
      },
      (error:string) => {

      })


    })
  }



  refresh(): void {
    window.location.reload();
  }
  goToUrl(id: any){
    this.router.navigate(['/post',id])
  }

  copyUrl(){
    alert("Motivation link has been copied. Share with your friends!")
  }


}
