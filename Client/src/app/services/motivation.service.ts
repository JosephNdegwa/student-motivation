import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { MotivationComponent } from '../motivation/motivation.component';

@Injectable({
  providedIn: 'root'
})
export class MotivationService {

  readonly APIUrl = environment.URL;

  constructor(private http: HttpClient) {

  }

  getAllPosts():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + 'post/')
  }


  getSinglePost(id:any):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + `post/mot-id/${id}`)
  }

  filterByCategory(id:any):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + `post/mot-cat/${id}`)
  }


  subscribeCat(subscription:any, id:any):Observable<any[]>{
    return this.http.post<any[]>(this.APIUrl + `subscribe/${id}`, subscription)
  }


  addToWishlist(favPostData:any, id:any){

    return this.http.post<any[]>(this.APIUrl + `wishlist/${id}`, favPostData )
  }

  getWishlistPost():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + 'user_wishlist')
  }



  // /api/wishlist/{id}


  postPost(postData:any){
    // const body = new FormData();
    // body.append('id', motivationData);
    // body.append('files', file, file.name);
    return this.http.post<any[]>(this.APIUrl + 'post/', postData )
  }

  getAllCategories():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + 'category/')

  }

  searchPost(service:string):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + 'api/search/?search='+ service )
  }

}
