import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { Category } from 'src/app/models/category';
import { Post } from 'src/app/models/post';
import { StudentUser } from 'src/app/models/student-user';
import { Subscription } from 'src/app/models/subscription';
import { BackupService } from 'src/app/services/backup.service';
import { CategoryService } from 'src/app/services/category.service';
import { MotivationService } from 'src/app/services/motivation.service';

@Component({
  selector: 'app-filter-category',
  templateUrl: './filter-category.component.html',
  styleUrls: ['./filter-category.component.css']
})
export class FilterCategoryComponent implements OnInit {

  posts!:Post[];
  // motivations!: any;

  categories:any;
  error: any;
  subscription: any;
  wishlist:any;
  category:any;
  currentUser!:StudentUser;



  constructor(
    private http: HttpClient,
    private motivationService: MotivationService,
    private categoryService: CategoryService,
    private authBackup: BackupService,
    private route:ActivatedRoute,
    private router: Router,


  )

  { }

  ngOnInit(){
    let id = this.route.snapshot.paramMap.get('id');
    let promise = new Promise <void> ((resolve,reject)=>{
      // motivations
      this.motivationService.filterByCategory(id).toPromise().then(
        (response:any) => {
        this.posts = response;
        resolve()
      },
      (error:string) => {

      })

      this.categoryService.getSingleCategory(id).toPromise().then(
        (response:any) => {
          // console.log(response)
        this.category = response;
        resolve()
      },

      (error:string) => {

      })

        // categories
      this.motivationService.getAllCategories().toPromise().then(
        (response:any) => {
        this.categories = response;
        resolve()
      },
      (error:string) => {

      })
      this.authBackup.getCurrentUser().pipe(first()).subscribe((loggedUser: StudentUser) => {
        this.currentUser = loggedUser;
        // console.log(loggedUser)
      });


    })
  }

  addWishlist(id: any){
    this.motivationService.addToWishlist(this.wishlist, id).subscribe( response => {
      console.log(response)

      alert('This motivation post has been added to wishlist')
      // this.router.navigate(['home'])

    },

    error => {
      this.error = error
      console.log('error',error)
    }
    );
  }


  subscribeToCat(id: any){
    console.log(this.subscription)
    this.motivationService.subscribeCat(this.subscription, id).subscribe( response => {
      console.log(response)

      alert('You have successfully subscribed to this category ')
      // this.router.navigate(['home'])

    },

    error => {
      this.error = error
      console.log('error',error)
    }
    );
  }

   goToCategory(id: any){
    this.router.navigate(['/category',id])
  }

  refresh(): void {
    window.location.reload();
  }
  goToUrl(id: any){
    this.router.navigate(['/motivation',id])
  }

  copyUrl(){
    alert("Motivation link has been copied. Share with your friends!")
  }


}
