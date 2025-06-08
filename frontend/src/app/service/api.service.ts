import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private API_URL = 'http://localhost:5000/api';

  constructor(private http: HttpClient) {}

  testConnection(): Observable<any> {
    return this.http.get(`${this.API_URL}/test`);
  }

  register(username: string, correo: string, nacionalidad: string, contraseña: string, ) {
    return this.http.post(`${this.API_URL}/registro`, { username, correo, nacionalidad, contraseña });
  }

  login(correo: string, contraseña: string) {
    return this.http.post<{ access_token: string }>(`${this.API_URL}/login`, { correo, contraseña })
      .pipe(
        map(response => {
          localStorage.setItem('token', response.access_token);
          return response;
        })
      );
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
