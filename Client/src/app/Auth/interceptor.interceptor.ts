import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HTTP_INTERCEPTORS
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthenticationService } from '../services/authentication.service';
import { BackupService } from '../services/backup.service';

@Injectable()
export class InterceptorInterceptor implements HttpInterceptor {

  constructor(public auth: AuthenticationService, public authBackup : BackupService) {}


  intercept(req: HttpRequest<any>, next: HttpHandler) {
    const authToken = this.authBackup.getToken();
    req = req.clone({
        setHeaders: {
            Authorization: "Bearer " + authToken
        }
    });
    return next.handle(req);
}

}

export const authInterceptorProviders = [
  { provide: HTTP_INTERCEPTORS, useClass: InterceptorInterceptor, multi: true }
];
