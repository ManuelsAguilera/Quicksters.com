import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { tap,map } from 'rxjs/operators';



@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private API_URL = 'http://localhost:5000';


  //Trackear estado de autenticación del usuario
  private authState = new BehaviorSubject<boolean>(!!localStorage.getItem('token'));
  public isAuthenticated$ = this.authState.asObservable();


  constructor(private http: HttpClient) {}

  testConnection(): Observable<any> {
    return this.http.get(`${this.API_URL}/api/test`);
  }

  register(username: string, correo: string, nacionalidad: string, contraseña: string, ) {
    return this.http.post(`${this.API_URL}/registro`, { username, correo, nacionalidad, contraseña });
  }

  login(correo: string, contraseña: string) {
    return this.http.post<{ access_token: string }>(`${this.API_URL}/login`, { correo, contraseña })
      .pipe(
        tap(response => {
          localStorage.setItem('token', response.access_token);
          this.authState.next(true);
          return response;
        })
      );
  }

  isAuthenticated(): boolean {
    return this.authState.value;
  }
  logout() {
    localStorage.removeItem('token');
    this.authState.next(false);
  }
  getProfile() {
    const token = localStorage.getItem('token');
    return this.http.get(`${this.API_URL}/profile`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
  }
}
